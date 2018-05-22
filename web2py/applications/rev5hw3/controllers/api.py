# Here go your api methods.
# These are the controllers for your ajax api.


def get_user_name_from_email(email):
    u = db(db.auth_user.email == email).select().first()
    if u is None:
        return 'None'
    else:
        return ' '.join([u.first_name, u.last_name])


def get_posts():
    start_index = int(request.vars.start_index) if request.vars.start_index is not None else 0
    end_index = int(request.vars.end_index) if request.vars.end_index is not None else 0
    # We just generate a lot of of data.
    posts = []
    has_more = False

    rows = db().select(db.post.ALL, orderby=~db.post.created_on, limitby=(start_index, end_index + 1))
    for i, r in enumerate(rows):
        name = get_user_name_from_email(r.user_email)
        if i < end_index - start_index:
            t = dict(
                id=r.id,
                user_email=r.user_email,
                title = r.title,
                content=r.post_content,
                is_public = r.is_public
            )
            posts.append(t)
        else:
            has_more = True
    logged_in = auth.user_id is not None
    return response.json(dict(
        posts=posts,
        logged_in=logged_in,
        has_more=has_more,
    ))


# Note that we need the URL to be signed, as this changes the db.
@auth.requires_signature()
def add_post():
    user_email = auth.user.email or None
    p_id = db.post.insert(title=request.vars.title,post_content=request.vars.content) ###edit by Tyler
    p = db.post(p_id)
    name = get_user_name_from_email(p.user_email)
    post = dict(
            id=p.id,
            user_email=p.user_email,
            title = p.title,    ####edit by Tyler
            content=p.post_content
    )
    print p
    return response.json(dict(post=post))

@auth.requires_signature()
def edit_post():
    post = db(db.post.id == request.vars.id).select().first() # update record with
    post.update_record(title=request.vars.title,post_content=request.vars.post_content) # update record with new title and content
    return dict()


@auth.requires_signature()
def toggle_post():
    post = db(db.post.id == request.vars.post_id).select().first()
    post.update_record(is_public=request.vars.is_public) 
    print post
    return dict()

@auth.requires_signature()
def del_post():
    db(db.post.id == request.vars.post_id).delete()
    return "ok"


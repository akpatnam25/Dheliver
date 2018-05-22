# Here go your api methods.

# Function to retrieve memos
def get_memos():
    
    memos = []
    has_more = False
    checklists = None
    logged_in = auth.user is not None
    
    # get length of memo list
    start_index = (int(request.vars.start_index) if request.vars.start_index
                                                    is not None else 0)
    end_index = (int(request.vars.end_index) if request.vars.end_index
                                                    is not None else 0)
    
    # get memos
    if auth.user is not None:   # added all public memos
        checklists = db((db.checklist.user_email == auth.user.email) |
                        (db.checklist.is_public == True)).select(db.checklist.ALL, limitby=(start_index, end_index+1))
    else:   # make public memos visible when not logged in
        checklists = db(db.checklist.is_public == True).select(db.checklist.ALL, limitby=(start_index, end_index+1))
    
    # get a certain amount of memos from the list
    for i, r in enumerate(checklists):
        if i < end_index - start_index:
            temp = dict(id = r.id,
                        user_email = r.user_email,
                        title = r.title,
                        memo = r.memo,
                        updated_on = r.updated_on,
                        is_public = r.is_public)
            memos.append(temp)
        else:
            has_more = True
    
    return response.json(dict(memos = memos,
                              logged_in = logged_in,
                              has_more = has_more))

# The old no swearing function
@auth.requires_signature()
def no_swearing(form):
    if 'fool' in form.vars.memo:
        form.errors.memo = T('No swearing please')

# Add memo to database
@auth.requires_signature()
def add_memo():
    """Adds a checklist."""
    m_id = db.checklist.insert(title = request.vars.title,
                               memo = request.vars.memo)
    m = db.checklist(m_id)
    return response.json(dict(memo=m))

# Delete memo from database
@auth.requires_signature()
def delete_memo():
    db((db.checklist.user_email == auth.user.email) &
             (db.checklist.id == request.vars.memo_id)).delete()
    return dict()

# Toggle public function to toggle public or private
@auth.requires_signature()
def toggle_public():
    item = db((db.checklist.user_email == auth.user.email) &
             (db.checklist.id == request.vars.memo_id)).select().first()
    toggle = not item.is_public
    item.update_record(is_public = not item.is_public)
    return response.json(dict(toggle=toggle))

# Update an edited memo
@auth.requires_signature()
def edit_memo():
    item = db((db.checklist.user_email == auth.user.email) &
             (db.checklist.id == request.vars.memo_id)).select().first()
    item.update_record(title = request.vars.title)
    item.update_record(memo = request.vars.memo)
    return dict()

import tempfile

# Here go your api methods.

# To do:
# Form checking (check that the form is not empty when a new track is added)
# User checking
# Sharing

# Let us have a serious implementation now.



def get_memos():
    start_idx = int(request.vars.start_idx) if request.vars.start_idx is not None else 0
    end_idx = int(request.vars.end_idx) if request.vars.end_idx is not None else 0
    checklists = []
    has_more_memo = False
    rows = db().select(db.checklist.ALL, limitby=(start_idx, end_idx + 1))
    for i, r in enumerate(rows):
        if i < end_idx - start_idx:
            # Check if I have a track or not.
            memos_url = (
                URL('api', 'play_track', vars=dict(memo_id=r.id), user_signature=True)
                if r.has_memo else None)
            t = dict(
                id = r.id,
                title = r.title,
                description = r.description,
                is_public = r.is_public,
                is__editing_memo = r.is_editing_memo,
                memos_url = memos_url,
            )
            checklists.append(t)
        else:
            has_more_memo = True
    logged_in = auth.user is not None
    return response.json(dict(
        checklists=checklists,
        logged_in=logged_in,
        has_more_memo=has_more_memo,
    ))

@auth.requires_signature()
def add_memo():
    m_id = db.checklist.insert(
        title=request.vars.title,
        description=request.vars.description,
    )
    m = db.checklist(m_id)
    return response.json(dict(checklist=m))

@auth.requires_signature()
def delete_memo():
    "Deletes a track from the table"
    db(db.checklist.id == request.vars.memo_id).delete()
    return "ok"


@auth.requires_signature()
def play_memo():
    memo_id = int(request.vars.memo_id)
    m = db(db.checklist.memo_id == memo_id).select().first()
    if m is None:
        return HTTP(404)
    headers = {}
    headers['Content-Type'] = m.mime_type
    # Web2py is setup to stream a file, not a data blob.
    # So we create a temporary file and we stream it.
    # f = tempfile.TemporaryFile()
    f = tempfile.NamedTemporaryFile()
    f.write(m.data_blob)
    f.seek(0) # Rewind.
    return response.stream(f.name, chunk_size=4096, request=request)

@auth.requires_login()
def edit_memo():
    db.checklist.id == request.vars.memo_id
    db(db.checklist.id).delete()
    m_id = db.checklist.insert(
        title=request.vars.title,
        description=request.vars.description,
    )
    m = db.checklist(m_id)

    return response.json(dict(checklist=m))


@auth.requires_signature()
def toggle_visibility():
    db.checklist.id == request.vars.memo_id
    m = db(db.checklist.id).select().first()
    m = db.checklist.id == request.vars.is_public
    m = db(db.checklist.id).select().first()
    if m == True:
        m.update_record(is_public=False)
    elif m.is_public == False:
        m.update_record(is_public=True)

    # cl = m.is_public
    # cl.update_record(is_public=not value)
    return response.json(dict(checklist=m))



# Here go your api methods.

# Required page info
def index():
	# Get memos sorted by update date
	
	if auth.user is not None:
		# Get the user's checklists and public lists
		checklists = db((db.checklist.user_email == auth.user.email) 
		                | (db.checklist.is_public == True)).select(
			                orderby=~db.checklist.updated_on,
		                )
	else:
		# Get public lists
		checklists = db(db.checklist.is_public == True).select(
			                orderby=~db.checklist.updated_on,
		                )

	return response.json(dict(
														checklists = checklists,
														logged_in = auth.user is not None,
														email = None if auth.user is None else auth.user.email
														))

# Create new memos
@auth.requires_login()
@auth.requires_signature()
def memo_new():
	id = db.checklist.insert(
													title = request.vars.title,
													memo = request.vars.content,
													)
	# Return the full database entry
	return response.json(dict(
														new_memo = db(db.checklist.id == id).select().first()
														))


# Edits existing memo
@auth.requires_login()
@auth.requires_signature()
def memo_edit():
	cl = get_user_memo_by_id(request.vars.id)
	cl.update_record(
	                 title=request.vars.title,
	                 memo=request.vars.memo
	                 )
	
	return HTTP(200)

# Toggles the value of is_true for a checklist item
@auth.requires_login()
@auth.requires_signature()
def memo_toggle_public():
  cl = get_user_memo_by_id(request.vars.id)
  # Update is_public
  cl.update_record(is_public=not cl.is_public)
  return HTTP(200)

# Deletes a memo
@auth.requires_login()
@auth.requires_signature()
def memo_delete():
  get_user_memo(request.vars.id).delete()
  return HTTP(200)


# Helper functions

# Returns a database query for a user memo
def get_user_memo(id):
	return db((db.checklist.user_email == auth.user.email) & (db.checklist.id == id))

# Gets a memo by id, returns 401 if the memo does not belong to the user
def get_user_memo_by_id(id):
	cl = get_user_memo(id).select().first()
	# I fish out the first element of the query, if there is one, otherwise None.
	if cl is None:
	  # The record exists but is by another user
	  session.flash = T('Not Authorized')
	  return HTTP(401)
	return cl

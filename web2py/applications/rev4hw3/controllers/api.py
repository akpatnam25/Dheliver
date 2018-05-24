# Here go your api methods.

def get_memos():
	start_index = int(request.vars.start_index) if request.vars.start_index is not None else 0
	end_index = int(request.vars.end_index) if request.vars.end_index is not None else 0

	memos = []
	has_more = False
	user_email = None

	logged_in = auth.user is not None
	if logged_in:
		# Return memos that belong to the user or are public.
		user_email = auth.user.email
		q = ((db.memos.user_email == auth.user.email) | (db.memos.is_public == True))
	else:
		# Return public memos only.
		q = (db.memos.is_public == True)

	rows = db(q).select(db.memos.ALL, limitby=(start_index, end_index + 1))
	for index, row in enumerate(rows):
		if index < end_index - start_index:
			# Add memos corresponding to (start_index, end_index) to memos.
			memo = dict(
				id = row.id,
				user_email = row.user_email,
				title = row.title,
				memo = row.memo,
				is_public = row.is_public,
			)
			memos.append(memo)
		else:
			# If there is an additional memo, set has_more to True.
			has_more = True

	# Return the query results.
	return response.json(dict(
			memos=memos,
			logged_in=logged_in,
			user_email=user_email,
			has_more=has_more,
		))

@auth.requires_login()
@auth.requires_signature()
def add_memo():
	# Add the new memo to the database table: memos.
	memo_id = db.memos.insert(
			title = request.vars.title,
			memo = request.vars.memo,
	)

	# Return the added memo to the user.
	added_memo = db.memos(memo_id)
	return response.json(dict(memo=added_memo))


@auth.requires_login()
@auth.requires_signature()
def edit_memo():
	# If no memo id is provided, raise an error.
	memo_id = request.vars.memo_id
	if memo_id is None:
		raise HTTP(500)

	# Retrieve the corresponding memo from the database.
	# Raise an error if:
	# 1) the memo doesn't exist.
	# 2) the requester does not own the memo.
	q = ((db.memos.user_email == auth.user.email) & (db.memos.id == memo_id))
	memo = db(q).select().first()
	if memo is None:
		raise HTTP(500)

	# Update the memo.
	memo.update_record(
		title = request.vars.title,
		memo = request.vars.memo
	)
	return 'ok'


@auth.requires_login()
@auth.requires_signature()
def delete_memo():
	# If no memo id is provided, raise an error.
	memo_id = request.vars.memo_id
	if memo_id is None:
		raise HTTP(500)

	# Retrieve the corresponding memo from the database.
	# Raise an error if:
	# 1) the memo doesn't exist.
	# 2) the requester does not own the memo.
	q = ((db.memos.user_email == auth.user.email) & (db.memos.id == memo_id))
	memo = db(q).select().first()
	if memo is None:
		raise HTTP(500)

	# Delete the memo.
	memo.delete_record()
	return 'ok'


@auth.requires_signature()
def toggle_visibility():
	# If no memo id is provided, raise an error.
	memo_id = request.vars.memo_id
	if memo_id is None:
		raise HTTP(500)

	# Retrieve the corresponding memo from the database.
	# Raise an error if:
	# 1) the memo does not exist.
	# 2) the requester does not own the memo.
	q = ((db.memos.user_email == auth.user.email) & (db.memos.id == memo_id))
	memo = db(q).select().first()
	if memo is None:
		raise HTTP(500)

	# Update the memo's is_public value.
	toggled_value = not(memo.is_public)
	memo.update_record(is_public=toggled_value)
	return 'ok'

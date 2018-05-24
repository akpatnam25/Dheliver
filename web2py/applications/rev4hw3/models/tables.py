# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

import datetime

def get_user_email():
	return auth.user.email if auth.user is not None else None

db.define_table('memos',
				Field('user_email', default=get_user_email()),
				Field('title'),
				Field('memo', 'text'),
				Field('updated_on', 'datetime', update=datetime.datetime.utcnow()),
				Field('is_public', 'boolean', default=False)
				)

db.memos.id.writable = db.memos.id.readable = False
db.memos.user_email.writable = db.memos.user_email.readable = False
db.memos.updated_on.writable = db.memos.updated_on.readable = False
db.memos.is_public.writable = db.memos.is_public.readable = False

# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

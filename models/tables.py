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


db.define_table('checklist',
                Field('user_email', default=get_user_email()),
                Field('Delivery_Time'),
                Field('title'),
                Field('memo', 'text'),
                Field('Additional_Instructions', 'text'),
                Field('updated_on', 'datetime', update=datetime.datetime.now()),
                Field('is_public', 'boolean',default=False),
                Field('phone_number'),
                )

db.define_table('orderlist',
                Field('user_email', default=get_user_email()),
                Field('dh', 'text'),
                Field('times', 'text'),
                Field('menu_item', 'text'),
                Field('updated_on', 'datetime', update=datetime.datetime.now()),
                Field('is_public', 'boolean',default=False),
                )


db.checklist.user_email.writable = False
db.checklist.user_email.readable = False
db.checklist.title.writable = False
db.checklist.title.readable = False
db.checklist.memo.writable = False
db.checklist.memo.readable = False
db.checklist.is_public.writable = False
db.checklist.is_public.readable = False
db.checklist.updated_on.writable = db.checklist.updated_on.readable = False
db.checklist.id.writable = db.checklist.id.readable = False


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)

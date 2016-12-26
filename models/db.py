db = DAL("sqlite://storage.sqlite")

db.define_table('item',
                Field('title'),
                Field('Material'),
                Field('price', 'double'),
                Field('file', 'upload'),
                Field('sold', 'boolean'),
                Field('shipping'),
                Field('description', 'text'),
                Field('care', 'text'))

db.define_table('post',
                Field('item_id', 'reference item'),
                Field('author'),
                Field('email'),
                Field('body', 'text'))

db.define_table('sale',
                Field('item_id', 'reference item'),
                Field('name'),
                Field('address'),
                Field('city'),
                Field('state'),
                Field('zip'),
                Field('email'),
                Field('body', 'text'))

db.item.title.requires = IS_NOT_IN_DB(db, db.item.title)
db.post.item_id.requires = IS_IN_DB(db, db.item.id, '%(title)s')
db.post.author.requires = IS_NOT_EMPTY()
db.post.email.requires = IS_EMAIL()
db.post.body.requires = IS_NOT_EMPTY()

db.post.item_id.writable = db.post.item_id.readable = False

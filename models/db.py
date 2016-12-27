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

db.define_table('orderform',
                Field('item_id', 'reference item'),
                Field('name'),
                Field('address'),
                Field('city'),
                Field('state'),
                Field('zip'),
                Field('shipped', 'boolean'))

db.define_table('post',
                Field('item_id', 'reference item'),
                Field('author'),
                Field('nix'),
                Field('body', 'text'))


db.post.item_id.requires = IS_IN_DB(db, db.item.id, '%(title)s')
db.post.author.requires = IS_NOT_EMPTY()
db.post.body.requires = IS_NOT_EMPTY()

db.post.item_id.writable = db.post.item_id.readable = False
db.orderform.item_id.writable = db.orderform.item_id.readable = False
db.orderform.shipped.writable = db.orderform.shipped.readable = False

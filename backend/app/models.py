from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # not unique because it is possible that one warehouse has some of a particular item, and another has the rest of it. so, 
    # i have made both name and warehouse not unique, but adding another item of the same name will result in an increment, not a
    # new item (this will be more clear in the ui)
    name = db.Column(db.String(64), index=True, unique=False)
    quantity = db.Column(db.Integer, unique=False)
    warehouse = db.relationship('Location')

class Warehouse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=False)

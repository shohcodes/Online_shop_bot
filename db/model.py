from db.config import DB


class Baskets(DB):
    def __init__(self , *fields):
        self.fields = fields

class Clients(DB):
    def __init__(self , *fields):
        self.fields = fields


class Merchants(DB):
    def __init__(self , *fields):
        self.fields = fields

class Orders(DB):
    def __init__(self , *fields):
        self.fields = fields

class Products(DB):
    def __init__(self , *fields):
        self.fields = fields










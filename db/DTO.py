class ClientDto:
    def __init__(self,
                 id: int = None,
                 user_id: int = None,
                 fullname: str = None,
                 phone: str = None,
                 password: str = None,
                 location: str = None,
                 status: str = None,
                 created_at: str = None):
        self.id = id
        self.user_id = user_id
        self.fullname = fullname
        self.phone = phone
        self.password = password
        self.location = location
        self.status = status
        self.created_at = created_at


class MerchantDto:
    def __init__(self,
                 id: int = None,
                 full_name: str = None,
                 phone: int = None,
                 email: str = None,
                 passwoed: str = None,
                 status: str = None,
                 created_at: str = None
                 ):
        self.id = id
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.passwoed = passwoed
        self.status = status
        self.created_at = created_at


class BasketDto:
    def __init__(self,
                 id: int = None,
                 product_id: int = None,
                 user_id: int = None,
                 count: int = None,
                 created_at: str = None):
        self.id = id
        self.product_id = product_id
        self.user_id = user_id
        self.count = count
        self.created_at = created_at


class OrdersDto:
    def __init__(self,
                 id: int = None,
                 customer_id: int = None,
                 merchant_id: int = None,
                 basket_id: int = None,
                 payment_method: str = None,
                 total: float = None,
                 created_at: str = None):
        self.id = id
        self.customer_id = customer_id
        self.merchant_id = merchant_id
        self.basket_id = basket_id
        self.payment_method = payment_method
        self.total = total
        self.created_at = created_at


class ProductDto:
    def __int__(self,
                id: int = None,
                name: str = None,
                price: float = None,
                term: str = None,
                discount: float = None,
                status: str = None,
                is_sold_out: bool = None,
                merchant_id: bool = None,
                created_at: str = None):
        self.id = id
        self.name = name
        self.price = price
        self.term = term
        self.discount = discount
        self.status = status
        self.is_sold_out = is_sold_out
        self.merchant_id = merchant_id
        self.created_at = created_at

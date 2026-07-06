from models import Product


'''create'''
def add_product(name: str, price: float, category: str):
    return Product.create(name=name, price=price, category=category)


'''read'''
def get_categories():
    return Product.select(Product.category.distinct()).order_by(Product.category)

def get_products():
    return Product.select()

'''update'''


'''delete'''
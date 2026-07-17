from models import Product, Company


'''create'''
def add_product(name: str, price: float, category: str):
    return Product.create(name=name, price=price, category=category)


'''read'''
def get_categories():
    products = Product.select(Product.category.distinct()).order_by(Product.category)
    categories = [product.category for product in products]
    return categories

def get_products():
    return Product.select()

def get_products_by_category(category: str):
    return Product.select().where(Product.category == category)

def product_exists(name: str) -> bool:
    return Product.select().where(Product.name == name).exists()

# for edit
def product_current_price(name: str):
    product = Product.get(Product.name == name)
    return product.price

def product_current_category(name: str):
    product = Product.get(Product.name == name)
    return product.category
# ---------

'''update'''
def edit_product(name: str, price: float, category: str):
    return Product.update(price= price, category= category).where(Product.name == name).execute()


'''delete'''
def delete_product(name: str):
    return Product.delete().where(Product.name == name).execute()


# ===== Company ==================
'''create'''
def add_company(name: str, password: str):
    return Company.create(name= name, password= password)


''' read '''
def get_company_by_name(name: str) -> Company:
    return Company.get_or_none(Company.name == name)

def company_exists(name: str) -> bool:
    return Company.select().where(Company.name == name).exists()

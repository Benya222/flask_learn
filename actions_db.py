from models import Product, Company


'''create'''
def add_product(name: str, price: float, category: str, company: int):
    return Product.create(name=name, price=price, category=category, company_id= company)


'''read'''
def get_categories(company: int):
    products = Product.select(Product.category.distinct()).where(Product.company_id == company).order_by(Product.category)
    categories = [product.category for product in products]
    return categories

def get_products(company: int):
    return Product.select().where(Product.company_id == company)

def get_products_by_category(category: str, company: int):
    return Product.select().where((Product.category == category)&(Product.company_id == company))

def product_exists(name: str, company: int) -> bool:
    return Product.select().where((Product.name == name)&(Product.company_id == company)).exists()

# for edit
def product_current_price(name: str, company: int):
    product = Product.get((Product.name == name)&(Product.company_id == company))
    return product.price

def product_current_category(name: str, company: int):
    product = Product.get((Product.name == name)&(Product.company_id == company))
    return product.category
# ---------

'''update'''
def edit_product(name: str, price: float, category: str, company: int ):
    Product.update(price= price, category= category).where((Product.name == name)&(Product.company_id == company)).execute()


'''delete'''
def delete_product(name: str, company: int):
    Product.delete().where((Product.name == name)&(Product.company_id == company)).execute()


# ===== Company ==================
'''create'''
def add_company(name: str, password: str):
    return Company.create(name= name, password= password)


''' read '''
def get_company_by_name(name: str) -> Company:
    return Company.get_or_none(Company.name == name)

def company_exists(name: str) -> bool:
    return Company.select().where(Company.name == name).exists()

from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from actions_db import *


product_bp = Blueprint('product', __name__, template_folder= 'templates')


def is_logged():
    return 'company' in session

def current_company():
    return get_company_by_name(session['company'])


@product_bp.route('/', methods= ['GET', 'POST'])
@product_bp.route('/products', methods= ['GET', 'POST'])
def products():
    session.permanent = True
    
    if not is_logged():
        return redirect(url_for('login'))
    
    company = current_company()
    

    
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        price = float(price)
        
        if product_exists(name, company.id):
            flash('Такий товар вже є!', category="error")
        else:
            add_product(name, price, category, company.id)

        return redirect(url_for('product.products'))

    all_categories = get_categories(company.id)
    choose_category = request.args.get('category', 'all')

    if choose_category == 'all':
        filter_product = get_products(company.id)
    else:
        filter_product = get_products_by_category(choose_category, company.id)
 


    return render_template('product/product.html',
                           products= filter_product, 
                           categories= all_categories,
                           choose_category= choose_category,
                           company=current_company
                           )

@product_bp.route('/edit/<name>', methods= ['GET', 'POST'])
def edit(name):
    company = current_company()

    current_price = str(product_current_price(name, company.id))
    current_category = product_current_category(name, company.id)

    
    if request.method == 'POST':
        price = request.form.get('new-price')
        category = request.form.get('new-category')

        edit_product(name, price, category, company.id)
        
        flash('Product edited!', category="success")
        return redirect(url_for('product.products'))


    return render_template('product/edit.html', 
                           current_price= current_price, 
                           current_category= current_category,
                           title= name,
                           company= company
                           )

@product_bp.route('/delete/<name_product>')
def delete(name_product):
    company = current_company()
    delete_product(name_product, company.id)
    flash(f'Product {name_product} was deleted!', category="success")

    return redirect(url_for('product.products'))



from flask import Flask, render_template, request, flash, redirect, url_for
from models import init_db
from actions_db import *




app = Flask(__name__)
app.secret_key = 'lslsdo***'


init_db()



@app.route('/', methods= ['GET', 'POST'])
@app.route('/products', methods= ['GET', 'POST'])
def products():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        price = float(price)
        
        if product_exists(name):
            flash('Такий товар вже є!', category="error")
        else:
            add_product(name, price, category)

        return redirect(url_for('products'))

    all_categories = get_categories()
    choose_category = request.args.get('category', 'all')

    if choose_category == 'all':
        filter_product = get_products()
    else:
        filter_product = get_products_by_category(choose_category)
 


    return render_template('product.html',
                           products= filter_product, 
                           categories= all_categories,
                           choose_category= choose_category
                           )


@app.route('/edit/<name>', methods= ['GET', 'POST'])
def edit(name):
    current_price = str(product_current_price(name))
    current_category = product_current_category(name)

    if request.method == 'POST':
        price = request.form.get('new-price')
        category = request.form.get('new-category')

        edit_product(name, price, category)
        
        flash('Product edited!', category="success")
        return redirect(url_for('products'))


    return render_template('edit.html', 
                           current_price= current_price, 
                           current_category= current_category,
                           title= name
                           )




@app.route('/delete/<name_product>')
def delete(name_product):
    delete_product(name_product)
    flash(f'Product {name_product} was deleted!', category="success")

    return redirect(url_for('products'))


app.run(debug= True)

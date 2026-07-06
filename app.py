from flask import Flask, render_template, request, flash, redirect, url_for
from models import init_db

app = Flask(__name__)
app.secret_key = 'lslsdo***'


init_db()

all_products = {}

@app.route('/', methods= ['GET', 'POST'])
@app.route('/products', methods= ['GET', 'POST'])
def products():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        price = float(price)
        
        if name in all_products:
            flash('Такий товар вже є!')
        else:
            all_products[name] = {'price': price,
                                  'category': category
                                  }
        return redirect(url_for('products'))

    all_categories = sorted({info['category'] for name, info in all_products.items()})
    choose_category = request.args.get('category', 'all')
    if choose_category == 'all':
        filter_product = all_products
    else:
        filter_product = {name: info for name, info in all_products.items() if info['category'] == choose_category}
 


    return render_template('product.html',
                           all_products= filter_product, 
                           categories= all_categories,
                           choose_category= choose_category
                           )


@app.route('/edit/<name>', methods= ['GET', 'POST'])
def edit(name):
    current_price = str(all_products[name]['price'])
    current_category = all_products[name]['category']

    if request.method == 'POST':
        price = request.form.get('new-price')
        category = request.form.get('new-category')
        if price:
            all_products[name]['price'] = float(price)

        if category:    
            all_products[name]['category'] = category
        
        flash('Product edited!')
        return redirect(url_for('products'))


    return render_template('edit.html', 
                           current_price= current_price, 
                           current_category= current_category,
                           title= name
                           )




@app.route('/delete/<name_product>')
def delete(name_product):
    all_products.pop(name_product)
    flash(f'Product {name_product} was deleted!')

    return redirect(url_for('products'))


app.run(debug= True)

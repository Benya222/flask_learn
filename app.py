from flask import Flask, render_template, request, flash, redirect, url_for, session
from models import init_db
from actions_db import *
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__)
app.secret_key = 'lslsdo***'


init_db()


def is_logged():
    return 'company' in session

def current_company():
    return get_company_by_name(session['company'])


@app.route('/', methods= ['GET', 'POST'])
@app.route('/products', methods= ['GET', 'POST'])
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
        
        if product_exists(name):
            flash('Такий товар вже є!', category="error")
        else:
            add_product(name, price, category, company.id)

        return redirect(url_for('products'))

    all_categories = get_categories(company.id)
    choose_category = request.args.get('category', 'all')

    if choose_category == 'all':
        filter_product = get_products(company.id)
    else:
        filter_product = get_products_by_category(choose_category, company.id)
 


    return render_template('product.html',
                           products= filter_product, 
                           categories= all_categories,
                           choose_category= choose_category
                           )


@app.route('/edit/<name>', methods= ['GET', 'POST'])
def edit(name):
    company = current_company()

    current_price = str(product_current_price(name, company.id))
    current_category = product_current_category(name, company.id)

    
    if request.method == 'POST':
        price = request.form.get('new-price')
        category = request.form.get('new-category')

        edit_product(name, price, category, company.id)
        
        flash('Product edited!', category="success")
        return redirect(url_for('products'))


    return render_template('edit.html', 
                           current_price= current_price, 
                           current_category= current_category,
                           title= name
                           )




@app.route('/delete/<name_product>')
def delete(name_product):
    company = current_company()
    delete_product(name_product, company.id)
    flash(f'Product {name_product} was deleted!', category="success")

    return redirect(url_for('products'))



@app.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name_company')
        password = request.form.get('password')
        
        if company_exists(name):
            flash(f'Company {name} already exists!')
            return redirect(url_for('register'))
        else:
            hash_pass = generate_password_hash(password)
            add_company(name, hash_pass)
            flash(f'Company {name} was created!')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name_company')
        password = request.form.get('password')

        if not company_exists(name):
            flash(f'Company {name} not exists!')
            return redirect(url_for('login'))

        company = get_company_by_name(name)
        if not check_password_hash(company.password, password):
            flash('Password incorrect!')
            return redirect(url_for('login'))

        session['company'] = company.name
        flash(f'Welcome {name}!')
        return redirect(url_for('products'))  
      

    return render_template('login.html')


app.run(debug= True)

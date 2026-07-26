from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from actions_db import *
from werkzeug.security import generate_password_hash, check_password_hash



auth_bp = Blueprint('auth', __name__, template_folder='templates')




def valid_register(login, password) -> bool:
    special = ['!', '@', '#', '$', '%', '^', '&', '*', '?', '/', ',', '.', ':', ';', '~']
    if_letter = any(letter.isalpha() for letter in password)
    if_special = any(letter in special for letter in password)
    strong_pass = len(password) >= 6 and if_letter and if_special
    return login and strong_pass


@auth_bp.route('/register', methods= ['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name_company')
        password = request.form.get('password')

        if not valid_register(name, password):
            flash('Weak password or no name!', category= 'error')
            return redirect(url_for('auth.register'))
        
        if company_exists(name):
            flash(f'Company {name} already exists!', category= 'error')
            return redirect(url_for('auth.register'))
        else:
            hash_pass = generate_password_hash(password)
            add_company(name, hash_pass)
            flash(f'Company {name} was created!', category= 'success')
            return redirect(url_for('auth.login'))

    return render_template('auth/register.html')

@auth_bp.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name_company')
        password = request.form.get('password')

        if not company_exists(name):
            flash(f'Company {name} not exists!', category= 'error')
            return redirect(url_for('auth.login'))

        company = get_company_by_name(name)
        if not check_password_hash(company.password, password):
            flash('Password incorrect!', category= 'error')
            return redirect(url_for('auth.login'))

        session['company'] = company.name
        flash(f'Welcome {name}!', category= 'success')
        return redirect(url_for('product.products'))  
      

    return render_template('auth/login.html')


@auth_bp.route('/loguot')
def logout():
    session.pop('company')
    flash('You are logged out!', category= 'success')
    return redirect(url_for('auth.login'))

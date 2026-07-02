from flask import Flask, render_template, request, flash, redirect, url_for


app = Flask(__name__)
app.secret_key = 'lslsdo***'

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

    return render_template('product.html', all_products= all_products)


@app.route('/delete/<name_product>')
def delete(name_product):
    all_products.pop(name_product)
    return redirect('products')


app.run(debug= True)

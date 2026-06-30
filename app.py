from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = "lasldl1*"

def valid_tel(tel): 
    return  tel.isdigit() and len(tel) == 12 and tel.startswith('380')

bid_list = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods= ['GET', 'POST'])
def register():
    name = None
    tel_number = None
    if request.method == 'POST':
        name = request.form.get('name')
        tel_number = request.form.get('phone')

        if valid_tel(tel_number):
            bid_list[name] = tel_number
            flash("Ваша заявка відправлена!")
            return redirect(url_for('index'))
        else:
            flash("Введіть коректний номер телефону!")
            return redirect(url_for('register'))

    return render_template('register.html')


@app.route('/admin', methods = ['GET', 'POST'])
def admin():
    if request.method == 'POST':
        status = request.form.get('status')
        if status:
            bid_list.pop(status)
            flash("Заявка оброблена")
    
    return render_template('admin.html', bid_list= bid_list)


app.run(debug= True)

from flask import Flask, render_template, request


app = Flask(__name__)


def valid_tel(tel):
    pattern = r'^[380]{9}$' 
    return  


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



    return render_template('register.html')


app.run(debug= True)

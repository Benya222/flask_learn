from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)
app.secret_key = '****'

gift_list = []

@app.route('/', methods= ['GET', 'POST'])
@app.route('/index', methods= ['GET', 'POST'])
def index():
    to_get = '*'
    if request.method == 'POST':
        for_add = request.form.get('add_gift')
        if for_add == '':
            flash('Порожній подарунок не можна додати!')
        else:
            gift_list.append(for_add)
            flash('Подарунок додано!')

        return redirect(url_for('index'))        
    
    elif request.method == 'GET':
        search = request.args.get('search_gift')

        if search:
            to_get = search in gift_list


    return render_template('index.html', gift_list= gift_list, to_get= to_get)



app.run(debug= True)

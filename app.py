from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/', methods= ['GET', 'POST'])
@app.route('/index', methods= ['GET', 'POST'])
def index():
    gift_list = []
    to_get = None
    if request.method == 'POST':
        for_add = request.form.get('add_gift')
        if for_add == '':
            ...
        else:
            gift_list.append(for_add)
    elif request.method == 'GET':
        search = request.args.get('search_gift')
        if search in gift_list:
            to_get = 'OK'
        else:
            to_get = 'NOT'


    return render_template('index.html', gift_list= gift_list, to_get= to_get)



app.run(debug= True)

from flask import Flask, render_template, request
from datetime import date


app = Flask(__name__)


@app.route('/', methods= ['GET', 'POST'])
def index():
    age, age_days = None, None

    if request.method == 'POST':
        the_day = request.form.get('age_day')
        the_mounth = request.form.get('age_mounth') 
        the_year = request.form.get('age_year') 

        birthday = date(int(the_year), int(the_mounth), int(the_day))

        today = date.today()
        age = today.year - birthday.year

        if (today.month, today.day) < (birthday.month, birthday.day):
            age -= 1

        age_days = (today - birthday).days


    return render_template('index.html', age = age, age_days = age_days)




app.run(debug= True)

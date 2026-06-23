from flask import Flask, render_template
import datetime


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    now = datetime.datetime.now().time()
    start_time = datetime.time(11, 0)
    end_time = datetime.time(22, 0)
    status = start_time <= now <= end_time
    return render_template('index.html', is_open= status)

@app.route('/menu')
def menu():
    menu = {
        "Капучино": 80,
        "Лате": 85,
        "Еспресо": 60,
        "Чізкейк": 120,
        "Панкейки": 95
    }
    days = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
    now = datetime.datetime.now()
    current_day = days[now.weekday()]
    friday = "Friday"
    return render_template('menu.html', base_menu= menu, the_day= current_day)


app.run(debug= True)

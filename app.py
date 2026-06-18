from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/for_student')
def for_student():
    return render_template('for_student.html', name= "Benya")



app.run(debug= True)

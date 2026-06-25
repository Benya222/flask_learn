from flask import Flask, render_template, request


app = Flask(__name__)



@app.route('/temperature', methods= ['GET', 'POST'])
def temperature():
    user_temp = 0
    to_fahrenheit = 0
    if request.method == 'POST':
        user_temp = request.form.get('temp_converter')
        to_fahrenheit = float(user_temp) * (9 / 5) + 32  

    return render_template('temperature.html', fahrenheit= to_fahrenheit, temperature= user_temp)



app.run(debug= True)

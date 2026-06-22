from flask import Flask, render_template


app = Flask(__name__)


@app.route('/events')
def event():
    events = [
        {"title": "morning meeting", "time": "09:30", "participants": ["Anna", "Oleh"]},
        {"title": "code review", "time": "14:00", "participants": ["Max", "Lera", "Ira"]},
        {"title": "team meeting", "time": "11:00", "participants": ["Sofia", "Danilo"]},
        {"title": "project planning", "time": "16:45", "participants": ["Ivan"]},
    ]
    sort_events = sorted(events, key= lambda item: item["time"])
    return render_template('events.html', our_events = sort_events)



app.run(debug= True)

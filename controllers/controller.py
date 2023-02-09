from flask import render_template, request, redirect
from app import app
from models.event_list import events_list, add_new_event
from models.event import *
from datetime import datetime

@app.route('/events')
def index():
    return render_template('index.html', title='Home', events_list = events_list)

@app.route('/events/new')
def new_event(): 
    return render_template('new.html', title = "New Event")

@app.route('/events', methods=['POST'])
def add_event():
    event_date = request.form['date']
    year, month, day = map(int, event_date.split("-"))
    formatted_date = datetime(year, month, day)

    event_name = request.form['event_name']
    number_of_guests = request.form['number_of_guests']
    room_location = request.form['room_location']
    description = request.form['description']
    new_event = Event(formatted_date, event_name, number_of_guests, room_location, description)
    add_new_event(new_event)
    return redirect("/events")

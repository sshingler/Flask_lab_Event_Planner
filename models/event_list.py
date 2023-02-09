from models.event import *
import datetime



event_1 = Event(datetime.date(2023, 2, 8), "Tech-Meetup-Lochaber", 20, "The Grog & Gruel", "A meet up for tech enthusiasts in Lochaber - Grog & Gruel pub.")
event_2 = Event(datetime.date(2023, 2, 7), "Tech-Meetup-Argyll", 20, "The Oban Inn", "A meet up for tech enthusiasts in Argyll - The Oban Inn.")
events_list = [event_1, event_2]

def add_new_event(event):
    events_list.append(event) 



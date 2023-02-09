class Event():

    def __init__(self, date, name, number_of_guests, room_location, description, recurring):
        self.date = date
        self.name = name
        self.number_of_guests = number_of_guests
        self.room_location = room_location
        self.description = description
        self.recurring = recurring
    
    def __nonzero__(self):
        return self.recurring != 0


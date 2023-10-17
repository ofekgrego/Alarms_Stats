
class Alarm:
    def __init__(self, place, date, time):
        self.place = place
        self.date = date
        self.time = time

    def getPlace(self):
        return self.place
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time
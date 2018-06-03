class PhotoFile(object):
    def __init__(self, filename, date_time, trip_key):
        self.filename = filename
        self.date_time = date_time
        self.trip_key = trip_key

    def get_new_name(self):
        return ""

    def __lt__(self, other):
        return self.date_time < other.date_time

    def __gt__(self, other):
        return self.date_time > other.date_time

    def __str__(self):
        return "Filename: {}, DateTime: {}".format(self.filename, self.date_time)
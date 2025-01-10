import datetime as dt

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def __radd__(self, other):
        return self.__add__(other)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def full_datetime(self):
        now = dt.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')

    def current_time(self):
        now = dt.datetime.now()
        return now.strftime('%.2d:%.2d:%.2d' % (now.hour, now.minute, now.second))

    def date_only(self):
        now = dt.datetime.now()
        return now.strftime('%Y-%m-%d')

    def time_only(self):
        return self.__str__()
    
    def date_diff(self, date1, date2):
        date1 = dt.datetime.strptime(date1, '%Y-%m-%d')
        date2 = dt.datetime.strptime(date2, '%Y-%m-%d')
        return (date2 - date1).days

# Helper function to convert seconds to Time object
def int_to_time(seconds):
    minutes, second = divmod(seconds, 60)
    hour, minute = divmod(minutes, 60)
    return Time(hour, minute, second)
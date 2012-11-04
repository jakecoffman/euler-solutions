import datetime
sundays = 0

for year in xrange(1901,2001):
    for monday in xrange(1,13):
        # Creates a datetime for each 1st of the month, checks for sundayness
        if datetime.datetime(year, monday, 1).weekday() == 6:
            sundays += 1
print sundays


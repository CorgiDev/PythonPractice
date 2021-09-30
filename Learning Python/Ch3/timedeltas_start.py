#
# Example file for working with timedelta objects
#

from datetime import date
from datetime import time
from datetime import datetime as dt
from datetime import timedelta as td


# construct a basic timedelta and print it
print(td(days=365, hours=5, minutes=1))

# print today's date
now = dt.now()
print("Today is:" + str(now))

# print today's date one year from now
print("One year from now it will be " + str(now + td(days=365)))

# create a timedelta that uses more than one argument
print("In 2 days and 3 weeks, it will be " + str(now+td(days=2, weeks=3)))

# calculate the date 1 week ago, formatted as a string
t=dt.now() - td(weeks=1)
s=t.strftime("%A %B %d, %Y")
print("One week ago it was " + s)


### How many days until April Fools' Day?
today = date.today()
afd = date(today.year, 4, 1)

# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April Fool's day has already occurred %d days ago" % ((today-afd).days))
    afd = afd.replace(year = today.year+1)
    print("The next April Fools day is on ", str(afd))
elif afd > today:
    print("April Fool's day will occur in %d days" % ((afd-today).days))
elif afd == today:
    print("Today is April Fool's Day!")

# Now calculate the amount of time until April Fool's Day
time_to_afd = afd-today 
print("It's just ", time_to_afd.days, "days until April Fool's Day.")

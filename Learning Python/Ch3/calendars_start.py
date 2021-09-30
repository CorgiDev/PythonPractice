#
# Example file for working with Calendars
#

# import the calendar module
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
st=c.formatmonth(2021, 1, 0, 0)
print (st)

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
st = hc.formatmonth(2021, 1)
print (st)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2021, 8):
    print (i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
    print (name)

for day in calendar.day_name:
    print (day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:

print("Team meetings will be on the first Friday of each month: ")
for m in range (1,13): #13 is non-inclusive. It just ensures you get all 12 months.
    cal = calendar.monthcalendar(2021,m)
    # Week 1 and 2 helps you get the first 2 weeks of the specified month
    weekone=cal[0]
    weektwo=cal[1]

    # From there we determine which week has the first Friday.
    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))

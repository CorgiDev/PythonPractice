#
# Example file for working with date information
#
from datetime import date as d
from datetime import time
from datetime import datetime as dt

def WeekdayName(arg):
        switcher = {
            0: "Monday",
            1: "Tuesday",
            2: "Wednesday",
            3: "Thursday",
            4: "Friday",
            5: "Saturday",
            6: "Sunday",
        }
        return switcher.get(arg, "nothing")

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  today = d.today()
  print("Todays date is", today)

  # print out the date's individual components
  print("Date components:", today.month, "/", today.day, "/", today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("Today's weekday number is:", today.weekday())
  days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  print ("Which is a:", days[today.weekday()])

  print("Which is short for", WeekdayName(today.weekday()))
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today2 = dt.now()
  print ("The current date and time is: ", today2)
  
  # Get the current time
  t = dt.time(dt.now())
  print (t)


if __name__ == "__main__":
  main();
  
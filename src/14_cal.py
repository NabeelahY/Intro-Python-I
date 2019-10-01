"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

x = f'14_cal.py {datetime.now().strftime("%m")} [{datetime.now().strftime("%Y")}]'


def cal():
    print('============================================')
    print('Please input your preferred month and year')
    month = input('Enter month: ')
    year = input('Enter year: ')
    if len(month) == 0 or len(year) == 0:
        print('Printing current month calender')
        print(
            f'{calendar.month(int(datetime.now().strftime("%Y")), int(datetime.now().strftime("%m")), 2, 1)}'
        )
        return x
    else:
        print(calendar.month(int(year), int(month), 2, 1))
        return f'14_cal.py {month} [{year}]'


print(cal())

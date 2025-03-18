#1
'''
import math
print(math.floor(-2.8))
print(abs(round(-4.3)))
print(math.ceil(math.sin(34.5)))
'''

#2
'''
import calendar

print(calendar.isleap(2025)) #help(calendar.isleap)
#print(dir(calendar))
print(calendar.leapdays(2000, 2050))
print(calendar.weekday(2016, 7, 29))
'''

#3
def average(num1, num2):
    '''(number, number) -> number
    Return the average of num1 and num2.
        average(10,20)
    15.0
        average(2.5,3.0)
    2.75
    '''
    return (num1+num2) / 2


import doctest
doctest.testmod("exercise.py")
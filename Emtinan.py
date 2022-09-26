# Task 1
# Given a list of names, create a running Python project that sorts it alphabetically,
# Python has this functionality built-in, but see if you can do it without using sort()!
unsort_list = ['d','b','a','c','f','h','g','e']
sort_list = []

while unsort_list:
    smallest = min(unsort_list)
    sort_list.append(smallest)
    unsort_list.pop(unsort_list.index(smallest))

print (sort_list)


#Task 2
# Create a running Python project that can take two dates as input, and then
# calculate the amount of time between them.
from datetime import datetime
from dateutil import relativedelta

d1 = input('ENTER DATE 1 ')
d2 = input('ENTER DATE 2 ')

date1 = datetime.strptime(d1, "%d/%m/%Y")
date2 = datetime.strptime(d2, "%d/%m/%Y")

delta = relativedelta.relativedelta(date2, date1)
print(delta.years, 'Years,', delta.months, 'Months,', delta.days, 'Days')


#Task 3 
# Create a running Python project to check if all digits of a number divide it; given a
# number n, find whether all digits of n divide it or not.

def checkDivisibility(n, digit) :
	
	return (digit != 0 and n % digit == 0)
	
def allDigitsDivide( n) :
	
	temp = n
	while (temp > 0) :
		
		digit = temp % 10
		if ((checkDivisibility(n, digit)) == False) :
			return False

		temp = temp // 10
	
	return True

n = int(input('Please Enter a number: '))

if (allDigitsDivide(n)) :
	print("Yes")
else :
	print("No" )
	



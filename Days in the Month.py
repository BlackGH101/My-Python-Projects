days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		return True

def num_of_days(month, year):
	if not 1<= month <= 12:
		return('Invalid Month')

	if is_leap(year) and month == 2:
		return 29

	return days[month]



print(num_of_days(2, 2016))
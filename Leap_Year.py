days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	return year % 4 == 0 and (year % 400 != 0 or year %  100 == 0)

def days_in_month(month, year):
	if not 1<= month <= 12:
		return 'Invalid Month'

	if month == 2 and is_leap(year):
		return 29

	return days[month]


print(days_in_month(12, 2016))
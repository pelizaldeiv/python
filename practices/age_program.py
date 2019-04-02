#!/bin/python
def age_program():
	seconds_or_years = input("Give me seconds (s) or years (y)? ")
	if seconds_or_years == "s":
		#convert seconds to years
		user_value = input("How many seconds have you lived for? ")
		print("You've lived for {} years.".format(int(user_value)/60/60/24/365))
	elif seconds_or_years == "y":
		#convert years to seconds
		user_value = input("How many years have you lived for? ")
		print("You've lived for {} seconds.".format(int(user_value)*365*24*60*60))
	else:
		print("idiot")
age_program()

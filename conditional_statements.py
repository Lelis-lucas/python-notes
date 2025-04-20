#!/bin/python3
def drink(money): 
	if money >= 2:
		return "You've got yourself a drink!"
	else:
		return "No drink for you"
		
print(drink(5))
print(drink(1))

######-----######

def alcohol(age, money):
	if (age >= 21) and (money >= 5):
		return "We're getting a drink!"
	elif (age >= 21) and (money < 5):
		return "Come back with ore money!"
	elif (age < 21) and (money >= 5):
		return "Nice try, kid"
	else:
		return "You're too poor and too young"

print(alcohol(21, 7))
print(alcohol(20, 7))
print(alcohol(10, 3))
 

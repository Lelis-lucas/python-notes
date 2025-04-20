#!/bin/python3
#Functions:
def who_am_i(): #This is a function
	name = "Heath"
	age = 30
	print("My name is " + name + " and I am " + str(age) + " years old.")
who_am_i()

#Adding parameters:
def add_one_hundred(num):
	print(num + 100)

add_one_hundred(100)

#Multiple parameters:
def add(x, y):
	print(x + y)

add(7,7)

###----###

def multiply(x,y):
	return(x * y)
	
print(multiply(7, 7))

###---###
def new_line():
	print('\n')
new_line()
	

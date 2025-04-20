#!/bin/python3
#List it is a data structure

#Lists - Have brackets --> []

movies = ['Carros', 'The Hangover', 'The exorcist']

#list = [index0, index1, index2]
print(movies[0])
print(movies[1:3])
print(movies[1:])
print(movies[:2])
print(movies[-1]) #Last item of the list
print(len(movies))
movies.append("JAWS") #ADD END
movies.pop() #REMOVE LAST ITEM
movies.pop(0) #REMOVE FIRST ITEM


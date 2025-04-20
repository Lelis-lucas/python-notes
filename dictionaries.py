#!/bin/python3

#key : value pairs {}

#Dictionaries
drink = {'white russian':7,
'old fashion':10,
'lemon drop':8}
#Drink is key, price is value

employees = {"Finance":["Bob", "Linda", "Tina"], "IT":["Gene", "Louise", "Teddy"], "HR":["JimmyJR", "Mort"]}

employees['legal']:["Mr.Frond"] #ADD NEW KEY:VALUE PAIR
employees.update({"Sales":["Andie"]}) #ADD NEW KEY:VALUE PAIR

drink['white russian'] = 8
print(drink.get('white russian'))

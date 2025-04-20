#!/bin/python3

my_name = "Lucas Dias Lelis"
print(my_name[0])
print(my_name[-1])

sentence = 'This is a sentence'
print(sentence[:4])
print(sentence.split())
#

sentence_split = sentence.split()
sentence_join = join(sentence_split)
print(sentence_join)

quote = 'He said, \'Give me all your money\''
print(quote)

too_much_space = '       HELLO         '
print(too_much_space.strip())

letter = 'A'
word = 'Apple'
print(letter.lower() in word.lower())

movie = "THE MATRIX"
print("My favorite movie is {}".format(movie))


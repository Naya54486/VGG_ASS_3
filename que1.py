# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def up_low(string):
    upper_letter = 0
    lower_letter = 0
    for letter in string:
        if letter.isupper():
            upper_letter += 1
        elif letter.islower():
            lower_letter += 1
    print(upper_letter, lower_letter)

up_low('The quick Brow Fox')
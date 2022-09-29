
# how to use iput
name = input('What is your name? ')
print('Hi ' + name)

# Qn.  person's name and favourite color.
# Then print a message like "Moses likes blue"

# Solution

name = input("What's your name? ")
color = input("What is your favourite color? ")
print(name + ' likes ' + color)


# TYPE CONVERSION
# example
birth_year = int(input('Birth year: '))
age = 2022 - birth_year
print(age)

# Qn. ask a user their weight(in pounds), convert it to kilograms
# and print on the terminal

# Solution

weight_lbs = input('wight (lbs): ')
weight_kg = int(weight_lbs) * 0.45
print(weight_kg)

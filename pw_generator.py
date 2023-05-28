import random
import string

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

characters = []
characters.extend(random.sample(string.ascii_letters, nr_letters))
characters.extend(random.sample(string.digits, nr_numbers))
characters.extend(random.sample(string.punctuation, nr_symbols))

random.shuffle(characters)

password = ''.join(characters)
print(f"Your password is: {password}")

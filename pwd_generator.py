import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# get a list of letters
for char in range(0, nr_letters):
  password.append(random.choice(letters))

# get a list of symbols
for char in range(0, nr_symbols):
  password.append(random.choice(symbols))

# get a list of numbers
for char in range(0, nr_numbers):
  password.append(random.choice(numbers))

# randomize the list
random.shuffle(password)

#convert the list to  a string and print it
pass_string =""
for item in password:
    pass_string += item
# pass_string = [str(element) for element in password]
print(f"Your password is: {pass_string}")



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
passw = ""
'''for _ in range(nr_letters):
  letter = random.choice(letters)
  passw = passw + letter
for _ in range(nr_symbols):
  symbol = random.choice(symbols)
  passw = passw + symbol
for _ in range(nr_numbers):
  nr = random.choice(numbers)
  passw = passw + nr
print(f"PyPassword Generator: {passw}")'''
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
passw = ""
new_list = []
for _ in range(nr_letters):
  new_list.append(random.choice(letters))
for _ in range(nr_symbols):
  new_list.append(random.choice(symbols))
for _ in range(nr_numbers):
  new_list.append(random.choice(numbers))
  
random.shuffle(new_list)
print(new_list)
for el in new_list:
  passw = passw + el
print(passw)
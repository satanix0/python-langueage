# Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nl = int(input("How many letters would you like in your password?\n"))
ns = int(input(f"How many symbols would you like?\n"))
nn = int(input(f"How many numbers would you like?\n"))
# In simple order
easy_pass = ""
for i in range(1, nl+1):
    easy_pass += random.choice(letters)

for i in range(1, ns+1):
    easy_pass += random.choice(symbols)

for i in range(1, nn+1):
    easy_pass += random.choice(numbers)

print(f"You can use easy passwoed : {(easy_pass)}")

# In random Order
pass_list = []
for i in range(1, nl+1):
    pass_list += random.choice(letters)

for i in range(1, ns+1):
    pass_list += random.choice(symbols)

for i in range(1, nn+1):
    pass_list += random.choice(numbers)

random.shuffle(pass_list)
hard_pass = ""
for i in range(len(pass_list)-1):
    hard_pass += pass_list[i]
print(f"You can use hard passwoed :  {(hard_pass)}")

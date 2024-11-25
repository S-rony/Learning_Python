# Class_List = ['Noah','Simone','Ji Ho','Thanh','Nathanial','Soo','Mickel','Tuan','Thuy Linh']
#
# random.shuffle(Class_List)
#
# print (Class_List[0:3])

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Easy Level letter+symbol+number
random.shuffle(letters)
random.shuffle(symbols)
random.shuffle(numbers)
l=[]
for letter in letters[0:nr_letters]:
    l.append(letter)
for symbol in symbols[0:nr_symbols]:
    l.append(symbol)
for number in numbers[0:nr_numbers]:
    l.append(number)
st = ""
random.shuffle(l)
for i in l:
    st = st+i
print("Here is your password:",st)

#for shuffle the l use random.shuffle(l)


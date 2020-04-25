age = int(input("How old are you mate? "))
if age >= 18:
    print(f"You are {age}, so go out and chill as much as you want")
else:
    print(f"You are {18-age} year(s) old from chilling, so wait a bit")


while age <= 20:
    print("Keep printing this")
    age += 1

while age != 100:
    age = int(input("How old are you mate? "))
    if age >= 18:
        print(f"You are {age}, so go out and chill as much as you want")
    else:
        print(f"You are {18-age} year(s) old from chilling, so wait a bit")

topping = input("Enter Pizza Topping: ")
while topping != 'quit':
    print(f"{topping.title()} added successfully")
    topping = input("Enter Pizza Topping: ")


restaurant_open = True
while restaurant_open:
    topping = input("Enter Pizza Topping: ")
    if(topping == 'quit'):
        restaurant_open = False
        #break
    else:
        print(f"{topping.title()} added successfully")


family = ['sheriffo', 'lisa', 'maryam', 'fatou', 'oumie', 'neer', 'neer']
while family:
    print(family.pop().title())#pop will remove and return


family = ['sheriffo', 'lisa', 'maryam', 'fatou', 'oumie', 'neer', 'neer']
print(family)
while 'neer' in family:
    family.remove('neer')#remove will only remove
print(family)
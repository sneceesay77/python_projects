import simple_module as sm
from simple_module import club_entry as ce
ce(20)

my_tuple = tuple(range(1, 21))
for val in my_tuple:
    if val == 5 or val == 15:
        print("This is number 10")
        break
    else:
        print("Not yet 10")


squares_lc = [value **2 for value in range(1, 11)]

print(4 in squares_lc)
print(4 not in squares_lc)

age = 24
if age <= 10:
    print("You are a kiddo")
elif age <= 15:
    print("You are and adolescent")
else:
    print("Dude go and chill, you are a star")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')


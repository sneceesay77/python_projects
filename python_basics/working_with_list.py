for value in range(1, 100):
    print(value)

for value in range(10):
    print(value)

numbers = list(range(1, 10))
print(numbers)

even_numbers = list(range(2, 20, 2))
print(even_numbers)

squares = []
for v in range(1, 11):
    square = v ** 2
    squares.append(square)
print(squares)

print(f"{min(squares)} {max(squares)} {sum(squares)}")

#List comphrension
squares_lc = [value **2 for value in range(1, 11)]
print(squares_lc)

#TIY
big_list = []
for value in range(1, 1_000_001):
    big_list.append(value)
#print(big_list)
print(f"{min(big_list)} {max(big_list)} {sum(big_list)}")

odd_list = list(range(1,21,2))
print(odd_list)

mul_three = list(range(3, 31, 3))
for value in mul_three:
    print(value)

cube_list = []
for value in range(1,11):
    cube_list.append(value**3)
print(cube_list)

#List comphrension
cube_list_lc = [value**3 for value in range(1,11)]

print(cube_list_lc)
print(cube_list[0:3])
print(cube_list[:5])
#output last n
print(cube_list[-4:])
print(cube_list[4:])
print(cube_list[1:4])
print(cube_list[1:4:2])

#copies and maintain separate copies
cube_list_copy = cube_list[:]
print(cube_list_copy)

#copies are not separate
cube_list_copy = cube_list
print(cube_list_copy)

#An immutable list is called a Tuple in python. 
#Use parenthesis instead of 
my_t = (4,6,3,5,4)
print(my_t)
mytuple = (tuple(range(1, 20)))
print(mytuple)
print(mytuple[0:4])


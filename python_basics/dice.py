from random import randint
from random import choice

class Dice:
    def __init__(self, side=6):
        self.side = side
    
    def roll_dice(self):
        return randint(1, self.side)

dice = Dice()
for i in range(1,11):
    print(dice.roll_dice())


dice = Dice(10)
for i in range(1,11):
    print(dice.roll_dice())

dice = Dice(20)
for i in range(1,11):
    print(dice.roll_dice())

num = tuple(range(1,10))
letters = ('a', 'e', 'b', 'c', 'f', 'd')

lottery_code = num + letters

my_ticket = ['a', 'b', 'c', 'd']


winning_str = ""
my_ticket_str = ""

for i in range(0, 4):
    my_ticket_str += str(my_ticket[i])

count = 0
while my_ticket_str != winning_str:
    winning_code = []
    winning_str = ""
    for i in range(0,4):
        code = choice(lottery_code)
        winning_code.append(choice(lottery_code))
        winning_str += str(winning_code[i])
    print(f"{winning_str} {my_ticket_str}")
    count += 1
print("--Winning code--")
print(f"Winning number : {winning_str} found after {count} iteration")

# from random import randint
# from random import choice

# class Dice:
#     def __init__(self, side=6):
#         self.side = side
    
#     def roll_dice(self):
#         return randint(1, self.side)

# dice = Dice()
# for i in range(1,11):
#     print(dice.roll_dice())


# dice = Dice(10)
# for i in range(1,11):
#     print(dice.roll_dice())

# dice = Dice(20)
# for i in range(1,11):
#     print(dice.roll_dice())

# num = tuple(range(1,10))
# letters = ('a', 'b', 'c', 'd', 'e', 'f')

# lottery_code = num + letters

# my_ticket = ['a', 'b', 'c', 'd']


# winning_str = ""
# my_ticket_str = ""

# for i in range(0, 4):
#     my_ticket_str += str(my_ticket[i])

# while my_ticket_str != winning_str:
#     winning_code = []
#     winning_str = ""
#     for i in range(0,4):
#         code = choice(lottery_code)
#         winning_code.append(choice(lottery_code))
#         winning_str += str(winning_code[i])
#     print(f"{winning_str} {my_ticket_str}")
# print("--Winning code--")
# print(winning_str)


def club_entry(age):
    if(age >= 18):
        print("You can enter club")
    else:
        print("Go and study")

age = int(input("Enter you age"))
club_entry(age)

"""this is really not the case"""

#In python there are several ways of dealing with arguments. 
#Positional arguments, the parameters a, b in fun(a, b) should be accessed in order when the arguments are supplied. 
#Keyword arguments fun(a, b) == fun(b="abc", a="bbb")
#Default values

#Arbitrary number of arguments, you can have fix parameters as well.
def family(*members):
    print("\n Senior first generation member of this family are:")
    for member in members:
        print(f" - {member}")

family("Sheriffo", "Malick", "Balla", "Nyambi")

#Arbitrary keyword arguments, this world return a dictionary named family_info
#def family(name, village, **family_info):
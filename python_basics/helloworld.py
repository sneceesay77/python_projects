message = "Hello, World is not that nice"
print(message.upper())
print(message.lower())
print(message.title())

first_name = "Sheriffo"
second_name = "Ceesay"
full_name = f"{first_name} {second_name}"
print(full_name)
print("\tPython")

favourite_language = ' Java '
print(favourite_language)
print(favourite_language.rstrip())#you can use strip, lstrip or rstrip

sentence = "this is the first sentence I have written in this very brilliant python session. I'm loving it\n"
sentence_2 = 'this is the first sentence I have written in this very brilliant python session. I\'m loving it'

print(f"{sentence} {sentence_2}")

name = "Sheriffo"
full_message = "Hello "+name+", would you like to to learn some Python today?"

print(full_message)
print(f"Hello {name}, would you like to to learn some Python today?")

quote = "Shoot for the moon even if you miss you will land amongst the start"
author = "Nyambi Ceesay"
print(f'{author} once said, "{quote}"')

print(10+90)
print(10*90)
print(90/10)
print(10-90)
print(9^10)

age, salary, address = 34, 40_000, 8
MAX_BUS_PASSENGER = 30
print(MAX_BUS_PASSENGER)
print(f"{age} {salary} {address}")

#List definition, this is similar to arrays in Java
family = ['Maryam', 'Fatou', 'Oumie', 'Lisa', 'Sheriffo']
family.append('Nanding')
print(family)

print(family[1].upper())
print(family[-1])

#deletes a value from list
del family[4]

print(family)

#pop deletes but you can use the value. 
maryam = family.pop(0)
print(maryam)

party_guest = ['Ramadan', 'Khawar', 'Dawand', 'Sheriffo']
print(f"{party_guest[0]} is from Nigeria")
print(f"{party_guest[1]} is from Pakistan")
print(f"{party_guest[2]} is from Kurdistan")
print(f"{party_guest[-1]} is from The Gambia")

print(f"{party_guest[2]} cannot make it the Party!")
party_guest[2] = "Alfusainey"
print(party_guest)
party_guest.insert(0, "Lisa")
party_guest.insert(3, "Caroline")
print(party_guest)
party_guest.sort()
print(party_guest)
party_guest.sort(reverse=True)
print(party_guest)
##sorted maintain the original state of the list
print(sorted(party_guest))

for guest in party_guest:
    print(guest)
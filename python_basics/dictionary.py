dict = {}
dict['president'] = 'Sheriffo'
dict['vp'] = 'Alfusainey'
dict['sg'] = 'Fatou'

print(dict)

dict['vp'] = 'Alfu'

vp = dict.get('vp')
print(vp)

print(dict)

for key, val in dict.items():
    print(f"Key: {key.title()} => Value: {val}")

favourite_food ={'sc': 'Chicken Yassa', 'lg':'Domoda', 'mc': 'Mashmello'}

for key in sorted(favourite_food.keys()):
    print(f"{key.upper()}'s favourite food is {favourite_food[key]}")

cities = []
for n in range(30):
    city = {'name':"Dundee", 'rank': n}
    cities.append(city)

for city in cities:
    print(city)

favorite_languages = {
'jen': ['python', 'ruby'],
'sarah': ['c'],
'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'],
}

for person,fl in favorite_languages.items():
    print(f"{person.title()}'s favourite language(s) : {fl}")
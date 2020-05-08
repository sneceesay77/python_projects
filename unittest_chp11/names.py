from name_function import get_formatted_name


print("Enter 'q' to quit")

while True:
    first = input("Enter First Name: ")
    if first == 'q':
        break
    last = input("Enter Last Name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formated name: {formatted_name}")

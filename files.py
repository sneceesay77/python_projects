#print whole content
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents)

#line by line access
with open("pi_digits.txt") as file_object:
    print("===========================================")
    for line in file_object:
        #print(len(line)) 
        print(line.rstrip())

#read lines into list
with open("pi_digits.txt") as file_object:
    print("===========================================")
    lines = file_object.readlines()
    print(lines[1])
    for line in lines:
        print(line.rstrip())


with open("pi_million_digits.txt") as file_object:
    print("===========================================")
    lines = file_object.readlines()
    pi_string = ""
    for line in lines:
        pi_string += line.strip()
    print(f"{pi_string[:52]}...")
    print(len(pi_string))
    
    birthday = input("Enter your birthday in mmddyy: ")
    if birthday in pi_string:
        print("Your birthday is in the string")
    else:
        print("Your birthday is not in the string")

with open("what_i_learned.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(f"In Python you can {line}")

with open("what_i_learned.txt") as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(f"In Python you can {line}".replace("Python", "C"))

with open("what_i_learned_out.txt", 'a') as file_out:
    with open("what_i_learned.txt") as file_object:
        lines = file_object.readlines()
        for line in lines:
            line = f"In Python you can {line}".replace("Python", "C")
            file_out.write(line)


response = input("Which programming language is your favorite language?")
with open("poll_results.txt", 'w') as poll_out:
    while response != 'quit':
        poll_out.write(response+"\n")
        response = input("Which programming language is your favorite language?")
    print("End of survey")



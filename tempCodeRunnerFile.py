response = input("Which programming language is your favorite language?")
with open("poll_results.txt", 'w') as poll_out:
    while response != 'quit':
        poll_out.write(response+"\n")
        response = input("Which programming language is your favorite language?")
    print("End of survey")
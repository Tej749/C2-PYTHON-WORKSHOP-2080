# guess game
'''
while loop:
initialization
condition check
    block of code
    increment / decrement

'''

secret_number = 45
guess_count = 0     # initialization
guess_limit = 3     # condition checking value

while guess_count < guess_limit:
    guess = int(input("Enter Guess Number : "))
    guess_count += 1

    if guess == secret_number:
        print("Hurray..!! You won the game...")
        break
else:
    print("Sorry..!! .. Try Again...")


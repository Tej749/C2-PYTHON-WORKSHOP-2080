# Guess Game
secret_key = 50
guess_count = 0         # initialization
guess_limit = 3         # condition check number

while guess_count < guess_limit:
    guess = int(input("Enter your guess number : "))
    guess_count = guess_count + 1

    if guess == secret_key:
        print("Hurray...!! you won the game....!!")
        break

else:
    print("sorry...!!! Try Again....")

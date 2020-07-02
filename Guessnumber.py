actual_number = 30
attempts  = 0
while True:
    attempts += 1
    guessing_number = int(input("Guess the number :\n"))
    if guessing_number < actual_number:
        print("your guess was too low 😌")
    elif guessing_number > actual_number:
        print("your number was too high 😌")
    else:
        print(f"You guessed the number in  your {attempts} attempt 😊")
        break
print("Thanks for playing 😀")


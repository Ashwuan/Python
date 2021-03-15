number_guess = "0"
secret_number = "5"

while True:
    number_guess = input("Guess the number 1 to 5: ")
    if number_guess > secret_number :
        print("Your guess is greater than the Secret number!!!\n")
    if number_guess < secret_number :
        print("Your guess is less than the Secret number!!!\n")
    if number_guess == secret_number:
        print("You guessed", secret_number, "Which is the secret number!!!\n")
        break
    else:
        print(number_guess,"is incorrect\n")

guess = ''
secret_word ="Python"
guess_limit = 3
guess_count = 0
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if (guess_count < guess_limit):
     guess = input("Guess the Word: ")
     guess_count += 1

    else:
        out_of_guesses = True

if out_of_guesses:
    print("You're Out of Guesses, the secret word was Pyhton, YOU LOSE!!!!!!")   
else: 
    print("You Guessed Correctly,HOORAY!!!")
    
    
    
    


#Basic Structure
import random
from wordlist import word_list

#The input type allowed 
def get_word():
    word = random.choice(word_list)
    return word.upper()

#function to the user to play the game
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    #input displayed
    print("Let's play Hangman Game!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries >0:
        guess = input("Please Guess a letter or word: ").upper()
        
        #if statment condtion
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
                
            else:
                print("Good Job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
                    
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
                
            else:
                guessed = True
                word_completion = word
            
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    #result condation statment
    if guessed:
        print("congratulations, you guessed the word !!")
    else:
        print("Sorry you have run out of tries. The word was "+ word + ". Maybe try next time")
         
#display the game    
def display_hangman(tries):
     stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
     return stages[tries]
 
 #loop the game again !!
def main():
     word = get_word()
     play(word)
     #whileloop select the user to play the game again
     while input("Play Again? (YES/NO) ").upper() == "YES":
         word = get_word()
         play(word)
 
#function return the user to the beginning of the game to play agian !         
if __name__ == "__main__":
    main()
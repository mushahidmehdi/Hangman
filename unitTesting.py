from ps3_hangman import *

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    word = ''
    for i in secretWord:
        if i in lettersGuessed:
          word += i
        else:
          word +=  '_ '
    return word
        
# print(getGuessedWord('mushahid', 'musho'))

          
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    words = ''
    for i in 'abcdefghijkmnopqrstuvwxyz':
      if not i in lettersGuessed:
        words += i
    return words
    

# print(getAvailableLetters('abcdfgh'))

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
      if not i in lettersGuessed:
        return False
    return True


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    secretWord = secretWord.lower()
    attempt = 8
    lettersGuessed = ''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')

    while attempt > 0:
      print('-----------------------------')
      print('You have ' + str(attempt) + ' guesses left.')
      print("Available letters: " + str(getAvailableLetters(lettersGuessed)))
      guess = input("Please guess a letter: ")
      
      if not guess in secretWord and not guess in lettersGuessed:
        lettersGuessed += guess
        print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
        attempt -= 1
        getAvailableLetters(guess)
        
      elif guess in secretWord and not guess in lettersGuessed:
        lettersGuessed += guess
        print("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
      else:
        guess in secretWord and guess in lettersGuessed
        print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
      if isWordGuessed(secretWord, lettersGuessed):
        break
    
    if attempt == 0 and not isWordGuessed(secretWord, lettersGuessed):
      print("--------------------------")
      print("Sorry, you ran out of guesses. The word was " + str(secretWord))
    else:
      print("--------------------------")
      print("Congratulations, you won!")

        
print(hangman('mushahid'))
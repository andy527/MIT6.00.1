__author__ = 'kuanweichen'



def hangman(secretWord):





'''    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is"+str(len(secretWord))+"letters long."
    for i in range(8):
        print "-"*30
        print "You have "+str(i)+ "guesses left."
        print "Available letters:"+ str(getAvailableLetters(lettersGuessed))
        char=str(input("Please guess a letter:"))
        if char in secretWord:
            print 'Good Guess:'+ str(getGuessedWord(secretWord, lettersGuessed))
        elif char in secretWord and isWordGuessed(secretWord, lettersGuessed):
            print "Oops! You've already guessed that letter:"+str(getGuessedWord(secretWord, lettersGuessed))
        else:
            print "Oops! That letter is not in my word:"+str(getGuessedWord(secretWord, lettersGuessed))

        if isWordGuessed(secretWord, lettersGuessed):
            print '-'*30
            print "Congratulations, you won!"
    print '-'*30
    print 'Sorry, you ran out of guesses. The word was else. '




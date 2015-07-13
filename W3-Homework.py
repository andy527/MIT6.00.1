__author__ = 'kuanweichen'
#Q1
def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start,stop,step):
    sum=0
    start0=start
    while start<stop:
        sum+=step*f(start)
        start+=step
    return sum


print radiationExposure(5, 11, 1)
#----------------------------------------------------
#Q2
# 6.00 Problem Set 3
#
# Hangman game
#

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    i=0
    while i <len(secretWord):
        if secretWord[i] in lettersGuessed:
            i+=1
        else:
            return False
            break
    return True





def getGuessedWord(secretWord, lettersGuessed):
    letter=''
    for e in secretWord:
        if e in lettersGuessed:
            letter+=str(e)+' '
        else:
            letter+=str(' _ ')

    return letter




def getAvailableLetters(lettersGuessed):
    import string
    all_letter=string.ascii_lowercase
    for char in lettersGuessed: all_letter=all_letter.replace(char,"")
    return all_letter


def hangman(secretWord):
    lettersGuessed=''
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is "+str(len(secretWord))+" letters long."
    i=0
    while i<8:
        print "-"*30
        print "You have "+str(8-i)+ " guesses left."
        print "Available letters:"+ str(getAvailableLetters(lettersGuessed))
        letters=raw_input("Please guess a letter:")
        if letters in lettersGuessed and len(lettersGuessed)>=1:
            print "Oops! You've already guessed that letter:"+str(getGuessedWord(secretWord, lettersGuessed))
            print "The letter you have used: "+str(lettersGuessed)
        elif str(letters) in secretWord:
            lettersGuessed+=letters
            print 'Good Guess:'+ str(getGuessedWord(secretWord, lettersGuessed))
            print "The letter you have used: "+str(lettersGuessed)
        else:
            print "Oops! That letter is not in my word:"+str(getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed+=letters
            print "The letter you have used: "+str(lettersGuessed)
            i+=1
        if isWordGuessed(secretWord, lettersGuessed):
            print '-'*30
            print "Congratulations, you won!"
    print '-'*30
    print 'Sorry, you ran out of guesses. The word was: '+str(secretWord)



secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
__author__ = 'kuanweichen'
#Honoi Towers
def printmove(fr,to):
    print 'From: ' +str(fr)+ ","+ "To: " +str(to)

def move(n,fr,to,spare):
    if n==1:
        printmove(fr,to)
    else:
        move(n-1,fr,spare,to)
        move(1,fr,to,spare)
        move(n-1,spare,to,fr)

#Palindrome
def isPalindrome(s):
    def toChar(s):
        s=s.lower()
        re=""
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                re=re+c
        return re

    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
    return isPal(toChar(s))




def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    #base cases
    if aStr == '':
        return False
    elif len(aStr) == 1:
        if char==aStr:
            return True
        else:
            False
    elif char == aStr[int(round((len(aStr))/2.0))]:
        return True

    #general case
    else:
        high = len(aStr)
        low = 0
        mid = int((high + low) / 2)
        if (char < aStr[mid]):
            aStr = aStr[low:mid]

        else:
            aStr = aStr[mid:high]

        return isIn(char,aStr)
print isIn('a','cdijk' )
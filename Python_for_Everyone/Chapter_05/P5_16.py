#P5.16 Write a recursive function
#def isPalindrome(string)
#that returns True if string is a palindrome, that is, a word that is the same when
#reversed. Examples of palindromes
#are “deed”, “rotor”, or “aibohphobia”. Hint: A
#word is a palindrome if the first and last letters match and the remainder is also a
#palindrome.



# Solution_1 Code : Without recursion ------------------------------------------------
#Used regular expressions to remove all non alphabets and convert characters to lower case
#Used for loop to create string variable that has the characters of original string in reverse order
#Compared the original and reverse string

import re
def ispalindrome(string):
    str_1 = ("").join([i.lower() for i in str(string) if re.search(r"[a-zA-Z]",i)])
    cont = []
    for i in range(len(str_1)):
        cont.insert(0,str_1[i])
    str_2 = ("").join(cont)
    print(str_1==str_2)
    
# Solution_2 Code : With recursion ------------------------------------------------
#Used regular expressions to remove all non alphabets and convert characters to lower case
#Use recursion. At each step, the first character is compared with last character
#Only if the characters  match, we call the function recursively.The argument passed is a string 
#stripped off of the first and last characters

#The very first instance when the first and last characters do not match, false is returned  
#The exit condition is therefore:
# >> either the characters do not match
# >> or recursion continues successfully till we have 0 or only one character left

import re
def is_palindrome(string):
    str_1 = ("").join([i.lower() for i in str(string) if re.search(r"[a-zA-Z]",i)])
    if len(str_1) > 1:
        if str_1[0] == str_1[-1]:
            return ispalindrome(str_1[1:-1])
        else: 
            return False
    else :
        return True

# Solution_3 Code : With recursion ------------------------------------------------
11.2 Problem Solving: Thinking Recursively 617    

def isPalindrome(text) :
    length = len(text)
    # Separate case for shortest strings.
    if length <= 1 :
        return True
    else :
        # Get first and last characters, converted to lowercase.
        first = text[0].lower()
        last = text[length - 1].lower()
        if first.isalpha() and last.isalpha() :
            # Both are letters.
            if first == last :
               # Remove both first and last character.
               shorter = text[1 : length - 1]
               return isPalindrome(shorter)
            else :
               return False
        elif not last.isalpha() :
            # Remove last character.
            shorter = text[0 : length - 1]
            return isPalindrome(shorter)
        else :
           # Remove first character.
            shorter = text[1 : length]
            return isPalindrome(shorter)    

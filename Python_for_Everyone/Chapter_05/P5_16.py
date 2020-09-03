#P5.16 Write a recursive function
#def isPalindrome(string)
#that returns True if string is a palindrome, that is, a word that is the same when
#reversed. Examples of palindromes
#are “deed”, “rotor”, or “aibohphobia”. Hint: A
#word is a palindrome if the first and last letters match and the remainder is also a
#palindrome.



# Solution_1 Code : Without recursion ------------------------------------------------
#Used regular expressions to remove all non alphabets

import re
def ispalindrome(string):
    str_1 = ("").join([i for i in str(string) if re.search(r"[a-zA-Z]",i)])
    cont = []
    for i in range(len(str_1)):
        cont.insert(0,str_1[i])
    str_2 = ("").join(cont)
    print(str_1==str_2)

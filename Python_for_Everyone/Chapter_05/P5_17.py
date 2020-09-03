#P5.17 Use recursion to implement a function find(string, match) that tests whether match is
#contained in string:
#b = find("Mississippi", "sip") # Sets b to true
#Hint: If string starts with match, you are done. If not, consider the string that you
#obtain by removing the first character.

#Solution_1 Code ------------------------------------------------------------------------------
#Simple function returning whether a match exists or not. Returns True or False. 

def find(string,match):
    if string[:len(match)] == match:
        return True
    elif len(string) == 1:
        return False 
    return find(string[1:],match)

#Solution_2 Code ------------------------------------------------------------------------------
#Function with added features of returning the all the match cases and the index position of 
#each of the matches 

def find(string,match):
    find_string(string,match,len(string),0)

def find_string(string,match,constant1,constant2):
    if string[:len(match)] == match:
        print (f"Match at index position: {constant1-len(string)}")
        constant2 +=1
    elif len(string) == 1:
        print("\"Entire string checked\"")
        print("No match found"*(constant2==0))
        return 
    find_string(string[1:],match,constant1,constant2)
    
    
#important to use return. 
#Had it been used within the first condition, function would terminate at the first match case.  

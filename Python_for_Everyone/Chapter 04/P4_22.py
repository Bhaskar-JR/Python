P.4.22 Write a program that reads an integer and displays, using asterisks, a filled diamond
of the given side length. For example, if the side length is 4, the program should
display

*
***
*****
*******
*****
***
*

#Solution

#Defining the function to create to take in integer input and create the pattern
def diamond():
    n = int(input("Enter a integer:"))

    for row in range(2*n-1):
        #for the upper half : using boolean condition, printing stars in increasing order of count
        print((row<n)*(" "*(n-row-1)+"*"*(2*row+1)),end ="") 
        #for the lower half : using boolean condition, printing stars in decreasing order of count 
        print((row >=n)*(" "*(row-n+1)+"*"*(2*(2*n-row)-3)),end="")
        print("")     
        
 #Calling the function
diamond()

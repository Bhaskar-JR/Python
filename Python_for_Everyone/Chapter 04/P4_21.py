#P4.21 Write a program that reads an integer and displays, using asterisks, a filled and hollow
#square, placed next to each other. For example if the side length is 5, the program
#should display

***** *****
***** *   *
***** *   *
***** *   *
***** *****

#Solutions 
n = int(input("Enter a integer:"))

for row in range(n):
    print("*"*n+" "+"*",end ="")                          # Ensuring first block of characters ((n+2)=7 in the above case) are printed in every row 
    print("*"*(n-2)*((row == 0)|(row==(n-1))),end="")     # Printing asterisks marks only incase of top and bottom rows using boolean output  
    print(" "*(n-2)*((row != 0)&(row!=(n-1))),end="")     # Printing spaces for the intermediate rows
    print("*")                                            # Printing the last asterisk in a row
    

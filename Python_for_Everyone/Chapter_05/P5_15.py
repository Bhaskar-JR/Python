#P5.15 Write a recursive function def reverse(string) that computes the reverse of a string. 
For example, reverse("flow") should return "wolf".

Hint: Reverse the substring starting at the second character, then add the first
character at the end. For example, to reverse "flow", first reverse "low" to "wol", then
add the "f" at the end.

#Solution:

def reverse(string):
    x = str(string)
    x_rev =[]
    for i in range(len(x)):
        x_rev.append(x[len(x)-1-i])
        x_rev_string = ("").join(x_rev)
    return x_rev_string

#Please note that a string argument needs to be passed while calling the User defined function reverse(string argument).
# reverse(abcd) will return an error
# reverse("abcd") will return "dcba" as the output 
    


"""Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing."""

def reverses(alist):
    new_list = []
    for i in alist:
        new_list.insert(0, i)
    return new_list

print(reverses([1, 2, 3, 4, 5]))
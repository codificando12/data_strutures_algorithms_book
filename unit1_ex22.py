"""Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . ,n−1."""

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError("a and b must be of the same length")
    return sum([a[i] * b[i] for i in range(len(a))])

first = [1,2,3]
second = [3,4,5]

print(dot_product(first, second))
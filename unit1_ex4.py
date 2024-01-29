"""Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

def sum_squares(n):
    sumatory = 0
    for i in range(0, n):
        sumatory += i*i
    return sumatory

print(sum_squares(9))	
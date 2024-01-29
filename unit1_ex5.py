"""Give a single command that computes the sum from Exercise R-1.4, relying
on Python’s comprehension syntax and the built-in sum function."""

def sum_squares(n):
    sumatory = sum(i*i for i in range(0, n))
    return sumatory

print(sum_squares(9))	
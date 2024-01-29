"""Give a single command that computes the sum from Exercise R-1.6, relying
on Python’s comprehension syntax and the built-in sum function."""

def sum_odd_squares(n):
    sumatory = sum(i*i for i in range(0, n) if i % 2 == 0)
    return sumatory

print(sum_odd_squares(9))	
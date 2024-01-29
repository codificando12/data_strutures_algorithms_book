"""Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd."""

def is_odd_product(numbers):
    is_odd = []
    for i in numbers:
        for j in numbers:
            product = i * j
            if i != j and product % 2 == 1:
                is_odd.append(product)
    return is_odd

print(is_odd_product([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
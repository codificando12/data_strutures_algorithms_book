"""Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct)."""

def are_distinct(numbers):
    distinct = []

    for i in numbers:
        if i not in distinct:
            distinct.append(i)
        else:
            return "They are not distinct"
    return "They are distinct"

print(are_distinct([1, 2, 3, 4, 5, 7, 7, 8, 9, 10]))
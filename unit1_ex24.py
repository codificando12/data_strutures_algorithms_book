"""Write a short Python function that counts the number of vowels in a given
character string."""

def count_vowels(data):
    vowels = 'aeiou'
    data = data.lower()
    count = 0
    for char in data:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Hola como estas"))

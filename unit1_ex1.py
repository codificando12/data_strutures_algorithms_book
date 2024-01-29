""" Write a short python function is_multiple(n, m), that takes two integer values
and returns True if n is multiple of m, that is n= mi for some integers i and false otherwise"""

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False
    
while True:
    print("------------------------------")
    print("If you want to stop press q")
    print("If you want to calculate a multiple, press c")
    option = input("What would you like to do?(quit or calculate): ")
    if option == "c":
        try:
            num1 = int(input("Write the integer that you want check it multiple: "))
            num2 = int(input("write it's multiple: "))
            result = is_multiple(num1, num2)
            print(result)
        except ValueError:
            print("Error! Please Write an integer")
    elif option == "q":
        print("have a good day!")
        break
    else:
        print("Write a valid option")
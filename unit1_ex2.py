"""Write a short python function is_even(k) that takes
an integer value and return True if k is even and False otherwise
however your funtion can not use the multiplication, modulo or division
operators"""

def is_even(k):
    if k & 1 == 0:
        return True
    else:
        return False
    
while True:
    print("------------------------------")
    print("If you want to stop press q")
    print("If you want to check if a number is even, press c")

    option = input("Choose an option: ")
    if option == "c":
        try:
            num = int(input("Write a integer that you want to check: "))
            result = is_even(num)
            print(result)
        except:
            print("Error! Please write an integer")
    elif option == "q":
        break
    else:
        print("Write a valid option!")
    
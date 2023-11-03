# define the functions needed: add, sub, mul, div.
# print option to the user.
# ask for the values.
# call the function.
# while loop to continue the program untill the user wants to exit.

def add(a, b):
    answer = a + b
    print(str(a) + "+" + str(b) + '=' + str(answer))


def sub(a, b):
    answer = a - b
    print(str(a) + "-" + str(b) + '=' + str(answer))


def mul(a, b):
    answer = a * b
    print(str(a) + "*" + str(b) + '=' + str(answer))


def div(a, b):
    answer = a / b
    print(str(a) + "/" + str(b) + '=' + str(answer))


while True:
    print("A for Addition")
    print("B for Subraction")
    print("C for Multiplication")
    print("D for Division")
    print("E for Exit")

    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Enter the values: ")
        a = int(input("enter the first value: "))
        b = int(input("enter the second value: "))
        add(a, b)

    elif choice == "b" or choice == "B":
        print("Enter the values: ")
        a = int(input("enter the first value: "))
        b = int(input("enter the second value: "))
        sub(a, b)

    elif choice == "c" or choice == "C":
        print("Enter the values: ")
        a = int(input("enter the first value: "))
        b = int(input("enter the second value: "))
        mul(a, b)

    elif choice == "d" or choice == "D":
        print("Enter the values: ")
        a = int(input("enter the first value: "))
        b = int(input("enter the second value: "))
        div(a, b)

    else:
        print("Thanks for using the calculator")
        quit()

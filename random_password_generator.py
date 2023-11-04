

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    password_length = int(input("How long the password should be? "))

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print("Your password : ", password)
    print("")


option = input("Do you want to generate password? (yes/no) : ")

if option == "yes":
    generate_password()
elif option == "no":
    print("program ended")
    quit()
else:
    print("Invalid input, please enter yes or no")
    quit()

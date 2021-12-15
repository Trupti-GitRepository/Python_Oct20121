""" Menu driven application provides users to perform math and security functions."""
import secrets
import string
import math
import datetime
from datetime import date


def password_info():
    """ Secure password specification """
    print("\n*** Password Generator ***")
    print("Your secure password must contain:\
               \n\tUpper and lowercase letters,\
                \n\tAt least one number,\
                \n\tAt least one special character(@$!%*?^&_#),\
                 \n\tbetween 8 to 12 characters.")
def menu_option():
    """ Menu option to select on the application"""
    print("\n*** Menu options ***")
    print(f'{"a.Generate Secure Password":<40}')
    print(f'{"b.Calculate and Format a Percentage":<40}')
    print(f'{"c.How many days from today until July 4, 2025?":<40}')
    print(f'{"d.Use the Law of Cosines to calculate the leg of a triangle.":<40}')
    print(f'{"e.Calculate the volume of a Right Circular Cylinder":<40}')
    print(f'{"f.Exit program":<40}')


# Generate secure password
def secure_password(length):
    """ Generates secure password between specified length"""
    alphabets = string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation
    secret_password = "".join(secrets.choice(alphabets) for i in range(length))
    # print("length: ", len(secret_password))
    if (any(c.islower() for c in secret_password) and any(u.isupper() for u in secret_password)
            and any(n.isdigit() for n in secret_password)):
        print("Secret_password is ", secret_password)

    else:
        print("Generated password is not as per the specification.")


# Calculate percentage
def cal_percentage(num, dino):
    """
    :param num: numerator value
    :param dino: denominator
    :return: print value of the percentage
    """
    percentage = (num / dino) * 100
    print(f'\nPercentage of {num} and {dino} is {percentage:.3f} %')


# calculate how many days until
def cal_days():
    """Calculate day until july 4, 2025"""
    today = date.today()
    print(f"Today's date: {today}")

    given_date = datetime.date(2025, 7, 4)
    print(f'Given_date:{given_date}')

    days_left = (given_date - today)
    print(f"{days_left.days} Days left from today until July 4, 2025.( End date is not included.)")


# Calculate third leg of triangle
def law_of_cosines(len_a, len_b, angle):
    """ Calculate third leg of the triangle using law of Cosines c^2 = a^2 + b^2 - 2ab cos(C)"""
    # cos = math.cos(angle)
    # print(cos)
    # print(f'cos {cos:.2f}')
    square_c = (math.pow(len_a, 2) + math.pow(len_b, 2) - (2 * len_a * len_b) * (math.cos(angle)))
    # take a sqrt of C
    len_c = math.sqrt(square_c)
    print(f'The length of the triangle leg "c" is :{len_c:.2f}')


# Calculate volume of right cylinder function
def vol_cylinder(radius, height):
    """ Calculate a  volume of a right circular cylinder"""
    volume = math.pi * math.pow(radius, 2) * height
    print(f'Volume of the right circular cylinder is {volume:.2f}')


# User input for the menu option
print("\nWelcome to Math and Security Related Application. ")
menu_option()
reply = input("\nDo you want to use application?: Y/N  ").lower()
while reply == 'y':
    user_reply = input("\nPlease enter the menu option.:").lower()

    if user_reply == 'a':
        password_info()
        password_len = int(input("\nwhat length would you like your password to be: "))

        while password_len < 8 or password_len > 12:
            print("Invalid password length.")
            password_len = int(input("\nPassword length must be between 8 to 12.: "))

        secure_password(password_len)

    elif user_reply == 'b':
        print("*** Calculate percentage ***")
        numerator = float(input("Enter the value of the numerator: "))
        denominator = float(input("Enter the value of the denominator: "))
        while denominator == 0:
            print("Denominator value can not be zero")
            denominator = float(input("Enter the value of the denominator: "))

        cal_percentage(numerator, denominator)

    elif user_reply == 'c':
        print("\n*** Calculate Dates until july 4, 2025 ***")
        cal_days()

    elif user_reply == 'd':
        print("\n*** The Law of Cosines ***")
        side_a = int(input("Enter the length of side 'a':  "))
        side_b = int(input("Enter the length of side 'b':  "))
        angle_c = int(input("Enter the value of angle opposite of side 'c':  "))
        law_of_cosines(side_a, side_b, angle_c)

    elif user_reply == 'e':
        print("\n*** Volume of a Cylinder ***")
        r = int(input("Enter the base radius of right Circular cylinder :  "))
        h = int(input("Enter the height of the cylinder:  "))
        vol_cylinder(r, h)

    elif user_reply == 'f':
        print("Thank you for using Math and Security application.")
        break
    else:
        print("Incorrect menu option.")
    reply = input("\nDo you want to continue using Math and Security application?: Y/N ").lower()

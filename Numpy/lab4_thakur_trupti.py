'''Python Numpy and Pandas Application Code.'''
import re
import hashlib
import sys
import numpy as np
np.set_printoptions(precision=2)


def password_crackers():
    ''' password crakers tool'''
    # input a message to encode
    print('Enter a message to encode:')
    message = input()
    # encode it to bytes using UTF-8 encoding
    message = message.encode()
    # hash with MD5 (very weak)
    #print(hashlib.md5(message).hexdigest())
    # Lets try a stronger SHA-2 family
    print(hashlib.sha256(message).hexdigest())
    print(hashlib.sha512(message).hexdigest())


def menu_operation():
    """ Menu for matrix operations"""
    print("\nSelect a Matrix Operation from the list below:")
    print("a. Addition")
    print("b. Subtraction")
    print("c. Matrix Multiplication")
    print("d. Element by element multiplication")

def matrix_printing(matrix):
    """Printing  matrix """
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end="  ")
        print()


def matrix_transpose(matrix):
    ''' Matrix transpose functionality'''
    print("\nThe Transpose is:")
    transpose = np.transpose(matrix)
    matrix_printing(transpose)

def matrix_mean(matrix):
    '''Calculate mean of the matrix rows and columns'''
    print("\nThe row and column mean values of the results are:")
    print("Row:",np.mean(matrix, axis=1))
    # Function mean with axis =0 finds column means
    print("Column:",np.mean(matrix, axis=0))


def main():
    """ Entry point of the application to get input."""
    print("***************** Welcome to the Python Matrix Application***********")
    while True:
        prompt = input("Do you want to play the Matrix Game?"
                   "\nEnter Y for yes or N for No:").capitalize()
        if not re.search('^Y',prompt):
            print("Thanks for visiting Python Matrix Application. ")
            sys.exit(0)
        else:
            #checking phone number
            while True:
                phone = input("Enter your phone number (XXX-XXX-XXXX:)")
                if re.findall(r'^[2-9]\d{2}-\d{3}-\d{4}$', phone):
                    print(phone)
                    break
                else:
                    print("InValid number.")
                    continue
            # checking Zip code
            while True:
                zip_code = input("\nEnter your zip code+4(xxxxx-xxxx): ")
                if re.findall(r"\d{5}-\d{4}", zip_code):
                    print(zip_code)
                    break
                else:
                    print('Invalid zip code.')
                    continue

            # checking matrix functionality
            num = 9
            while True:
                first_matrix = []
                print("\nEnter your first 3 x 3 matrix, seperated by space:")
                try:
                    for i in range(num):
                        numbers = list(map(float, input().split()))
                        first_matrix = np.array(numbers).reshape(3, 3)
                        print("\nYour first 3x3 matrix is:")
                        matrix_printing(first_matrix)
                        break
                    break
                except ValueError:
                    print("Invalid Matrix. Please enter numbers ( 3 x 3) seperated by space.")

            # take input for Second matrix
            while True:
                second_matrix = []
                print("\nEnter your second 3 x 3 matrix, seperated by space:")
                try:
                    for i in range(num):
                        numbers = list(map(float, input().split()))
                        second_matrix = np.array(numbers).reshape(3, 3)
                        print("\nYour second 3x3 matrix is:")
                        matrix_printing(second_matrix)
                        break
                    break
                except ValueError:
                    print("Invalid Matrix. Please enter 3 x 3  numbers seperated by space.")

            # Matrix operations
            while True:
                menu_operation()
                char = input()
                if char == 'a':
                    print("\nYou selected Addition. The results are: ")
                    addition = first_matrix + second_matrix
                    matrix_printing(addition)
                    matrix_transpose(addition)
                    matrix_mean(addition)

                elif char == 'b':
                    print("You selected subtraction. The results are: ")
                    subtraction = first_matrix - second_matrix
                    matrix_printing(subtraction)
                    matrix_transpose(subtraction)
                    matrix_mean(subtraction)

                elif char == 'c':
                    print("You selected Matrix Multiplication. The results are: ")
                    multiplication = np.matmul(first_matrix, second_matrix)
                    matrix_printing(multiplication)
                    matrix_transpose(multiplication)
                    matrix_mean(multiplication)
                elif char == 'd':
                    print("You selected Element by element multiplication. The results are: ")
                    multiplication = (first_matrix * second_matrix)
                    matrix_printing(multiplication)
                    matrix_transpose(multiplication)
                    matrix_mean(multiplication)
                else:
                    print("Entered operation is not available in the list.")

                reply = input("\nDo you want to continue...Y/N").upper()
                if reply == 'N':
                    break
                else:
                    continue

main()
password_crackers()

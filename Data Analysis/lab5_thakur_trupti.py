import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('precision', 2)
np.set_printoptions(precision=2)


def menu_operation():
    """ Menu for Python Data Analysis App"""
    print("\nSelect the file you want to analyze: ")
    print("1. Population Data ")
    print("2. Housing Data")
    print("3. Exit the Program ")


def load_csv_file(filename):
    """ Read file. If file is not present then print message 'file does not not exist.' """
    csv_df = pd.read_csv(filename)
    return csv_df


def cal_stats(column):
    """calculate the count , mean , std_dev , minimum , maximum of the give distribution ."""
    data = np.array(column).flatten()
    count = data.shape[0]
    mean = np.mean(data)
    std_dev = np.std(data)
    minimum = min(data)
    maximum = max(data)
    print(f'Count : {count}\nMean : {mean:.2f} \nStandard Deviation:{std_dev:.2f}'
          f'\nMin : {minimum}\nMax : {maximum}')


def display_histogram(column_name, column_data):
    """ display histogram of selected column"""
    plt.title(column_name)
    plt.hist(column_data)
    plt.show()


def main():
    """ Entry point of the application to get input."""
    print("\n***************** Welcome to the Python Data Analysis App **********")
    while True:
        menu_operation()
        try:
            ans = int(input())
            if ans == 1:
                try:
                    df_pop_change = load_csv_file("PopChange.csv")
                    print("\nYou have entered Population Data.")
                except FileNotFoundError:
                    print("The file name you specified does not exist.")
                    break
                while True:
                    print("\nSelect the Column you want to analyze: ")
                    print("a. Pop Apr 1")
                    print("b. Pop Jul 1 ")
                    print("c. Change Pop ")
                    print("d. Exit Column")
                    char = input().lower()
                    if char == 'a':
                        print("You selected Pop Apr 1.\nThe statistics for this column are : ")
                        column_pop_apr = df_pop_change['Pop Apr 1']
                        cal_stats(column_pop_apr)
                        display_histogram('Pop Apr 1', column_pop_apr)

                    elif char == 'b':
                        print("You selected Pop Jul 1.\n The statistics for this column are: ")
                        column_pop_jul = df_pop_change['Pop Jul 1']
                        cal_stats(column_pop_jul)
                        display_histogram('Pop Jul 1', column_pop_jul)

                    elif char == 'c':
                        print("You selected Change Pop.\n The statistics for this column are: ")
                        column_change_pop = df_pop_change['Change Pop']
                        cal_stats(column_change_pop)
                        display_histogram('Change Pop', column_change_pop)

                    elif char == 'd':
                        print("You selected to exit the column menu.")
                        break

                    else:
                        print("Invalid choice")
                        continue

            elif ans == 2:
                try:
                    df_housing = load_csv_file("Housing.csv")
                    print("\nYou have entered Housing Data.")
                except FileNotFoundError:
                    print("The file name you specified does not exist.")
                    break

                while True:
                    print("\nSelect the Column you want to analyze: ")
                    print("a. AGE")
                    print("b. BEDRMS ")
                    print("c. BUILT ")
                    print("d. ROOMS ")
                    print("e. UTILITY ")
                    print("f. Exit Column")
                    char = input().upper()

                    if char == 'A':
                        print("\nYou selected AGE.\nThe statistics for this column are : ")
                        col_house_age = df_housing['AGE']
                        cal_stats(col_house_age)
                        display_histogram('AGE', col_house_age)

                    elif char == 'B':
                        print("\nYou selected BUILT.\n The statistics for this column are: ")
                        col_house_built = df_housing['BUILT']
                        cal_stats(col_house_built)
                        display_histogram('BUILT', col_house_built)

                    elif char == 'C':
                        print("\nYou selected BEDRMS.\n The statistics for this column are: ")
                        col_house_bedrms = df_housing['BEDRMS']
                        cal_stats(col_house_bedrms)
                        display_histogram('BEDRMS', col_house_bedrms)
                    elif char == 'D':
                        print("\nYou selected ROOMS.\n The statistics for this column are: ")
                        col_house_rooms = df_housing['ROOMS']
                        cal_stats(col_house_rooms)
                        display_histogram('ROOMS', col_house_rooms)
                    elif char == 'E':
                        print("\nYou selected UTILITY.\n The statistics for this column are: ")
                        col_house_utility = df_housing['UTILITY']
                        cal_stats(col_house_utility)
                        display_histogram('UTILITY', col_house_utility)

                    elif char == 'F':
                        print("\nYou selected to exit the column menu.")
                        break

                    else:
                        print("Invalid choice")
                        continue

            elif ans == 3:
                print("Thank you for using Python Data Analysis App.")
                sys.exit(0)
            else:
                print("Invalid choice")

        except ValueError:
            print("Invalid input.")


# Main function
main()

"""voter registration application"""
print("*********************************************************************")
print("Welcome to the Python Voter Registration Application.")

while True:
    user_input = input("Do you want to continue with Voter Registration? : ").lower()
    if user_input == 'yes':
        first_name = input("What is your first name?: ")
    else:
        print("Thanks for trying the Voter Registration Application.")
        break
    user_input = input("Do you want to continue with Voter Registration? : ").lower()
    if user_input == 'yes':
        last_name = input("What is your last name?: ")
    else:
        print("Thanks for trying the Voter Registration Application.")
        break
    user_input = input("Do you want to continue with Voter Registration? : ").lower()
    if user_input == 'yes':
        # Validate age
        while True:
            age = int(input("What is your age?: "))
            if age >= 18:
                if age <= 120:
                    pass
                else:
                    print("Applicant's age must be between 18 to 120 years.")
                    if age < 18:
                        age = 18 - age
                        print(f"Please come back in {age} years")
                        print("Thanks for trying the Voter Registration Application.")
                    else:
                        print("Entered age is not a valid age for voter registration.")
                        print("Thanks for trying the Voter Registration Application.")
                    break
            else:
                print("Applicant's age must be between 18 to 120 years.")
                if age < 18:
                    age = 18 - age
                    print(f"Please come back in {age} years")
                    print("Thanks for trying the Voter Registration Application.")
                else:
                    print("Entered age is not a valid age for voter registration.")
                    print("Thanks for trying the Voter Registration Application.")
                break

            user_input = input("Do you want to continue with Voter Registration? : ").lower()
            if user_input == 'yes':
                # Validate Citizenship
                citizenship = input("Are you a U.S. Citizen?: ").lower()
                if citizenship == 'yes':
                    user_input = input("Do you want to continue with Voter Registration?:")
                    user_input = user_input.lower()
                    if user_input == 'yes':
                        while True:
                            # Validate state
                            state = input("What state do you live?: ")
                            if len(state) != 2:
                                print("Enter two letters of a U.S.state you are living. ")
                            else:
                                break

                        user_input = input("Do you want to continue with Voter Registration?:")
                        user_input = user_input.lower()
                        if user_input == 'yes':
                            # Validate zipcode
                            zipcode = int(input("What is your zipcode?: "))
                            print('\nThanks for registering to vote.')
                            print('Here is the information we received:\n')
                            print(f'Name (first last): {first_name} {last_name}\n')
                            print(f"Age:{age}\nU.S.Citizen:{citizenship}\n")
                            print(f"State:{state}\nZipcode:{zipcode}\n")
                            print("Thanks for trying the Voter Registration Application.")
                            print("Your voter registration card should be shipped within 3 weeks.")
                            break
                    else:
                        print("Thanks for trying the Voter Registration Application.")
                        break

                else:
                    print("Applicant must be a US Citizen.")
                    print("Thanks for trying the Voter Registration Application.")
                    break
            else:
                print("Thanks for trying the Voter Registration Application.")
                break
            break
        break

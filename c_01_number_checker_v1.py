# Integer checker, used for components consisting of checking integers
# Code taken from "04_Pythagoras - Integer_float"
def number_checker(question, allow_floats="yes"):

    while True:
        response = input(question)

        if response == "xxx":
            return response

        elif response != "":
            try:
                if allow_floats == "yes":
                    response = float(response)

                    # When implemented into base, no sides (which the user has to find) will be less than 1
                    if response <= 0:
                        print("\nPlease input a valid NUMBER (> 0)\n")
                        continue

                elif allow_floats == "no":
                    response = int(response)

                    if response < 1:
                        print("\nPlease input a valid integer (> 0)\n")
                        continue

            except ValueError:
                print("<ValueError> That is an invalid INTEGER / NUMBER\n")
                continue

        return response


# Testing...
ask_integer = number_checker("Please input an integer: ", allow_floats="no")
print()
ask_number = number_checker("Please input a number: ", allow_floats="yes")

print(f"\nInteger: {ask_integer}   |   Number: {ask_number}")

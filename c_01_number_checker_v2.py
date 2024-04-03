# Integer checker, used for components consisting of checking integers
# Code taken from "04_Pythagoras - Integer_float"
def number_checker(question, error, input_type):

    while True:
        try:
            response = input_type(input(question))

            if response <= 0:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


get_int = number_checker("Input an integer: ", "Please input a valid integer (>0).\n", int)
print()

get_float = number_checker("Input a number: ", "Please input a valid number (>0).\n", float)
print()

print(f"Integer: {get_int}  |   Number: {get_float}")

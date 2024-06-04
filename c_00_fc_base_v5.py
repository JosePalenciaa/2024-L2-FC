import pandas
import math
from datetime import date

# Functions go here...


# Checks that users input is either a float or an integer (more than 0).
# Takes custom error messages, outputting where relevant.
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


# Outputs the instructions when the user wants
def instructions():

    print("Instructions go here\n")


# Function to check if user inputs y / n
def yes_no(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no)\n")


# Prevents string responses from being blank
def not_blank(question, error):
    while True:
        response = input(question).lower()

        if response == "":
            print(f"{error}. Please try again.")

        else:
            return response


# Adds dollar sign...
def currency(x):
    return f"${x:.2f}"


# Get expenses, returns list which has the data frame and subtotal
def get_expenses(var_fixed):
    # Set up dictionaries and lists
    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list
    }

    # Loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # Get name, quantity, and item
        item_name = not_blank("Item name: ", "The component name: ")
        if item_name.lower() == "xxx":
            break

        if var_fixed == "variable":
            quantity = number_checker("Quantity: ",
                                      "The amount must be a whole number", int)
        else:
            quantity = 1

        price = number_checker("How much for a single item? $",
                               "The price must be a number more than $0", float)

        # Add item, quantity, and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index("Item")

    # Calculate the cost of each component
    expense_frame["Cost"] = expense_frame["Quantity"] * expense_frame["Price"]

    # Find subtotal
    sub_total = expense_frame["Cost"].sum()

    # Currency formatting (uses currency function)
    add_dollars = ["Price", "Cost"]
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]

    
# Prints expense frames
def expense_print(heading, frame, subtotal):
    print()
    print(f"{heading} Costs")
    print(frame)
    print()
    print(f"{heading} Costs: ${subtotal:.2f}")
    return


def profit_goal(total_costs):

    # Initialise variables and error message
    error = "Please enter a valid profit goal \n"

    while True:

        # Ask for profit goal...
        response = input("What is your profit goal (e.g. $500 or %50)? ")

        # Check if first character is $...
        if response[0] == "$":
            profit_type = "$"
            # Get amount (everything after the $)
            amount = response[1:]

        # Check if last character is %
        elif response[-1] == "%":
            profit_type = "%"
            # Get amount (everything before the %)
            amount = response[:-1]

        else:
            # Set response to amount for now
            profit_type = "unknown"
            amount = response

        try:
            # Check amount is a number more than 0
            amount = float(amount)
            if amount <= 0:
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${amount:.2f}? ie {amount:.2f} dollars , ( y / n? ")

            if dollar_type == "yes":
                profit_type = "$"

            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"Do you mean {amount:.2f}%? y / n?")

            if percent_type == "yes":
                profit_type = "%"

            else:
                profit_type = "$"

        # Return profit goal to main routine
        if profit_type == "$":
            return amount

        else:
            goal = (amount / 100) * total_costs
            return goal


# Rounding Function
def round_up(amount, var_round_to):
    return int(math.ceil(amount / var_round_to)) * var_round_to


yesno_list = ["yes", "no"]

# Main routine goes here...

# Asks user if they want to see instructions (yes = display, no = continue)
display_instructions = yes_no("Have you used this calculator before? ")
print()

if display_instructions == "no":
    instructions()

# Gets product name(s)
product_name = not_blank("Product name: ", "The product name can not be numbers")

how_many = number_checker("\nHow many items will you be producing? "
                          , "The number of items must be a whole number (more than 0)"
                          , int)

print("\nPlease enter your variable costs below...")

# Get variable costs
variable_expenses = get_expenses("variable")
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

print()
have_fixed = yes_no("Do you have fixed costs (y / n)? ")

if have_fixed == "yes":

    # Get fixed costs
    fixed_expenses = get_expenses("fixed")
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

else:
    fixed_sub = 0

# Work out total costs and profit target
all_costs = variable_sub + fixed_sub
profit_target = profit_goal(all_costs)

# Calculates total sales needed to reach goal
sales_needed = all_costs + profit_target

# Ask user for rounding
round_to = number_checker("Round to nearest...? $", "Can't be 0", int)

# Calculate recommended price
selling_price = sales_needed / how_many

recommended_price = round_up(selling_price, round_to)

# *** Printing Area ***

if have_fixed == "yes":
    expense_print("Fixed", fixed_frame[["Cost"]], fixed_sub)

# Get current date for heading and file name
# Get today's date
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

file_heading = f"\n---- Fundraising Calculator - {product_name} ({day} / {month} / {year}) ----\n"
variable_heading = "**** Variable Costs ****\n"
fixed_heading = "\n**** Fixed Costs ****\n"

total_costs = f"\n\n!!! Total Costs: ${all_costs:.2f} !!!\n"

profit_sales_heading = "\n==== Profit & Sales Targets ===="
profit_target_txt = f"Profit Target: ${profit_target:.2f}"
total_sales = f"Total Sales: ${(all_costs + profit_target):.2f}"

recommended_price_txt = f"\n Recommended Selling Price: ${recommended_price:.2f} ****"

filename = f"FRC_{year}_{month}_{day}"

# Change frame to a string so that we can export it to file
variable_frame_string = pandas.DataFrame.to_string(variable_frame)
fixed_cost_string = pandas.DataFrame.to_string(fixed_frame)

to_write = [file_heading, variable_heading, variable_frame_string, fixed_heading, fixed_cost_string,
            total_costs, profit_sales_heading, profit_target_txt, total_sales, recommended_price_txt]

# Print Output
for item in to_write:
    print(item)

# Write output to file
# Create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# Close the file
text_file.close()

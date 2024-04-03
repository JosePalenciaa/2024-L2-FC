# Imports go here...
import pandas


# Functions go here...
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


# *** Main routine goes here ***

# Set up dictionaries and lists
item_list = []
quantity_list = []
price_list = []

variable_dict = {
    "Item": item_list,
    "Quantity": quantity_list,
    "Price": price_list
}

# Get user data...
product_name = not_blank("Product name: ", "The product name can't be blank.")

# Loop to get component, quantity and price
item_name = ""

while item_name.lower() != "xxx":

    print()
    # Gey name, quantity and item
    item_name = not_blank("Item Name: ", "The component name can't be blank.")

    quantity = number_checker("Quantity: ", "The amount must be a whole number more than zero", int)

    price = number_checker("How much for a single item? $", "The price must be a number more than 0.", float)

    if item_name.lower == "xxx":
        break

    # Add variables to list
    item_list.append(item_name)
    quantity_list.append(quantity)
    price_list.append(price)

variable_frame = pandas.DataFrame(variable_dict)
variable_frame = variable_frame.set_index("Item")

# Calculate cost of each component
variable_frame["Cost"] = variable_frame["Quantity"] * variable_frame["Price"]

# Find sub-total
variable_sub = variable_frame["Cost"].sum()

# Currency Formatting (uses currency function)
add_dollars = ["Price", "Cost"]
for item in add_dollars:
    variable_frame[item] = variable_frame[item].apply(currency)

# *** Printing Area ***
print(variable_frame)
print()
print(f"Variable Costs: {variable_sub:.2f}")

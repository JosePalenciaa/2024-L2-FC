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


# Gets expenses, returns list which has the data frame and subtotal
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


# *** Main routine goes here ***

# product_name = not_blank("Product name: ", "The product name can't be blank.")

fixed_expenses = get_expenses("fixed")
fixed_frame = fixed_expenses[0]
fixed_sub = fixed_expenses[1]

# *** Printing Area ***
print()
print(fixed_frame[["Cost"]])
print()
print(f"Fixed Costs: ${fixed_sub:.2f}")

def yes_no(question):
    while True:
        response = input(question).lower()

        for item in yesno_list:
            if response == item[0] or response == item:
                return item

        print("Please enter a valid response (yes / no)\n")


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
        elif response [-1] == "%":
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
            dollar_type = yes_no(f"Do you mean ${amount:.2f}? ie {amount:.2f} dollars , y / n? ")

            if dollar_type == "yes":
                profit_type = "$"

            else:
                profit_type =  "%"

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


# Main routine goes here...
yesno_list = ["yes", "no"]

all_costs = 200

for item in range(0, 6):
    profit_target = profit_goal(all_costs)
    print(f"Profit Target: ${profit_target:.2f}")
    print(f"Total Sales: ${all_costs + profit_target:.2f}")
    print()
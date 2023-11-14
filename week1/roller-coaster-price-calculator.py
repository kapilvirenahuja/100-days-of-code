# Script to start trying conditional statements. this is for a simple if-else
ticket_price = 0
add_on_price = 0

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age in years? "))
want_photo = input("Do you want a photo (yes/no)? ")

if (want_photo == "yes"):
    add_on_price = 3

if height >= 120:
    if age < 12:
        ticket_price = 5
    elif age <= 18:
        ticket_price = 7
    elif age >= 45 and age <= 55:
        # mid life crisis window
        ticket_price = 0
        add_on_price = 0
    else:
        ticket_price = 12

    ticket_price += add_on_price
    print("\n")
    print(
        f"You can ride the rollercoaster for a ticket price of ${ticket_price}"
    )
else:
    print("Sorry, you are not tall enough to ride the rollercoaster.")

print("Have a good day!")

# Comparison Operators
# > Grater than
# < less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

# Logical Operators
# and
# or
# not

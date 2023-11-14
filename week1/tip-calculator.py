#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill_value = float(input("What was the total Bill? "))
num_of_people = int(input("How many people should this be split in? "))

per_person_contribution = bill_value * 1.12 / num_of_people

# The following 2 statements are 2 ways of how we can force 2 decimal places

print("{:.2f}".format(per_person_contribution))

print(f"{per_person_contribution:.2f}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

selection_list = ["Rock", "Paper", "Scissors"]

user_selection = input("Select one of these: Rock (0), Paper (1) or Scissors (2):\n")
user_selection = int(user_selection)

computer_selection = random.randint(0, 2)


print (f"Computer selected {selection_list[computer_selection]} and you selected {selection_list[user_selection]}.")

if (computer_selection == user_selection) :
  print ("It's a Draw.")
elif (computer_selection == 2 and user_selection == 0) :
  print ("You win")
elif (computer_selection > user_selection) :
  print ("Computer wins")
else :
  print ("You win.")

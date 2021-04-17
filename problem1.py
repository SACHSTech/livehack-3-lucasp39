"""
********************************************************
Filename:       problem1.py
Description:    Calculate tournament scores for group placement 
Author:         Pei.L
Created On:     23/02/2021
********************************************************
"""
print("******Tournament Tracker******")
print("")

#set variables
win_count = 0

#use for loop to count the number of wins
for i in range(6):

    win_or_loss = input("Enter the wins and losses for your team: ")
    win_or_loss_capitalized = win_or_loss.capitalize()
    if win_or_loss_capitalized[0] == "W":
      win_count = win_count + 1

print("")

#print final grouping based on number of wins
if win_count == 5 or win_count == 6:
  print("Your team is in Group 1")
elif win_count == 3 or win_count == 4:
  print("Your team is in Group 2")
elif win_count == 1 or win_count == 2:
  print("Your team is in Group 3")
else:
  print("Your team is eliminated from the tournament")
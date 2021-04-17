"""
********************************************************
Filename:       problem1.py
Description:    Calculate tournament scores for group placement 
Author:         Pei.L
Created On:     23/02/2021
********************************************************
"""
print("******Tournament Tracker******")

#set variable 
distance = 0
days_travelled = 0

print("")
print("** Travel Long **")

#find distance travelled and number of days using while loops
while distance < 101:
  distance_travelled = float(input("Enter the distance travelled for the day: "))
  distance = distance + distance_travelled
  days_travelled += 1 

#calculate average distance per day
average_distance = distance / days_travelled

print("")
print("** Summary **")

#print final statements with days travelled and average distance for the user
print("It took " + str(days_travelled) + " days to surpass 100km driven")
print("The average distance driven per day is " + str(round(average_distance,2)) + " km")
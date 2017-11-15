import math
# Allows us to do the complex math of exponential equations for the rest of the
# program
from sys import argv
# Allows us to take in the RMS value as an argument from the command run in the
# bash script

# RMS = input("Enter the RMS: ")
# This "commented out" line was for when I was manually inputting RMS to test,
# rather than taking it as an argument

rms = int(argv[1])
# Stores the RMS value of the current instance passed by the argument
rms = rms * 1.5
# Adjusts the RMS by multiplying it by 1.5 to yield more accurate results

exp_factor = 0
# Initializes the variable exp_factor that will be determined based off of
# the different ranges of RMS values

if (rms == 0):
	RMS = 1
# Edge case for 0 as it will crash the entire program if we don't change it to 1

if (rms >= 101.2):
	exp_factor=-0.169347
elif (rms >= 87.5):
	exp_factor=-0.099219
else:
	exp_factor=-0.081395
# Uses logial if and else statements to change the exp_variable to the correct
# value

FINAL_DISTANCE = (math.log(rms/236.0))/exp_factor
# Performs the necessary calculations to finally store the correct distance
# value in the variable FINAL_DISTANCE

print FINAL_DISTANCE
# Prints the final answer of the algorithm

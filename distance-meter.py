import math
import soundmeter as meter
from sys import argv


#RMS = input("Enter the RMS: ")
RMS = int(argv[1])
RMS = RMS * 1.5


exp_factor = 0

if (RMS == 0):
	RMS = 1

if (RMS >= 101.2):
	exp_factor=-0.169347
elif (RMS >= 87.5):
	exp_factor=-0.099219
else:
	exp_factor=-0.081395

FT = (math.log(RMS/236.0))/exp_factor

print FT

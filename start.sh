# This is a bash script, basically a program which allows you to automate commands
# In this case, it allows me to use the soundmeter program and then feed specific results to my own Python script

while [ true ]
do
	# A while loop allows these 2 commands to run infinetely until the user hits Ctrl+C on the keyboard

	RMS=$(soundmeter -c -s 8 | grep max: | awk '{print $2}')
	# Runs the soundmeter program for 10 seconds, collects the maximum RMS detected, and then stores this in the variable RMS

	python2 distance-meter.py $RMS
	# Feeds the RMS value to my Python script
done

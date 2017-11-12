# Hello World

while [ true ]
do
	RMS=$(soundmeter -c -s 8 | grep max: | awk '{print $2}')
	python2 distance-meter.py $RMS
done

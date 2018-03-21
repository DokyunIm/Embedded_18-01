#/bin/bash

s="/sys/class/gpio/gpio21"
if [ -d ${s} ]; then
		echo "gpio21 exists"
else
		echo 21 > /sys/class/gpio/export
		echo "gpio21 created"
fi
echo out > ${s}/direction
while ((1))
do
		echo 1 > ${s}/value
		sleep 1
		echo 0 > ${s}/value
		sleep 1
done

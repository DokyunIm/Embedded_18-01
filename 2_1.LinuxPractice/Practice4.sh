## List up the ALL user ids in an ascending order
# cat /etc/passwd | awk -F: '{print $1}' | sort

## Check the hardware information
## Processor 
# cat /proc/cpuinfo | grep processor

## Memory Size
# cat /proc/meminfo | grep MemTotal

## Arichitecture Info
# uname -a

# set directory
dir=$HOME/Practice5

# if directory is not existed, Making New directory
echo "Making Folder..."
if [ -d ${dir} ]; then
	echo "${dir} exists. Using this Folder."
else
	echo "${dir} created."
	mkdir ${dir}
fi

# Print users having '/bin/bash'
echo -e "<<User Info>>" > ${dir}/Practice5.txt
cat /etc/passwd | grep bash | awk -F: '{print $1}' | sort >> ${dir}/Practice5.txt

# Print proccessor info 
echo -e "\n<<Processor Info>>" >> ${dir}/Practice5.txt
cat /proc/cpuinfo >> ${dir}/Practice5.txt

# Print memory info
echo -e "\n<<Memory Info>>" >> ${dir}/Practice5.txt
cat /proc/meminfo | grep MemTotal >> ${dir}/Practice5.txt

# Print Architecture info
echo -e "\n<<Architecture Info>>" >> ${dir}/Practice5.txt
uname -a >> ${dir}/Practice5.txt

echo "Succeed to write system info to ${dir}/Practice5.txt"

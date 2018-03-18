## Install openssh_server
# sudo apt-get install openssh-server

## Change the port number of ssh server
# sudo vim /etc/ssh/sshd_config
	##Port 22 -> Port 10022

## ssh service restart
# sudo service ssh restart

## Test to access with your account
# ssh [-p your_port_number] [yourID]@hostname

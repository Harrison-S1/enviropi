# Enviro Pi

To monitor temperature and humidity in Zabbix from a Raspberry Pi.

## Documentation

Download and install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/)\

Select and write your distro. Im using [Ubuntu](https://ubuntu.com/) Server 20.04 LTS\
Log into your Pi with SSH or however you are accessing it\
Update the repos and OS
 
`sudo apt update && sudo apt upgrade`

More on the way.

## DHT22 temperature-humidity sensor

https://learn.adafruit.com/dht
[Adafruit CircuitPython Module Install](https://learn.adafruit.com/dht/dht-circuitpython-code)

## Ansible

playbook coming.

 

## Zabbix set up

You will need a running Zabbix server.
Guide [here](https://www.zabbix.com/download?zabbix=5.0&os_distribution=ubuntu&os_version=20.04_focal&db=mysql&ws=apache) for a standard server set up.\
Will look to add a docker image later on.  

## Parts list

Raspberry Pi 4 Model B 8 GB - This can be a 2GB model, 8GB is just what I was using.\
Official EU Raspberry Pi 4 Power Supply (5.1V 3A)\
SanDisk Extreme Pro 128GB microSDXC\
AZDelivery DHT22 AM2302 Temperature and Humidity Sensor\
Geekworm Raspberry Pi 4 Aluminum Case\
Jumper wires (nice to have but not essential)

# Enviro Pi

To monitor temperature and humidity in Zabbix from a Raspberry Pi.

## Documentation

Download and install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/)\

Select and write your distro. Im using [Ubuntu](https://ubuntu.com/) Server 20.04 LTS\
Log into your Pi with SSH or however you are accessing it\
Update the repos and OS
 
`sudo apt update && sudo apt upgrade`

Install pip

`sudo apt-get install python3-pip`

`sudo pip install launchpadlib`

`sudo python3 -m pip install --upgrade pip setuptools wheel`


Will need to install schedule\
`sudo pip install schedule`

And install the Adafruit DHT module\
`sudo pip3 install Adafruit_DHT`

Make the enviropi.py script executable\
`chmod +x enviropi.py`

If you already have you senor wired up, you can run the enviropi.py with\
`sudo python3 enviropi.py`

## DHT22 temperature-humidity sensor

https://learn.adafruit.com/dht \
[Adafruit CircuitPython Module Install](https://learn.adafruit.com/dht/dht-circuitpython-code) \
[Adafruit-DHT 1.4.0](https://pypi.org/project/Adafruit-DHT/) \
[ref code](https://newbedev.com/python-dht22-on-raspberry-pi-4-code-example)

## Ansible

playbook coming.

 
## Zabbix set up

You will need a running Zabbix server.
Guide [here](https://www.zabbix.com/download?zabbix=5.0&os_distribution=ubuntu&os_version=20.04_focal&db=mysql&ws=apache) for a standard server set up.\
Will look to add a docker image later on.\ 
Once you have your Zabbix server you can then import the template created. There are two log files that are being monitored, one for the temperature and one for humidity.\
There are four tiggers, two for each log. If the temperate is more than X value then your tigger is set off and the same for the hunidity.   


## Parts list

Raspberry Pi 4 Model B 8 GB - This can be a 2GB model, 8GB is just what I was using.\
Official EU Raspberry Pi 4 Power Supply (5.1V 3A)\
SanDisk Extreme Pro 128GB microSDXC\
AZDelivery DHT22 AM2302 Temperature and Humidity Sensor\
Geekworm Raspberry Pi 4 Aluminum Case\
Jumper wires (nice to have but not essential)

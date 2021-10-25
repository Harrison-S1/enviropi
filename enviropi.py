#!/usr/bin/python3

import Adafruit_DHT
import logging
import schedule
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

#Turn this into a function so the scheduler could be used. 

def temp():
#Logging the data to the temp.log file. Level set to info and format to only have the message.
#Because the data is being pulled into Zabbix I only wanted the numeric value. The time stamp will be within Zabbix.
#Have left a format to have the message and time stamp for debugging.

    logging.basicConfig(filename='/var/log/temp.log', level=logging.INFO,
        format='%(message)s')
        #format='%(asctime)s:%(message)s')

    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
#Have left the ref to the humidity metric. For my use case I only need the temp, but if you want the humitiy as well in a nice format, its there.
    if humidity is not None and temperature is not None:
        #logging.info("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
        logging.info("{0:0.1f}".format(temperature, humidity))
    else:
        logging.info("Failed to retrieve data from the sensor")

#Set the scheduler to every 300 seconds (every 5 mins) 
schedule.every(300).seconds.do(temp)

while 1:
    schedule.run_pending()
    time.sleep(1)


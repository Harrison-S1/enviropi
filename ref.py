import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        logging.info("{0:0.1f}  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        logging.info("Failed to retrieve data from humidity sensor")

import Adafruit_DHT
import time


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
full_path_to_file = "/home/pi/DHT11.txt"

while True:
    h, t = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if h is not None and t is not None:
        toSaveString = """
                en son alınan geçerli değer: {0}
                
                sıcaklık:   {1},
                nem:    {2}\n
                
                        """.format(
                                str(datetime.datetime.now()),
                                t, h)
    else:
        print("sensor okumasında sıkıntı var")

    time.sleep(3)


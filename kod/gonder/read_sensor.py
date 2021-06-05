import Adafruit_DHT
import datetime
import time

# native modulleri indir
from cred import full_path_to_file, DHT_PIN
from AzureBlob import main as senk_main

sensor = Adafruit_DHT.DHT22

humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)

try:
    while True:
        if humidity is not None and temperature is not None:
            print('Temp={:.1f}*C  Humidity={}%'.format(temperature,humidity))

            toSaveString = """
                sıcaklık:   {:.1f}*C ,
                nem:    {}%\n

                """.format(temperature, humidity)



            with open(full_path_to_file, "a") as f:
                f.write(toSaveString)
                print("dosya yazma başarılı")
                f.close()

           # kaydetme işi bittiğinden senkron et
            senk = senk_main()
            if senk:
                print("Dosya başarılı bir şekilde Azure'a yollandı.")
            if not senk:
                print("Senkronize etme başarısız")
  

        else:
            #print('Failed to get reading. Try again!')
            print('dosya okuma ve yazma başarısız')

        time.sleep(3)

except KeyboardInterrupt:
    print("Cleanup")

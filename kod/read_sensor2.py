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
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format( temperature,
                                                                humidity))

            toSaveString1 = """
                en son alınan geçerli değer: {0}

                sıcaklık:   {0:0.1f}*C ,
                nem:    {1:0.1f}%\n

                """.format(str(datetime.datetime.now()),
                                   temperature,
                                   humidity)



            with open(full_path_to_file, "a") as f:
                f.write(toSaveString)
                print("dosya yazma başarılı")
                f.close()

           # kaydetme işi bittiğinden senkron et
            senk = senk_main()
            if senk:
                print("Azure'a yollandı")
            if not senk:
                print("opisee")
  

        else:
            #print('Failed to get reading. Try again!')
            print('dosya okuma ve yazma başarısız')

        time.sleep(3)

except KeyboardInterrupt:
    print("Cleanup")

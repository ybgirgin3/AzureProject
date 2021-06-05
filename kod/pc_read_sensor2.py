#import Adafruit_DHT
import datetime

# native modulleri indir
from cred import full_path_to_file, DHT_PIN
from AzureBlob import main as senk_main

#sensor = Adafruit_DHT.DHT22

#humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT_PIN)

try:

    toSaveString = "en son deneme budur"


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


except KeyboardInterrupt:
    print("Cleanup")

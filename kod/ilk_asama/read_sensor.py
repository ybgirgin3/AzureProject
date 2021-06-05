import RPi.GPIO as GPIO
import dht11
import time
import datetime
# kayıt edilecek olan dosyanın yolunu aldık
#from cred import full_path_to_file, DHT_PIN
#from AzureBlob import main as senk_main

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
DHT_PIN = 14
full_path_to_file = "/home/pi/DHT11.txt"
instance = dht11.DHT11(pin=DHT_PIN)

try:
    while True:
        result = instance.read()
        # eğer sensörden gelen değer geçerli ise
        if result.is_valid():
            
            # TERMINAL EKRANINA YAZDIRMA KISMI KULLANICI ISTEGINE BAGLI
            """ 
            print("En son alınan geçerli değer: " + str(datetime.datetime.now()))
            print("Sıcaklık: %-3.1f C" % result.temperature)
            print("Nem: %-3.1f %%" % result.humidity)
            """
            
            toSaveString = """
                    en son alınan geçerli değer: {0}
                    
                    sıcaklık:   {1},
                    nem:    {2}\n
                    
                            """.format(str(datetime.datetime.now()), 
                                       result.temperature,
                                       result.humidity)
                            
            # verileri belgeye kaydet
            # kayıt işlemi tamamlandıktan sonra senkron et
            with open(full_path_to_file, "a") as f:
                f.write(toSaveString)
                f.close()
              
            # kaydetme işi bittiğinden senkron et
            """
            senk = senk_main()
            if senk:
                print("Azure'a yollandı")
            if not senk:
                print("opisee")
            """

            

        time.sleep(6)

except KeyboardInterrupt:
    print("Cleanup")
    GPIO.cleanup()

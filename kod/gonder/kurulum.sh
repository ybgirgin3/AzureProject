# install req
sudo apt-get install git
echo "gerekli kütüphaneler pip ile yükleniyor"
pip3 install -r requirements.txt

echo "Adafruit kütüphanesi yükleniyor"
mkdir cikti/
mkdir lib/ && cd lib/
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install
echo """

  Kütüphanelerin kurulum tamamlandı.
  Sensör çıktılarını programınız ile aynı dizin içinde 
        cikti
  klasörü içinde bulabilirsiniz.
  Azure'a dosya gönderme işlemi "read_sensor.py" dosyası içinde otomatik olarak tetiklenmektedir.
  Tek yapılması gereken "python3 read_sensor.py" komutu ile projeyi çalıştırmak.

"""


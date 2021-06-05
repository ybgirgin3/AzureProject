# install req
echo "Eğer uygulamayı çalıştırdığınızda "... already in use" gibi bir hata alırsanız"
echo "rpi'nizi baştan başlatıp tekrar deneyin. Çünkü kullandığınız IDE hata aldığından programı tamamen kapatmak yerine sessize alıyor olabilir"
echo "Gerekli kütüphaneler yükleniyor"

pip3 install -r requirements.txt


echo "DHT11 için gerekli olan kütüphane yükleniyor"
# install DHT11
mkdir repo/ && cd repo/
git clone https://github.com/szazo/DHT11_Python.git
cd DHT11_Python/
pip3 install .




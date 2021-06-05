import os

#### AZURE ICIN GEREKLI OLAN KISIM BASLANGICI #########

# projenin ana dizini ve hedefteki container'in ismi
#source_folder = "/home/berkay/code/freelance/AzureProject/kod/toSend"
source_folder = os.path.dirname(os.path.abspath(__file__))
source_container_name = "dhtverileri"

# hedefteki hesabın adı
account_name = "iotfinal"
local_file_name = "DHT11.txt"
full_path_to_file = os.path.join(source_folder, "cikti/", local_file_name)

# arkaplandaki gönderimlerin güvenliğini kontrol etmek için kullanılan anahtarlar
key1 = "eUfs7vLwL31flCFuu+NaPVe2Fw7lOeWhgbgslDrYT0YFJETYh45JJH6k4i4ngXupVfB5YC2xFHrWAG2oOd2fIQ=="
key2 = "mhjplhWo4go7P/MV7YGy2XWRC2TFxq1TV5cP1XPTPt1NaIFvgzRmrE28IiPtwZff3WEv4YzkgIx5uqqtdGvR1w=="

# kullanıcı adı ve şifresi olmadan bağlantı sağlamak için gerekli olan stringler
azure_storage_connectionfromstring = "DefaultEndpointsProtocol=https;AccountName=iotfinal;AccountKey=eUfs7vLwL31flCFuu+NaPVe2Fw7lOeWhgbgslDrYT0YFJETYh45JJH6k4i4ngXupVfB5YC2xFHrWAG2oOd2fIQ==;EndpointSuffix=core.windows.net"
azure_storage_connectionfromstring2 = "DefaultEndpointsProtocol=https;AccountName=iotfinal;AccountKey=mhjplhWo4go7P/MV7YGy2XWRC2TFxq1TV5cP1XPTPt1NaIFvgzRmrE28IiPtwZff3WEv4YzkgIx5uqqtdGvR1w==;EndpointSuffix=core.windows.net"

###### AZURE ICIN GEREKLI OLAN KISIM BITISI ###########


###### SENSOR ICIN GEREKLI OLAN KISIM BASLANGICI ########
DHT_PIN = 4
###### SENSOR ICIN GEREKLI OLAN KISIM BITISI ########

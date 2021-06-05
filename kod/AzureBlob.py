import os
import uuid
import sys
from azure.storage.blob import BlockBlobService, PublicAccess
from cred import (
    # kullanıcı adı ve şifresi olmadan bağlantı sağlamak için gerekli olan stringler
    azure_storage_connectionfromstring,
    azure_storage_connectionfromstring2,

    # projenin ana dizini ve hedefteki container'in ismi
    source_folder,
    source_container_name,

    # hedefteki hesabın adı
    account_name,

    # arkaplandaki gönderimlerin güvenliğini kontrol etmek için kullanılan
    # anahtarlar
    key1,
    key2,

    # gönderilecek olan dosyanın adı ve bilgisayardaki tam yolu
    local_file_name,
    full_path_to_file
)

# gönderme işlemini yapacak olan temel fonk
def main():
    try:
        # kullanıcı adı ve anahtar kullanarak yazılım
        # üzerinden bağlantı kurmak için kullanılan
        # komut
        blob_service_client = BlockBlobService(
            account_name = account_name,
            account_key = key1
            )

        print("Hedefteki dosya = " + full_path_to_file)
        print(local_file_name + "isimli dosya blob olarak depolamaya yazılıyor")

        # Upload the created file, use local_file_name for the blob name
        blob_service_client.create_blob_from_path(
            source_container_name, local_file_name, full_path_to_file)

        # List the blobs in the container
        print("\Azure Container'da bulunan blob dosyalarınız")
        generator = blob_service_client.list_blobs(source_container_name)
        for blob in generator:
            print("\t Blob Adı: " + blob.name)


        return True



    except Exception as e:
        print(e)
        return False

"""
# Main method.
if __name__ == '__main__':
    main()
"""

from minio import Minio
from minio.error import S3Error

def test_minio():
    client = Minio(
        "localhost:8000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    bucket_name = "testando"
    file_name = "arquivo.txt"

    try:
        # Criando um arquivo
        #with open(file_name, "w") as f:
        #    f.write("Olá, este é um teste de upload para o MinIO!")

        # Enviando um arquivo para um bucket específico
        #client.fput_object(
        #    "testando",       # Nome do bucket
        #    "arquivo.txt",    # Nome do arquivo dentro do bucket
        #    file_name         # Arquivo a ser enviado
        #)

        # Exibe todos os buckets existentes
        #buckets = client.list_buckets()
        #for bucket in buckets:
        #    print(f'Nome: {bucket.name}, Criado em: {bucket.creation_date}')

        # Exibe os objetos dentro de um bucket específico
        #objects = client.list_objects("teste", recursive=True)
        #for object in objects:
        #    print(object.object_name)

    except S3Error as e:
        print(f'Erro ao interagir com o minio: {e}')

if __name__ == "__main__":
    test_minio()
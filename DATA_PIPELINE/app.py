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
        with open(file_name, "w") as f:
            f.write("Olá, este é um teste de upload para o MinIO!")

        client.fput_object(
            "testando",
            "arquivo.txt",
            file_name
        )
        print("Arquivo enviado com sucesso!")
    except S3Error as e:
        print(f'Erro ao interagir com o minio: {e}')

if __name__ == "__main__":
    test_minio()
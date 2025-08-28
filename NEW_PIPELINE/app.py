from minio import Minio

client = Minio(
    "minio:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

buckets = client.list_buckets()

if buckets:
    print('Bucket encontrado:')
    for bucket in buckets:
        print(bucket.name)
else:
    print('Nenhum bucket encontrado!')
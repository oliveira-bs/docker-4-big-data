import boto3

# Configurar o cliente S3 para o LocalStack
s3 = boto3.client(
    's3',
    endpoint_url='http://localstack:4566',  # URL do LocalStack
    aws_access_key_id='fake-key',
    aws_secret_access_key='fake-secret',
    region_name='us-east-1'
)

# Criar o bucket
s3.create_bucket(Bucket='bucket-teste')
print("Bucket 'meu-bucket-teste' criado com sucesso!")

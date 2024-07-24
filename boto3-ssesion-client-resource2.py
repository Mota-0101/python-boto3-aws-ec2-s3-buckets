# Importando o Boto3
import boto3
# Criando a sessão e especificando o profile adm.
sessao = boto3.Session(profile_name="automacao-curso")
# Cliando o cliente s3 a partir da sessão:  
cliente_s3 = sessao.client('s3')
# Cliando o cliente EC2 a partir da sessão:
cliente_ec2 = sessao.client('ec2')
# Listando os buckets:
lista = cliente_s3.list_buckets()
#print(lista) #<- Print comentado, para não sujar a console.

# Método 'resource' sendo chamado no objeto 'sessão', para criar um específico do s3, sendo atribuído a variável 'recurso_s3'.
# 'recurso_s3' é agora um objeto 'Resource'(específico) que fornece uma interface de alto nível para interagir com o serviço S3 da AWS.
recurso_s3 = sessao.resource('s3')
# Método 'Bucket' é chamado no objeto 'recurso_s3', para criar um objeto 'bucket', para acessar o bucket 'saudacoes'.   
bucket = recurso_s3.Bucket('saudacoes')
print(bucket) # Print do bucket 'saudacoes'.
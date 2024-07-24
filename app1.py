# Importando o Boto3:
import boto3
# Criando uma sessão, especificando o profile adm:
sessao = boto3.Session(profile_name="-----")
# Criando um client a partir da sessão:
cliente_s3 = sessao.client('s3')
# Criando uma variável, para receber à lista de bickets:
lista = cliente_s3.list_buckets()
# Printando à lista:
print(lista)
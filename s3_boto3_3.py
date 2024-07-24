import boto3
# Criando sessão:
sessao = boto3.Session(profile_name='automacao-curso')
cliente_s3 = sessao.client('s3') # criando cliente, a partir da sessão.
# Criando variável, para armazenar o nome do bucket:
nome_bucket = 'pythot-bucket-1'
#Tratamento de excessão, caso o bucket criado já exista:
try:
    # Criando o bucket, a partir do cliente:
    resposta_bucket = cliente_s3.create_bucket(
        Bucket=nome_bucket, #1º parâmetro: Atribuindo o nome da variável criada acima, para indicar nome do bucket.
        CreateBucketConfiguration={ #2º parâmetro: indicando a localização onde será criado o bucket. 
            'LocationConstraint': 'us-east-2'
        }
    )
    #print(resposta_bucket) #<-print que foi comentado, para não sujar a console.
except Exception as err:
    print('Este bucket já existe')
    #print(err)  #<-print que foi comentado, para não sujar a console.

cliente_s3.upload_file( #Subindo um arquivo local para o bucket, com o método 'upload_file'.
    'arquivos/aws_light_theme_logo.svg',
    nome_bucket,
    'imagens/aws_logo.svg'
)
# Criando uma planilha com formato antigo.
planilha = """
    Nome\tNota
    Ana\t8
    Mario\t9
    Maria\t7
    Carlos\t7    
"""

# Indicando que a planilha será criada dentro do bucket 'nome_bucket', com o método 'put_objet', a partir do 'client'.
cliente_s3.put_object( 
    Body=planilha,
    Bucket=nome_bucket,
    Key='planilha.xls'
)
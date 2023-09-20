import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Usuarios')
dynamodb_client = boto3.client("dynamodb")
    
def lambda_handler(event, context):
    
    user = event['pathParameters']['id']

    cuerpo = json.loads(event['body'])
    
    nombre = cuerpo['nombre']
    correo = cuerpo['correo']
    genero = cuerpo['genero']
    edad = cuerpo['edad']
    us = 'user-'+user
    
    nuevo_elemento = {'pk': {'S': 'user'},'sk' : {'S': us}, 'correo': {'S': correo}, 'edad' : {'N': str(edad)}, 'genero' : {'S': genero}, 'nombre' : {'S': nombre}}
    
    nuevo = json.loads(json.dumps(nuevo_elemento, default=str))
    
    try:
        response = dynamodb_client.put_item(TableName='Usuarios', Item=nuevo)
        return {
            'statusCode' : 200,
            'body' : json.dumps("Elemento insertado")
        }
    except Exception as e:
        return {
            'statusCode' : 200,
            'body' : json.dumps("Elemento no insertado")
        }
    
    

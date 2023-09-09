import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')
    

    # Valores de la clave primaria y clave de ordenamiento
    pk = 'user'
    sk = event['pathParameters']['id']
    us = 'user-'+sk

    # Realizar la operación de eliminación
    response = table.delete_item(
        Key={
            'pk': pk,
            'sk': us
        }
    )

    return {
            'statusCode' : 200,
            'body' : json.dumps(
            {
                'statusCode' : 200,
                'body' : json.dumps('Usuario "'+us+ '" eliminado correctamente')
            }
            , default=str)
        }
        

    

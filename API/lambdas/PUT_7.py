import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')
    
    user = event['pathParameters']['id']
    
    body = json.loads(json.dumps(event['body'], default=str))
    cuerpo = json.loads(body)

    correo = cuerpo['correo']
    print(correo)
    edad = cuerpo['edad']
    print(edad)

    try:
        response = table.update_item(Key={'pk': 'user', 'sk': user},UpdateExpression='set correo=:correo, edad=:edad',ExpressionAttributeValues={':correo': correo, ':edad': edad},ReturnValues='UPDATED_NEW')
        return {
            'statusCode' : 200,
            'body' : json.dumps('Usuario '+user+' fue actualizado')
        }
    except Exception as err:
        return {
            'statusCode' : 200,
            'body' : json.dumps(err)
        }


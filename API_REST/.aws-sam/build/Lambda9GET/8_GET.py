
import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')

    # Valor para la clave primaria
    usuario_id = 'user'

    # Realizar la consulta utilizando la clave primaria
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('pk').eq(usuario_id)
    )

    # Obtener los usuarios que cumplen con la consulta
    usuarios = response.get('Items', [])
    
    us2 = []
    for us in usuarios:
        nombre = us['nombre']
        correo = us['correo']
        genero = us['genero']
        edad = us['edad']
        
        d = {}
        d["nombre"] = nombre
        d["correo"] = correo
        d["genero"] = genero
        d["edad"] = edad
        
        us2.append(d)

    return {
        'statusCode': 200,
        'body': json.dumps(us2, default=str)
    }

import json
import boto3

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('Usuarios')

    # Valor mínimo para el filtro
    edad = 18

    # Filtro para la consulta
    filtro = boto3.dynamodb.conditions.Attr('edad').gt(edad)

    # Realizar la consulta utilizando el método scan y el filtro
    response = table.scan(FilterExpression=filtro)
    
    # Obtener los usuarios que cumplen con el filtro
    usuarios = response.get('Items', [])

    if (len(usuarios) == 0):
        return {
            'statusCode': 200,
            'body': json.dumps('No se econtraron coincidencias')
        }
    else:
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
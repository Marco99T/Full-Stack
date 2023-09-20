import json
from cognito.verify import Check_User_Exists
from cognito.reset import Reset

def lambda_handler(event, context):
    body = json.loads(event['body'])
    username = body['correo']

    existe = Check_User_Exists(username)
    if existe == True:
        reset = Reset(username)
        if reset == True:
            return{
                'statusCode': 200,
                'body': json.dumps('Contrasena reseteada')
            }
        else:
            return{
                'statusCode': 500,
                'body': json.dumps(f'Error: {reset}')
            }
    else:
        return{
                'statusCode': 400,
                'body': json.dumps('El usuario no existe')
            }
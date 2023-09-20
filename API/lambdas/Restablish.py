import json

from cognito.verify import Check_User_Exists
from cognito.confirm_pas import Confirm_Password

def lambda_handler(event, context):
    body = json.loads(event['body'])
    username = body['correo']
    code = body['codigo']
    password = body['contrasena']

    exist = Check_User_Exists(username)
    if exist == True:
        confirm = Confirm_Password(username, code, password)
        if confirm == True:
            return{
                'statusCode': 200,
                'body': json.dumps('Contrasena restablecida correctamente')
            }
        else:
            return{
                'statusCode': 500,
                'body': json.dumps(f'Error la restablecer: {confirm}')
            }
    else:
        return{
                'statusCode': 400,
                'body': json.dumps('Error, el usuario no existe')
            }
import json
from cognito.verify import Check_User_Exists
from cognito.resend_code import Resend_Code

def lambda_handler(event, context):
    body = json.loads(event['body'])
    correo = body['correo']
    
    existe = Check_User_Exists(correo)
    if existe == True:
        estado = Resend_Code(correo)
        check = {
            'status': 'Codigo de verificacion reenviado',
            'body': estado
        }
        if estado != False:
            return {
                'statusCode': 200,
                'body': json.dumps(check)
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps('Error el reenviar codigo')
            }
    else:
        return{
            'statusCode': 400,
            'body': json.dumps('Error al reenviar codigo, verifique el correo')
        }
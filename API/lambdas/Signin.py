import json
from cognito.verify import Check_User_Exists
from cognito.register import Register_User
from cognito.agregar_grupo import Add_Group
from cognito.resend_code import Resend_Code

def lambda_handler(event, context):
    body = json.loads(event['body'])
    correo = body['correo']
    genero = body['genero']
    password = body['contrasena']
    gender = ''
    if genero == 'H': gender = 'male'
    else:   gender = 'female'

    response = Check_User_Exists(correo)
    #response = True
    if(response == False):
        #Relizamos el registro en Cognito
        action = 'SUPPRESS'             #Indicamos si hay un reenvido de validacion o no
        atributos = {
            'Name': 'email',
            'Value': correo,
            'Name' : 'gender',
            'Value' : gender
        }
        res = Register_User(correo, password, action, atributos)
        Resend_Code(correo)
        if res != False:
            if genero == 'H':
                Add_Group(correo, 'hombres')
            else:
                Add_Group(correo, 'mujeres')
            return{
                'statusCode' : 200,
                'body' : json.dumps(res)
            }
        else:
            return{
                'statusCode' : 500,
                'body' : json.dumps('Error al registrar el usuario')
            }
    else:
        return{
            'statusCode' : 400,
            'body' : json.dumps('El usuario ya existe')
        }
    
#action = 'RESEND'             #Indicamos si hay un reenvido de validacion o no
#egistrado = register_user('marco.iturbide99@hotmail.es', action)
#lambda_handler(None, None)
import json
from cognito.log import Token
from cognito.sub import Get_Sub
from cognito.verify import Check_User_Exists

def lambda_handler(event, context):
    body = json.loads(event['body'])
    correo = body['correo']
    print(correo)
    password = body['contrasena']
    print(password)

    user_check = Check_User_Exists(correo)
    if user_check == True:
        tok = Token(correo, password)
        if tok != 'Incorrect' and tok != 'Unconfirmed' and tok != 'Reset':
            AccessToken = tok['AuthenticationResult']['AccessToken']
            RefreshToken = tok['AuthenticationResult']['RefreshToken']
            sub = Get_Sub(AccessToken)

            response = {
                'AccessToken' : AccessToken,
                'RefreshToken' : RefreshToken,
                'Correo' : correo,
                'Usersub' : sub
            }

            return {
                'statusCode' : 200,
                'body' : json.dumps(response)
            }
        elif tok == 'Incorrect':
            return {
                'statusCode' : 400,
                'body' : json.dumps('Error al iniciar sesion, correo o contrasena incorrectos.')
            }
        elif tok == 'Reset':
            return {
                'statusCode' : 500,
                'body' : json.dumps('Error al iniciar sesion, contrasena restablecida, confirme su correo primero con el codigo que se envio a su correo.')
            }
        else:   #Usuario no confirmado
            return {
                'statusCode' : 400,
                'body' : json.dumps('Error al iniciar sesion, valide primero su correo con el codigo que se envio al correo proporcionado.')
            }
    else:
        return {
                'statusCode' : 400,
                'body' : json.dumps('Error, el usuario no existe.')
            }
from cognito.oscognito import *
import boto3

def Log_In_User(username, password):
    cognito_client = boto3.client('cognito-idp', region_name=region())
    try:
        response = cognito_client.initiate_auth(
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password
            },
            ClientId= id_cliente(),
        )
        print("Inicio de sesion satisfactorio")
        return response
    except cognito_client.exceptions.NotAuthorizedException as e:
        print(f"Error al iniciar sesion: {e}")
        return 'Incorrect'
    except cognito_client.exceptions.UserNotConfirmedException as ex:
        print(f'Error al iniciar sesion: {ex}')
        return 'Unconfirmed'
    except cognito_client.exceptions.PasswordResetRequiredException as ex:
        print(f'Error al iniciar sesion: {ex}')
        return 'Reset'
    
def Token(email, contrasena):
    value = Log_In_User(email, contrasena)
    if(value != 'Incorred' and value != 'Unconfirmed'):
        return value
    else: 
        print('Error al obtener token')
        return value

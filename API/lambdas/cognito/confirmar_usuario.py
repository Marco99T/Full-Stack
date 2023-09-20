import boto3
from cognito.oscognito import *

def Confirm_User(username, key):

    cognito_client = boto3.client('cognito-idp', region_name=region())

    try:
        response = cognito_client.confirm_sign_up(
            ClientId = id_cliente(),
            Username = username,
            ConfirmationCode = key,
            ForceAliasCreation=False,
        )
        print('Correo validado con exito')
        return response
    except cognito_client.exceptions.CodeMismatchException as e:
        print(f'Error al validar: {e}')
        return 'Unconcide'
    except cognito_client.exceptions.ExpiredCodeException as ex:
        print(f'Error al validar: {ex}')
        return 'Expired'
    except cognito_client.exceptions.NotAuthorizedException as exp:
        print(f'Error: {exp}')
        return 'Unauthorized'
    
#Confirm_User('marco.iturbide99@hotmail.es', '645009')
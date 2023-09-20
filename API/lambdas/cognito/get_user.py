import boto3
from cognito.oscognito import *

def Get_User(token):

    cognito_client = boto3.client('cognito-idp', region_name=region())
    try:
        response = cognito_client.get_user(
        AccessToken=token
    )
        print('Token correcto')
        return response
    except cognito_client.exceptions.NotAuthorizedException as e:
        print(f'Error al acceder: {e}')
        return 'Expired'
    except Exception as ex:
        print(f'Error al acceder: {ex}')
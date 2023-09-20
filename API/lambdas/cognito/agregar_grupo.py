from cognito.oscognito import *
import boto3

def Add_Group(username, group):
    cognito_client = boto3.client('cognito-idp',region_name=region())
    try:
        response = cognito_client.admin_add_user_to_group(
            UserPoolId= user_pool_id(),
            Username= username,
            GroupName= group
        )
        print(f'Usuario Movido al grupo {group}')
        return response
    except Exception as e:
        print(f'Error al registar al grupo {e}')
        return False
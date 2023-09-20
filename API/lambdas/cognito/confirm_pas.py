import boto3
from cognito.oscognito import region, user_pool_id, id_cliente 

def Confirm_Password(username, code, password):
    cognito_client = boto3.client('cognito-idp', region_name=region())
    try:
        cognito_client.confirm_forgot_password(
            ClientId= id_cliente(),
            Username= username,
            ConfirmationCode= code,
            Password= password,
        )
        print('Contrasena Restablecida')
        return True
    except Exception as e:
        print(f'Error: {e}')
        return e
    
#Confirm_Password('marco.iturbide99@hotmail.es', '706896', 'Milo9901020@')
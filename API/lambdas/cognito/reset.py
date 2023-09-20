from cognito.oscognito import region, user_pool_id
import boto3

def Reset(username):
    cognito_client = boto3.client('cognito-idp',region_name=region())
    try:
        cognito_client.admin_reset_user_password(
            UserPoolId= user_pool_id(),
            Username=username,
        )
        print('Reseteo de contrasena correcto, codigo de reseteo enviado a correo')
        return True
    except Exception as e:
        print(f'Error: {e}')
        return e
    
#print(Reset('marco.iturbide99@hotmail.es'))
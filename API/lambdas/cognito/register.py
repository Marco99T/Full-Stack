from cognito.oscognito import *
import boto3

def Register_User(email, password, action, attributos):
    cognito_client = boto3.client('cognito-idp', region_name=region())
    try:
        '''
        cognito_client.admin_create_user(
            UserPoolId= user_pool_id(),
            Username=email,
            UserAttributes=[attributos],
            ValidationData=[attributos],
            #TemporaryPassword= password,
            ForceAliasCreation=True,
            MessageAction= action,
            DesiredDeliveryMediums=[
                'EMAIL',
            ],
        )
        '''
        response = cognito_client.sign_up(
            ClientId = id_cliente(),
            Username = email,
            Password= password,
            UserAttributes=[attributos ],
            ValidationData=[attributos],
        )
        print("Usuario registrado exitosamente")
        return response
    except Exception as e:
        print(f"Error al registrar usuario: {e}")
        return False

# Llama a la función para registrar un usuario
#register_user('marco.iturbide99@hotmail.es', 'Milo230394@', 'SUPPRESS')

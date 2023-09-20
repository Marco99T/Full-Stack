from cognito.oscognito import *
import boto3

def Check_User_Exists(username):
    cognito_client = boto3.client('cognito-idp', region_name=region())
    try:
        cognito_client.admin_get_user(
            UserPoolId=user_pool_id(),
            Username=username
        )
        print("Usuario existe")
        return True
    except cognito_client.exceptions.UserNotFoundException as e:
        print(f"Usuario no encontrado: {e}")
        return False
    except Exception as e:
        print(f"Error al verificar usuario: {e}")
        return None

# Llama a la función para verificar si un usuario existe
#user_info = check_user_exists('marco.iturbide99@hotmail.es')

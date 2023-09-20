import boto3
from cognito.oscognito import *

def Resend_Code(username):
    # Configura el cliente de Amazon Cognito
    client = boto3.client('cognito-idp', region_name=region())
    try:
        # Reenvía el código de verificación al usuario
        response = client.resend_confirmation_code(
            ClientId=id_cliente(),
            Username=username
        )
        print("Código de verificación reenviado con éxito")
        return response
    except client.exceptions as e:
        print(f"Error al reenviar codigo: {e}")
        return False

#Resend_Code('marco.iturbide99@hotmail.es')

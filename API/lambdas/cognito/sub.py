import base64
import json

def Get_Sub(access_token):

    # Dividir el token en sus tres partes: Encabezado, Carga útil y Firma
    header, payload, _ = access_token.split('.')

    # Decodificar la sección de carga útil (payload) del token JWT
    payload_bytes = base64.urlsafe_b64decode(payload + '===')
    payload_str = payload_bytes.decode('utf-8')

    # Analizar la carga útil como un objeto JSON
    payload_data = json.loads(payload_str)

    # Acceder al valor 'sub' en la carga útil
    sub = payload_data.get('sub')

    print("Valor 'sub':", sub)
    return sub
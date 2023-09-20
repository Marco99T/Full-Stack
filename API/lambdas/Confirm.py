import json
from pynamo.crud import crear_registro
from cognito.log import Token
from cognito.sub import Get_Sub
from cognito.verify import Check_User_Exists
from cognito.confirmar_usuario import Confirm_User

def lambda_handler(event, context):

    body = json.loads(event['body'])
    correo = body['correo']
    code = body['codigo']
    nombre = body['nombre']
    edad = body['edad']
    genero = body['genero']
    password = body['contrasena']

    gender =''
    if genero == 'H':   gender='male'
    else:   gender = 'female'

    #Verificamos el correo
    user_encontrado = Check_User_Exists(correo)
    if user_encontrado == True:
        #Confirmamos el usuario
        estado = Confirm_User(correo, code)
        if estado != 'Expired' and estado != 'Unconcide' and estado != 'Unauthorized':
            toke = Token(correo, password)
            #Vemos si hay acceso
            if toke != 'Incorrect' and toke != 'Unconfirmed':
                AccessToken = toke['AuthenticationResult']['AccessToken']
                sub = Get_Sub(AccessToken)
                datos = {
                    'estado': 'Datos Actualizados',
                    'nombre': nombre,
                    'genero': genero,
                    'edad': edad,
                    'correo': correo,
                    'status': estado
                }
                user = gender+'-'+sub
                crear_registro (user, nombre, edad, genero, correo)
                return {
                        'statusCode' : 200,
                        'body' : json.dumps(datos)
                    }
            elif toke == 'Incorrect':
                return {
                    'statusCode' : 400,
                    'body' : json.dumps('Correo o contrasena incorrectos')
                }
            else:   #Usuario sin confirmar
                return {
                    'statusCode' : 400,
                    'body' : json.dumps('Usuario no confirmado, valide el correo con el codigo enviado a su correo')
                }
        elif estado == 'Expired':
            return {
                'statusCode' : 500,
                'body' : json.dumps('Error al confirmar usuario, codigo expirdado, solicite de nuevo el codigo')
            }
        elif estado == 'Unauthorized':
            return {
                'statusCode' : 400,
                'body' : json.dumps('Error al confirmar usuario, el usuario ya esta confirmado')
            }
        else:   #Codigo no coincide
            return {
                'statusCode' : 400,
                'body' : json.dumps('Error al confirmar usuario, codigo no coincide')
            }
    else:
        return {
                'statusCode' : 200,
                'body' : json.dumps('El usuario no existe, verifique el correo')
            }
import json
import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.connection.base import Connection

from model import MiTabla

# Configurar las credenciales y la región de AWS

# Restaurar la conexión con DynamoDB

# Métodos CRUD
class CRUD:


    # Crear una nueva entrada en la tabla
    def crear_registro(self, user, nombre, edad, genero, correo):
        registro = MiTabla(pk='user', sk='user-'+str(user), nombre=nombre, edad=edad, genero=genero, correo=correo)
        registro.save()
        return registro

    # Obtener un registro por su ID
    def obtener_registro_por_id(self, user):
        try:
            registro = MiTabla.query('user', MiTabla.sk == user).next()
            return registro
        except MiTabla.DoesNotExist:
            return None

    # Actualizar un registro
    def actualizar_registro(self, user, correo, edad):
        registro = self.obtener_registro_por_id(user)
        if registro:
            registro.correo= correo
            registro.edad= edad
            registro.save()
            return registro
        return None

    # Eliminar un registro por su ID
    def eliminar_registro(self, user):
        registro = self.obtener_registro_por_id(user)
        if registro:
            registro.delete()
            return True
        return False

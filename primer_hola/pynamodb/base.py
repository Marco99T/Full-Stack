import os
from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.connection.base import Connection

from model import MiTabla

# Definir el modelo de datos

class Base:
    def Crear_Tabla (self, nombre_tabla):
        
        # Crear la tabla (si aún no existe)
        if not MiTabla.exists():
            MiTabla.create_table(
                wait=True,
                read_capacity_units= 5,
                write_capacity_units= 5,
            )
            print ("Tabla creada con exito")
        else:
            print ("Error al crear tabla")
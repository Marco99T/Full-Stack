from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute
from pynamodb.connection.base import Connection

from cognito.oscognito import region


# Definir el modelo de datos
class MiTabla(Model):
    class Meta:
        table_name = 'Clientes'  # Reemplaza con el nombre de tu tabla
        region = region()  # Reemplaza con tu región
    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)
    nombre = UnicodeAttribute()
    edad = NumberAttribute()
    genero = UnicodeAttribute()
    correo = UnicodeAttribute()

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
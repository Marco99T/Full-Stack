from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute

class MiTabla(Model):
    class Meta:
        table_name = 'Clientes'  # Reemplaza con el nombre de tu tabla
        region = 'us-east-1'  # Reemplaza con tu región
    pk = UnicodeAttribute(hash_key=True)
    sk = UnicodeAttribute(range_key=True)
    nombre = UnicodeAttribute()
    edad = NumberAttribute()
    genero = UnicodeAttribute()
    correo = UnicodeAttribute()

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

# Métodos CRUD
def crear_registro(user, nombre, edad, genero, correo):
    registro = MiTabla(pk='user', sk='user-'+str(user), nombre=nombre, edad=edad, genero=genero, correo=correo)
    registro.save()
    return registro

# Obtener un registro por su ID
def obtener_registro_por_id(user):
    try:
        registro = MiTabla.query('user', MiTabla.sk == user).next()
        return registro
    except MiTabla.DoesNotExist:
        return None

# Actualizar un registro
def actualizar_registro(user, correo, edad):
    registro = obtener_registro_por_id(user)
    if registro:
        registro.correo= correo
        registro.edad= edad
        registro.save()
        return registro
    return None

# Eliminar un registro por su ID
def eliminar_registro(user):
    registro = obtener_registro_por_id(user)
    if registro:
        registro.delete()
        return True
    return False

#crear_registro(9,'marco Torres Iturbide', 24, 'H', 'marco.iturbide99@hotail.es' )
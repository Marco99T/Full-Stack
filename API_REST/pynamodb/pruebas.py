import json
from base import Base
from crud import CRUD


cli = Base()
cl = CRUD()



#cl.crear_registro(i, 'Marco', 34, 'M', 'mar@')                     #Agregar Registro
#cl.actualizar_registro(i, 'marco'+str(i)+'@hotmail.es', 34+i)      #Actualizar Registro

registro = cl.obtener_registro_por_id('user-4')                     #Consultar Registro
registro = registro.attribute_values

#cl.actualizar_registro('user-0', 'luis@hotmail.es', 23)                #A
#cl.eliminar_registro('user-9')                                          #Eliminar Registro

print(registro)
#Crear un diccionario con informacion personal



informacion_personal = {
    "nombre": "yordan zarate",
    "edad": 30,
    "ciudad": "QUITO",
    "Profesion": "Estudiante"
}

# Acceder y Modificar Valores
# Modificar la ciudad
informacion_personal["ciudad"] = "QUITO"

# Agregar una nueva clave-valor para profesión
informacion_personal["Profesion"] = "Estudiante"

# Verificar Existencia de Claves
if "telefono" not in informacion_personal:
    informacion_personal["Celular"] = "0996129334"

# Eliminar una Clave
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimir el Diccionario Final
print(informacion_personal)

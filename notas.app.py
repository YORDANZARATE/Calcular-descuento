# Escritura en un archivo de texto
# creamos un archivo llamado my_notes.txt en modo escritura ('w')
file = open('my_notes.txt', 'w')  # Abre el archivo
# Escribimos varias líneas de notas personales en el archivo
file.write("1. Hoy aprendí a manejar archivos de texto en Python.\n")
file.write("2. Python facilita el trabajo con archivos utilizando 'with open()'.\n")
file.write("3. Es importante cerrar los archivos después de trabajar con ellos.\n")
file.write("4. La función write() permite escribir texto en el archivo.\n")
file.write("5. Podemos leer el contenido del archivo utilizando readline() o readlines().\n")
file.write("6. Los archivos se cierran automáticamente cuando usamos 'with'.\n")
file.write("7. Git y GitHub me ayudan a mantener versiones de mi código y compartirlo.\n")
file.close()  # Cierra el archivo después de escribir

# Lectura del archivo de texto
file = open('my_notes.txt', 'r')  # Abre el archivo en modo lectura ('r')
# Lee todas las líneas del archivo de una en una utilizando readline()
line = file.readline()  # Lee la primera línea
while line:  # Mientras haya más líneas por leer
    print(line.strip())  # Muestra la línea en consola, eliminando el salto de línea al final
    line = file.readline()  # Lee la siguiente línea
file.close()  # Cierra el archivo después de leer

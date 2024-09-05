from mongoengine import Document, StringField, IntField, connect

# Conectar a la base de datos MongoDB
connect(db="nombre_de_tu_base_de_datos", host="localhost", port=27017)


# Definir un modelo (similar a un esquema en ORM)
class Usuario(Document):
    nombre = StringField(required=True)
    email = StringField(required=True, unique=True)
    edad = IntField()


# Crear un nuevo usuario
nuevo_usuario = Usuario(nombre="Victor", email="victor@example.com", edad=25)
nuevo_usuario.save()

# Consultar un usuario
usuario = Usuario.objects(email="victor@example.com").first()
print(usuario.nombre)  # Imprime: Victor

# Actualizar un usuario
usuario.edad = 26
usuario.save()

# Eliminar un usuario
usuario.delete()

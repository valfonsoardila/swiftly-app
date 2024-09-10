# Patrón de diseño DTO (Data Transfer Object)
class User:
    def __init__(self, fullname, password, email):
        self.__fullname = fullname
        self.__password = password
        self.__email = email

    # Getters y Setters
    def getFullname(self):
        return self.__fullname

    def setFullname(self, fullname):
        self.__fullname = fullname

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    # Métodos para conversión a JSON
    def toJson(self):
        return {
            "fullname": self.getFullname(),
            "password": self.getPassword(),
            "email": self.getEmail(),
        }

    # Método para convertir JSON a objeto User
    @classmethod
    def fromJson(cls, data):
        fullname = data.get("fullname")
        password = data.get("password")
        email = data.get("email")
        return cls(fullname, password, email)

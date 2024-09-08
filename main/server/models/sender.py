class Sender:
    def __init__(self):
        self.__name = None
        self.__department = None
        self.__phone = None

    def setName(self, name: str):
        self.__name = name
        return self

    def setDepartment(self, department: str):
        self.__department = department
        return self

    def setPhone(self, phone: str):
        self.__phone = phone
        return self

    def build(self):
        # Validaciones previas a la construcción
        if not self.__name:
            raise ValueError("El nombre es obligatorio")
        if not self.__phone:
            raise ValueError("El teléfono es obligatorio")
        return Sender(self.__name, self.__department, self.__phone)

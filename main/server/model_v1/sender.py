class Sender:
    def __init__(self, name: str, department: str, phone: str):
        self.__name = name
        self.__department = department
        self.__phone = phone

    def getName(self) -> str:
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getDepartment(self) -> str:
        return self.__department

    def setDepartment(self, department: str):
        self.__department = department

    def getPhone(self) -> str:
        return self.__phone

    def setPhone(self, phone: str):
        self.__phone = phone

    def toJson(self):
        return {
            "name": self.__name,
            "department": self.__department,
            "phone": self.__phone
        }

    @staticmethod
    def fromJson(data):
        sender = Sender(
            data.get('name'),
            data.get('department'),
            data.get('phone')
        )
        return sender

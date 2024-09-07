class Department():
    def __init__(self, name: str, postal_code: str) -> None:
        self.__name = name
        self.__postal_code = postal_code

    def get_name(self) -> str:
        return self.__name

    def get_postal_code(self) -> str:
        return self.__postal_code

    def set_name(self, name: str):
        self.__name = name

    def set_postal_code(self, postal_code: str):
        self.__postal_code = postal_code

    def to_json(self):
        return {
            'name': self.get_name(),
            'postal_code': self.get_postal_code(),
        }

    @classmethod
    def from_json(cls, data: dict):
        # Verificamos que el diccionario contiene las claves correctas
        name = data.get('name')
        postal_code = data.get('postal_code')
        
        # Creamos una nueva instancia de Department
        return cls(name=name, postal_code=postal_code)
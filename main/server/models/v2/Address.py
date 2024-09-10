import json, uuid

class Address:
    def __init__(self, street: str, neighborhood: str, city: str, state: str, country: str, postal_code: str):
        self.__id = uuid.uuid4().__str__()
        self.__street = street
        self.__neighborhood = neighborhood
        self.__city = city
        self.__state = state
        self.__country = country
        self.__postal_code = postal_code

    def getId(self)->str:
        return self.__id
    
    def setId(self, id: str):
        self.__id = id
    
    def getStreet(self) -> str:
        return self.__street

    def setStreet(self, street: str):
        self.__street = street

    def getNeighborhood(self) -> str:
        return self.__neighborhood

    def setNeighborhood(self, neighborhood: str):
        self.__neighborhood = neighborhood

    def getCity(self) -> str:
        return self.__city

    def setCity(self, city: str):
        self.__city = city

    def getState(self) -> str:
        return self.__state

    def setState(self, state: str):
        self.__state = state

    def getCountry(self) -> str:
        return self.__country

    def setCountry(self, country: str):
        self.__country = country

    def getPostalCode(self) -> str:
        return self.__postal_code

    def setPostalCode(self, postal_code: str):
        self.__postal_code = postal_code

    # Metodo ToJson 
    def to_json(self):
        return {
            "id": self.__id,
            "street": self.__street,
            "neighborhood": self.__neighborhood,
            "city": self.__city,
            "state": self.__state,
            "country": self.__country,
            "postal_code": self.__postal_code
        }

    # Metodo FromJson
    @classmethod
    def from_json(cls, data):
        return cls(
            street=data['street'],
            neighborhood=data['neighborhood'],
            city=data['city'],
            state=data['state'],
            country=data['country'],
            postal_code=data['postal_code']
        )

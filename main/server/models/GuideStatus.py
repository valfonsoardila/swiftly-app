import json

class GuideStatus:
    def __init__(self, detalles: list = None):
        self.__status = "En Despacho"  # Estado inicial privado
        self.__detalles = detalles if detalles is not None else []  # Lista de detalles privada

    def to_json(self):
        return json.dumps({
            "status": self.__status,
            "detalles": self.__detalles
        })

    @classmethod
    def from_json(cls, data):
        data_dict = json.loads(data)
        return cls(
            detalles=data_dict['detalles']
        )

    def add_detalle(self, detalle: str):
        self.__detalles.append((self.__status, detalle))

    def cambiar_estado(self, nuevo_status: str):
        if nuevo_status == "Finalizada":
            self.__status = nuevo_status
        else:
            raise ValueError("El estado solo puede cambiar a 'Finalizada'.")

    def get_status(self):
        return self.__status

    def get_detalles(self):
        return self.__detalles

from main.server.api.firebase.requests import countries_request
import uuid

countrys_data = [
    {"name": "Colombia", "code": "CO"},
    {"name": "Argentina", "code": "AR"},
    {"name": "Brazil", "code": "BR"},
    {"name": "Chile", "code": "CL"},
    {"name": "Mexico", "code": "MX"},
    {"name": "Peru", "code": "PE"},
    {"name": "Venezuela", "code": "VE"},
    {"name": "Ecuador", "code": "EC"},
    {"name": "Bolivia", "code": "BO"},
    {"name": "Uruguay", "code": "UY"},
    {"name": "Paraguay", "code": "PY"},
    {"name": "United States", "code": "US"},
    {"name": "Canada", "code": "CA"},
    {"name": "Spain", "code": "ES"},
    {"name": "Germany", "code": "DE"},
    {"name": "France", "code": "FR"},
    {"name": "United Kingdom", "code": "GB"},
    {"name": "Italy", "code": "IT"},
    {"name": "Netherlands", "code": "NL"},
    {"name": "China", "code": "CN"},
    {"name": "Japan", "code": "JP"},
    {"name": "South Korea", "code": "KR"},
    {"name": "India", "code": "IN"},
    {"name": "Russia", "code": "RU"},
    {"name": "Australia", "code": "AU"},
]


# Función para verificar si la colección ya tiene registros
def check_and_create_countries():
    # Leer todos los registros en la colección 'countrys'
    existing_countries = countries_request.read_countrys()

    # Si la colección está vacía, se crea y se llenan los datos
    if len(existing_countries) == 0:
        create_countrys()
        return False
    else:
        return existing_countries


def create_countrys():
    # Llamar al método para agregar los departamentos
    # a cada documento en la colección 'countrys' le asigna el nombre del departamento como ID
    for contry in countrys_data:
        # Asignar un UUID único a cada departamento
        contry["id"] = str(uuid.uuid4())
        countries_request.create_countrys(contry["name"], contry)
    return True


def read_countrys():
    result = countries_request.read_countrys()
    return result


def read_contry(codigo_postal):
    result = countries_request.read_contry(codigo_postal)
    return result


def update_contry(codigo_postal, update_data):
    result = countries_request.update_contry(codigo_postal, update_data)
    return result


def delete_contry(codigo_postal):
    result = countries_request.delete_contry(codigo_postal)
    return result

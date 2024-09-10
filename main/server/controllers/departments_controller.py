from main.server.api.firebase.requests import departments_request
import uuid

deparments_data = [
    {"departamento": "Amazonas", "codigo_postal": "910001", "capital": "Leticia"},
    {"departamento": "Antioquia", "codigo_postal": "050001", "capital": "Medellín"},
    {"departamento": "Arauca", "codigo_postal": "810001", "capital": "Arauca"},
    {"departamento": "Atlántico", "codigo_postal": "080001", "capital": "Barranquilla"},
    {"departamento": "Bolívar", "codigo_postal": "130001", "capital": "Cartagena"},
    {"departamento": "Boyacá", "codigo_postal": "150001", "capital": "Tunja"},
    {"departamento": "Caldas", "codigo_postal": "170001", "capital": "Manizales"},
    {"departamento": "Caquetá", "codigo_postal": "180001", "capital": "Florencia"},
    {"departamento": "Casanare", "codigo_postal": "850001", "capital": "Yopal"},
    {"departamento": "Cauca", "codigo_postal": "190001", "capital": "Popayán"},
    {"departamento": "Cesar", "codigo_postal": "200001", "capital": "Valledupar"},
    {"departamento": "Chocó", "codigo_postal": "270001", "capital": "Quibdó"},
    {"departamento": "Córdoba", "codigo_postal": "230001", "capital": "Montería"},
    {"departamento": "Cundinamarca", "codigo_postal": "250001", "capital": "Bogotá"},
    {"departamento": "Guainía", "codigo_postal": "940001", "capital": "Inírida"},
    {
        "departamento": "Guaviare",
        "codigo_postal": "950001",
        "capital": "San José del Guaviare",
    },
    {"departamento": "Huila", "codigo_postal": "410001", "capital": "Neiva"},
    {"departamento": "La Guajira", "codigo_postal": "440001", "capital": "Riohacha"},
    {"departamento": "Magdalena", "codigo_postal": "470001", "capital": "Santa Marta"},
    {"departamento": "Meta", "codigo_postal": "500001", "capital": "Villavicencio"},
    {"departamento": "Nariño", "codigo_postal": "520001", "capital": "Pasto"},
    {
        "departamento": "Norte de Santander",
        "codigo_postal": "540001",
        "capital": "Cúcuta",
    },
    {"departamento": "Putumayo", "codigo_postal": "860001", "capital": "Mocoa"},
    {"departamento": "Quindío", "codigo_postal": "630001", "capital": "Armenia"},
    {"departamento": "Risaralda", "codigo_postal": "660001", "capital": "Pereira"},
    {
        "departamento": "San Andrés y Providencia",
        "codigo_postal": "880001",
        "capital": "San Andrés",
    },
    {"departamento": "Santander", "codigo_postal": "680001", "capital": "Bucaramanga"},
    {"departamento": "Sucre", "codigo_postal": "700001", "capital": "Sincelejo"},
    {"departamento": "Tolima", "codigo_postal": "730001", "capital": "Ibagué"},
    {"departamento": "Valle del Cauca", "codigo_postal": "760001", "capital": "Cali"},
    {"departamento": "Vaupés", "codigo_postal": "970001", "capital": "Mitú"},
    {"departamento": "Vichada", "codigo_postal": "990001", "capital": "Puerto Carreño"},
]


# Función para verificar si la colección ya tiene registros
def check_and_create_departments():
    # Leer todos los registros en la colección 'departments'
    existing_departments = departments_request.read_departmentss()

    # Si la colección está vacía, se crea y se llenan los datos
    if len(existing_departments) == 0:
        create_departments()
        return False
    else:
        return existing_departments


def create_departments():
    # Llamar al método para agregar los departamentos
    # a cada documento en la colección 'departments' le asigna el nombre del departamento como ID
    for department in deparments_data:
        # Asignar un UUID único a cada departamento
        department["id"] = str(uuid.uuid4())
        departments_request.create_departments(department["departamento"], department)
    return True


def read_departmentss():
    result = departments_request.read_departmentss()
    return result


def read_departments(codigo_postal):
    result = departments_request.read_departments(codigo_postal)
    return result


def update_departments(codigo_postal, update_data):
    result = departments_request.update_departments(codigo_postal, update_data)
    return result


def delete_departments(codigo_postal):
    result = departments_request.delete_departments(codigo_postal)
    return result

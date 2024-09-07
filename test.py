from main.server.api.firebase.requests.recipient_request import create_recipient,list_recipient
#from main.server.models.Recipient import Recipient

#sender = Sender("Victor","Magdalena",["53326595"])

#print(sender.to_json())
#create_sender(sender.to_json())

# res = list_senders()
# senders = []
# for sender in res:

#     senders.append( Sender.from_json(sender.to_dict()))

# print(senders[0].get_name())

# dep = {
#   "departments": [
#     {
#       "name": "Amazonas",
#       "postal_code": "910001"
#     },
#     {
#       "name": "Antioquia",
#       "postal_code": "050001"
#     },
#     {
#       "name": "Arauca",
#       "postal_code": "810001"
#     },
#     {
#       "name": "Atlántico",
#       "postal_code": "080001"
#     },
#     {
#       "name": "Bolívar",
#       "postal_code": "130001"
#     },
#     {
#       "name": "Boyacá",
#       "postal_code": "150001"
#     },
#     {
#       "name": "Caldas",
#       "postal_code": "170001"
#     },
#     {
#       "name": "Caquetá",
#       "postal_code": "180001"
#     },
#     {
#       "name": "Casanare",
#       "postal_code": "850001"
#     },
#     {
#       "name": "Cauca",
#       "postal_code": "190001"
#     },
#     {
#       "name": "Cesar",
#       "postal_code": "200001"
#     },
#     {
#       "name": "Chocó",
#       "postal_code": "270001"
#     },
#     {
#       "name": "Córdoba",
#       "postal_code": "230001"
#     },
#     {
#       "name": "Cundinamarca",
#       "postal_code": "250001"
#     },
#     {
#       "name": "Guainía",
#       "postal_code": "940001"
#     },
#     {
#       "name": "Guaviare",
#       "postal_code": "950001"
#     },
#     {
#       "name": "Huila",
#       "postal_code": "410001"
#     },
#     {
#       "name": "La Guajira",
#       "postal_code": "440001"
#     },
#     {
#       "name": "Magdalena",
#       "postal_code": "470001"
#     },
#     {
#       "name": "Meta",
#       "postal_code": "500001"
#     },
#     {
#       "name": "Nariño",
#       "postal_code": "520001"
#     },
#     {
#       "name": "Norte de Santander",
#       "postal_code": "540001"
#     },
#     {
#       "name": "Putumayo",
#       "postal_code": "860001"
#     },
#     {
#       "name": "Quindío",
#       "postal_code": "630001"
#     },
#     {
#       "name": "Risaralda",
#       "postal_code": "660001"
#     },
#     {
#       "name": "San Andrés and Providencia",
#       "postal_code": "880001"
#     },
#     {
#       "name": "Santander",
#       "postal_code": "680001"
#     },
#     {
#       "name": "Sucre",
#       "postal_code": "700001"
#     },
#     {
#       "name": "Tolima",
#       "postal_code": "730001"
#     },
#     {
#       "name": "Valle del Cauca",
#       "postal_code": "760001"
#     },
#     {
#       "name": "Vaupés",
#       "postal_code": "970001"
#     },
#     {
#       "name": "Vichada",
#       "postal_code": "990001"
#     }
#   ]
# }


# #create_sender(dep)
# # for dept in dep["departamentos"]:
# #     print()



# rp = Recipient("carlos","alibaba.com","call 19 #29-83","Sabanas","Valledupar","Cesar","","",["123456789","987654321"])

# res =create_recipient(rp.to_json())
# print(res)


from datetime import datetime
from main.server.models.Box import Box
from main.server.models.Envelope import Envelope
from main.server.models.Package import Package
from main.server.api.firebase.requests.guide_request import create_guide

# Crear una guía de tipo Box

box1 = Box(
    guide_number=1001,
    date=datetime.now(),
    description="Caja de libros",
    weight=5.0,
    declared_value=50.0,
    international=False,
    sender_name="John Doe",
    sender_department="Logistics",
    sender_phone=["123456789"],
    recipient_name="Jane Smith",
    recipient_company="ABC Corp",
    recipient_street="123 Main St",
    recipient_neighborhood="Downtown",
    recipient_city="New York",
    recipient_state="NY",
    recipient_country="USA",
    recipient_postal_code="10001",
    recipient_phones=["123456789","987456632123"]
)


# Crear una guía de tipo Package

package = Package(
    guide_number=1002,
    date=datetime.now(),
    description="Paquete de ropa",
    weight=3.5,
    declared_value=80.0,
    international=True,
    sender_name="Alice Johnson",
    sender_department="Warehouse",
    sender_phone=["987654321"],
    recipient_name="Bob Brown",
    recipient_company="XYZ Ltd",
    recipient_street="456 Elm St",
    recipient_neighborhood="Uptown",
    recipient_city="Los Angeles",
    recipient_state="CA",
    recipient_country="USA",
    recipient_postal_code="90001",
    recipient_phones=["123456789","987456632123"]
)


# Crear una guía de tipo Envelope

envelope = Envelope(
    guide_number=1003,
    date=datetime.now(),
    description="Sobre con documentos",
    weight=0.5,
    declared_value=20.0,
    international=False,
    sender_name="Mark Davis",
    sender_department="Administration",
    sender_phone=["555666777"],
    recipient_name="Sara Connor",
    recipient_company="Tech Solutions",
    recipient_street="789 Oak St",
    recipient_neighborhood="Midtown",
    recipient_city="San Francisco",
    recipient_state="CA",
    recipient_country="USA",
    recipient_postal_code="94105",
    recipient_phones=["123456789","987456632123"])


box_id = create_guide(box1.to_json())
print(f"Box guide added with ID: {box_id}")

package_id = create_guide(package.to_json())
print(f"Package guide added with ID: {package_id}")

envelope_id = create_guide(envelope.to_json())
print(f"Envelope guide added with ID: {envelope_id}")




from Controller.ClientController import ClientController
from Controller.DeliveryController import DeliveryController
from Models.ClientModel import ClientModel
from Models.DeliveryModel import DeliveryModel

def create_client(client):
    client_controller = ClientController()
    client_controller.create(client)
    print("Client created successfully!")

def create_delivery(client_email, delivery):
    client_controller = ClientController()
    client = client_controller.get_by_email(client_email)
    delivery.clients.append(client)
    delivery_controller = DeliveryController()
    delivery_controller.create(delivery)
    print("Delivery created successfully!")

def get_all_clients():
    client_controller = ClientController()
    clients = client_controller.get_all()
    for client in clients:
        print(client.to_dict())

def get_all_deliveries():
    delivery_controller = DeliveryController()
    deliveries = delivery_controller.get_all()
    for delivery in deliveries:
        print(delivery.to_dict())

client = ClientModel(
        name="John Doe",
        email="teste2@teste.com",
        phone="999999999",
        address="Rua teste, 123"
    )
create_client(client)

delivery= DeliveryModel(
        product="Product Test",
        quantity=10,
        status="pending"
    )

create_delivery("teste2@teste.com", delivery)

get_all_clients()
get_all_deliveries()


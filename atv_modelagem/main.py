from Controller.ClientController import ClientController
from Controller.DeliveryController import DeliveryController
from Models.ClientModel import ClientModel
from Models.DeliveryModel import DeliveryModel

def create_client(client):
    client_controller = ClientController()
    client_controller.create(client)
    print("Client created successfully!")

def create_delivery(client, delivery):
    client = ClientModel.get_by_email(client.email)
    delivery.client = client
    delivery.client_id = client.id
    delivery_controller = DeliveryController()
    delivery_controller.create(delivery)
    print("Delivery created successfully!")

client = ClientModel(
        name="John Doe",
        email="teste@teste.com",
        phone="999999999",
        address="Rua teste, 123"
    )
create_client(client)

delivery= DeliveryModel(
        product="Product Test",
        quantity=10,
        status="pending"
    )
create_delivery(client, delivery)
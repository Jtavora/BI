from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from Controller.ClientController import ClientController
from Controller.DeliveryController import DeliveryController
from Models.ClientModel import ClientModel
from Models.DeliveryModel import DeliveryModel

app = FastAPI()

client_controller = ClientController()
delivery_controller = DeliveryController()

class Client(BaseModel):
    name: str
    email: str
    phone: str
    address: str

class Delivery(BaseModel):
    client_email: str
    product: str
    quantity: int
    status: str

@app.get("/")
def return_status():
    return {"message": "Welcome to the API!"}

@app.post("/client")
def create_client(client: Client):
    client_data = ClientModel(**client.dict())
    client_controller.create(client_data)
    return {"Client created successfully!"}

@app.post("/delivery")
def create_delivery(delivery: Delivery):
    client = client_controller.get_by_email(delivery.client_email)
    if client is None:
        return {"message": "Client not found!"}
    delivery_data = DeliveryModel(product=delivery.product, quantity=delivery.quantity, status=delivery.status, clients=[client])
    delivery_controller.create(delivery_data)
    return {"Delivery created successfully!"}

@app.get("/clients")
def get_all_clients():
    clients = client_controller.get_all()
    return {"clients": [client.to_dict() for client in clients]}

@app.get("/deliveries")
def get_all_deliveries():
    deliveries = delivery_controller.get_all()
    return {"deliveries": [delivery.to_dict() for delivery in deliveries]}

uvicorn.run(app, host="localhost", port=8000)
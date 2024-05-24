from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Controller.ClientController import ClientController
from Controller.DeliveryController import DeliveryController
from Models.ClientModel import ClientModel
from Models.DeliveryModel import DeliveryModel

import uvicorn

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

@app.get("/", tags=["Root"])
def return_status():
    """Retorna uma mensagem de boas-vindas."""
    return {"message": "Welcome to the API!"}

@app.post("/client", tags=["Clients"])
def create_client(client: Client):
    """Cria um novo cliente."""
    client_data = ClientModel(**client.dict())
    client_controller.create(client_data)
    return {"message": "Client created successfully!"}

@app.post("/delivery", tags=["Delivery"])
def create_delivery(delivery: Delivery):
    """Cria uma nova entrega."""
    client = client_controller.get_by_email(delivery.client_email)
    if client is None:
        raise HTTPException(status_code=404, detail="Client not found!")
    delivery_data = DeliveryModel(product=delivery.product, quantity=delivery.quantity, status=delivery.status, clients=[client])
    delivery_controller.create(delivery_data)
    return {"message": "Delivery created successfully!"}

@app.get("/clients", tags=["Clients"])
def get_all_clients():
    """Obtém todos os clientes."""
    clients = client_controller.get_all()
    return {"clients": [client.to_dict() for client in clients]}

@app.get("/deliveries", tags=["Delivery"])
def get_all_deliveries():
    """Obtém todas as entregas."""
    deliveries = delivery_controller.get_all()
    return {"deliveries": [delivery.to_dict() for delivery in deliveries]}


uvicorn.run(app, host="localhost", port=8000)
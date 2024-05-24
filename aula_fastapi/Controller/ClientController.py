from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.ClientModel import ClientModel
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')

class ClientController:
    def __init__(self):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_by_id(self, id):
        with self.Session() as session:
            client = ClientModel.get_by_id(session, id)
        return client
    
    def get_all(self):
        with self.Session() as session:
            clients = ClientModel.get_all(session)
        return clients
    
    def create(self, client):
        with self.Session() as session:
            ClientModel.create(session, client)
    
    def update(self, client):
        with self.Session() as session:
            ClientModel.update(session, client)
    
    def get_by_email(self, email):
        with self.Session() as session:
            client = ClientModel.get_by_email(session, email)
        if client is None:
            return None
        return client
            
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Models.DeliveryModel import DeliveryModel
from dotenv import load_dotenv
import os

load_dotenv()

database_url = os.getenv('DATABASE_URL')

class DeliveryController:
    def __init__(self):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)
    
    def get_by_id(self, id):
        with self.Session() as session:
            delivery = DeliveryModel.get_by_id(session, id)
        return delivery
    
    def get_all(self):
        with self.Session() as session:
            deliveries = DeliveryModel.get_all(session)
        return deliveries
    
    def create(self, delivery):
        with self.Session() as session:
            DeliveryModel.create(session, delivery)
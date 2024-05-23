from sqlalchemy.orm import relationship
from sqlalchemy import *
import uuid
from datetime import datetime
from Models.Base import Base
from Models.ClientModel import client_delivery_association

def generate_uuid():
    return str(uuid.uuid4())

class DeliveryModel(Base):
    __tablename__ = "deliveries"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    product = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    clients = relationship("ClientModel", secondary=client_delivery_association, back_populates="deliveries")

    def to_dict(self):
        return {
            "id": self.id,
            "product": self.product,
            "quantity": self.quantity,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
    
    @staticmethod
    def get_by_id(session, id):
        return session.query(DeliveryModel).filter(DeliveryModel.id == id).first()
    
    @staticmethod
    def get_all(session):
        return session.query(DeliveryModel).all()
    
    @staticmethod
    def create(session, delivery):
        with session.begin():
            session.add(delivery)
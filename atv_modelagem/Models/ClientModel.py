from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import *
import uuid
from datetime import datetime

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class ClientModel(Base):
    __tablename__ = "clients"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    phone = Column(String(20), nullable=False)
    address = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    delivery = relationship("DeliveryModel", back_populates="client")

    def __repr__(self):
        return f"<ClientModel(id={self.id}, name={self.name}, email={self.email}, phone={self.phone}, address={self.address}, created_at={self.created_at}, updated_at={self.updated_at})>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "address": self.address,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @staticmethod
    def get_by_id(session, id):
        return session.query(ClientModel).filter(ClientModel.id == id).first()
    
    @staticmethod
    def get_all(session):
        return session.query(ClientModel).all()
    
    @staticmethod
    def create(session, client):
        session.add(client)
        session.commit()
    
    @staticmethod
    def update(session, client):
        session.add(client)
        session.commit()

    @staticmethod
    def get_by_email(session, email):
        return session.query(ClientModel).filter(ClientModel.email == email).first()
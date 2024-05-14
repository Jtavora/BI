from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import *
import uuid
from datetime import datetime

Base = declarative_base()

def generate_uuid():
    return str(uuid.uuid4())

class DeliveryModel(Base):
    __tablename__ = "deliveries"

    id = Column(String(36), primary_key=True, default=generate_uuid)
    product = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    client_id = Column(String(36), ForeignKey("clients.id"), nullable=False)
    status = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    client = relationship("ClientModel", back_populates="delivery")

    def __repr__(self):
        return f"<DeliveryModel(id={self.id}, client_id={self.client_id}, status={self.status}, created_at={self.created_at}, updated_at={self.updated_at})>"

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @staticmethod
    def get_by_id(session, id):
        return session.query(DeliveryModel).filter(DeliveryModel.id == id).first()
    
    @staticmethod
    def get_all(session):
        return session.query(DeliveryModel).all()
    
    @staticmethod
    def create(session, delivery):
        session.add(delivery)
        session.commit()

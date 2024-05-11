from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_models.models import User

# Create a connection to the database
e = create_engine('postgresql://postgres:123@localhost:5432/postgres', echo=True)

# Create a session
session = sessionmaker(bind=e)

# Create a new user
def add_user(name, email):
    s = session()
    s.add(User(name=name, email=email))
    s.commit()
    s.close()


add_user("John Doe", "jhon@jhon.com")
from .db import engine, Base
from .models import Sensordata

def init_db():
    Base.metadata.create_all(bind=engine)
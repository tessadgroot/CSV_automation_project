from database.db import Session
import pandas as pd
from sqlalchemy import Column, Integer, String, Text, DateTime, Float
from datetime import datetime
from .db import Base

# Creating the table with columns
class Sensordata(Base):
    __tablename__ = 'sensordata'
  
    sensor_id = Column(Integer, primary_key=True)
    value = Column(Float)
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

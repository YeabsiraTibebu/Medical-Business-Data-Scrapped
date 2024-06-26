# models.py
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DetectionResult(Base):
    __tablename__ = 'detection_results'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    image_id = Column(String, index=True)
    x_min = Column(Float)
    y_min = Column(Float)
    x_max = Column(Float)
    y_max = Column(Float)
    confidence = Column(Float)
    class_id = Column(Integer)
    class_name = Column(String, index=True)
    timestamp = Column(TIMESTAMP)

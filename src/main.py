from typing import Union
from . import crud, models, schemas, database
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://user:pass@localhost:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()




models.Base.metadata.create_all(bind = database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/detection_data/", response_model=schemas.DetectionData)
def create_detection_data(detection_data: schemas.DetectionDataCreate, db: Session = Depends(get_db)):
    return crud.creat_detection_data(db=db, detection_data=detection_data)


@app.get("/detection_data/", response_model=list[schemas.DetectionData])
def read_detection_date(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    detection_data =  crud.get_detection_data(db, skip=skip, limit=limit)    
    return  detection_data
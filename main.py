from fastapi import FastAPI

from database import Base, engine
from routers.medications import router as medication_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Medication Adherence API working 🚀"}


app.include_router(medication_router)
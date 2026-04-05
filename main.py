from fastapi import FastAPI

from database import Base, engine
from routers.auth import router as auth_router
from routers.medications import router as medication_router

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "NEW VERSION RUNNING"}


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(medication_router, tags=["Medications"])
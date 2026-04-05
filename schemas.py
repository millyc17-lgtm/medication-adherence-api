from pydantic import BaseModel, EmailStr


class MedicationCreate(BaseModel):
    name: str
    dosage: str


class MedicationUpdate(BaseModel):
    name: str
    dosage: str


class MedicationResponse(BaseModel):
    id: int
    name: str
    dosage: str


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str
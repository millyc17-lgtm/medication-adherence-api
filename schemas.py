from pydantic import BaseModel


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
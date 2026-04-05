from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from auth1 import get_current_user, get_db, oauth2_scheme
from models import Medication
from schemas import MedicationCreate, MedicationUpdate

router = APIRouter(
    dependencies=[Depends(get_current_user)]
)


@router.post("/medications")
def add_medication(
    med: MedicationCreate,
    db: Session = Depends(get_db)
):
    new_med = Medication(
        name=med.name,
        dosage=med.dosage
    )
    db.add(new_med)
    db.commit()
    db.refresh(new_med)

    return {
        "message": "Medication added",
        "data": {
            "id": new_med.id,
            "name": new_med.name,
            "dosage": new_med.dosage
        }
    }


@router.get("/medications")
def get_medications(
    db: Session = Depends(get_db)
):
    meds = db.query(Medication).all()

    return {
        "medications": [
            {
                "id": med.id,
                "name": med.name,
                "dosage": med.dosage
            }
            for med in meds
        ]
    }


@router.delete("/medications/{medication_id}")
def delete_medication(
    medication_id: int,
    db: Session = Depends(get_db)
):
    med = db.query(Medication).filter(Medication.id == medication_id).first()

    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")

    db.delete(med)
    db.commit()

    return {"message": f"Medication {medication_id} deleted successfully"}


@router.put("/medications/{medication_id}")
def update_medication(
    medication_id: int,
    updated_med: MedicationUpdate,
    db: Session = Depends(get_db)
):
    med = db.query(Medication).filter(Medication.id == medication_id).first()

    if not med:
        raise HTTPException(status_code=404, detail="Medication not found")

    med.name = updated_med.name
    med.dosage = updated_med.dosage

    db.commit()
    db.refresh(med)

    return {
        "message": f"Medication {medication_id} updated successfully",
        "data": {
            "id": med.id,
            "name": med.name,
            "dosage": med.dosage
        }
    }
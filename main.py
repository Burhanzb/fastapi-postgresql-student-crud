from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Student
from schemas import StudentCreate

app = FastAPI()


# Database session
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# CREATE student
@app.post("/students")
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):

    new_student = Student(
        name=student.name,
        age=student.age
    )

    db.add(new_student)

    db.commit()

    db.refresh(new_student)

    return new_student
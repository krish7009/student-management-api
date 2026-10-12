from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    course: str
    age: int 
    


class StudentUpdate(BaseModel):
    name: str | None = None
    course: str | None = None
    age: int | None = None


app = FastAPI(title="Student Management API")
students=[]

@app.get("/")
def home():
    return {"message": "This is a home page. API running"}

@app.get("/students")
def get_students():
    return students

@app.get("/students/{student_id}")
def get_students(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
        
    raise HTTPException(
        status_code=404, 
        detail="student not found"
        )

@app.post("/students")
def add_students(student: StudentCreate):
    new_student = student.model_dump()
    new_student["id"] = len(students)+1
    
    

    students.append(new_student)
    return{
        "message": "student created successfully",
        "student": new_student
    }

@app.patch("/students/{student_id}")
def update_student(student_id: int, update: StudentUpdate):
    for student in students:
        if student["id"] == student_id:
            changes = update.model_dump(exclude_unset=True)
            student.update(changes)
            return student

    raise HTTPException(status_code=404, detail="Student not found" )

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index,student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)
            return {"message": "Student deleted successfull",
                    "student": deleted_student
                    }

    raise HTTPException(
        status_code=404,
        detail="student not found"
    )


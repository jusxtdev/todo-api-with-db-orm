from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.task import Task
from app.schemas.tasks import TaskCreate, TaskResponse, TaskUpdate
from app.utils import raise_error_404

router = APIRouter(
    prefix='/tasks',
    tags=['Tasks']
)

@router.get('/', response_model=list[TaskResponse], status_code=status.HTTP_200_OK)
def all_tasks(db : Session = Depends(get_db)):
    all_tasks = db.query(Task).all()
    return all_tasks

@router.get('/{task_id}', response_model=TaskResponse, status_code=status.HTTP_200_OK)
def task_by_id(task_id : int, db : Session = Depends(get_db)):
    requested_task = db.query(Task).where(Task.task_id == task_id).first()

    raise_error_404(requested_task, task_id)

    return requested_task

@router.post('/', response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def add_task(new_task_data : TaskCreate, db : Session = Depends(get_db)):
    new_task = Task(title = new_task_data.title, due_date = new_task_data.due_date)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.delete('/{task_id}', response_model=TaskResponse, status_code=status.HTTP_200_OK)
def delete_task(task_id : int, db : Session = Depends(get_db)):
    requested_task = db.query(Task).where(Task.task_id == task_id).first()

    raise_error_404(requested_task, requested_id=task_id)

    db.delete(requested_task)
    db.commit()
    return requested_task

@router.put('/{task_id}', response_model=TaskResponse, status_code=status.HTTP_202_ACCEPTED)
def update_task(task_id : int, task_data :TaskUpdate, db : Session = Depends(get_db)):
    existing_data = db.query(Task).where(Task.task_id == task_id).first()

    raise_error_404(existing_data, task_id)

    update_data = task_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(existing_data, key, value)

    db.commit()
    db.refresh(existing_data)
    return existing_data
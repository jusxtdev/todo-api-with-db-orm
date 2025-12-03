from pydantic import BaseModel

from datetime import date, datetime

class TaskCreate(BaseModel):
    title : str
    due_date : date

class TaskUpdate(BaseModel):
    title : str | None = None
    is_done : bool | None = None
    due_date : date | None = None

class TaskResponse(BaseModel):
    task_id : int
    title : str
    is_done : bool
    due_date : date
    create_at : datetime
    update_at : datetime

    class Config:
        from_attributes = True
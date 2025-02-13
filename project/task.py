from datetime import datetime
from enum import Enum

class Status(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"

class Task:
    def __init__(self, id: str, description: str):
        self.id: str = id
        self.description: str = description
        self.status: Status = Status.TODO
        self.createdAt: datetime = datetime.now()
        self.updatedAt: datetime = datetime.now()
        datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": str(self.id),
            "description": str(self.description),
            "status": str(self.status),
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat()
        }
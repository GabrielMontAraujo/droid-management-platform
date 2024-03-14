from pydantic import BaseModel


class Droid(BaseModel):
    model: str
    type: str
    job: str
    status: str
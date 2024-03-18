from pydantic import BaseModel


class UserInput(BaseModel):
    name: str
    lastname: str


class PostCreation(BaseModel):
    auth_id: int
    header: str
    body: str

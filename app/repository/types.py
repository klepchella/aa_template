from pydantic import BaseModel


class ParrotUser(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        from_attributes = True
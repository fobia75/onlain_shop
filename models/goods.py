from pydantic import BaseModel, Field


class Goods(BaseModel):
    id: int
    name: str
    description: str = Field(title="Description",max_length = 1000)
    price: float


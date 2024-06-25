import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, Field


class Order_status(Enum):
    not_in_stock = 2
    available_in_stock = 1




class Orders(BaseModel):
    id: int
    user_id: int
    goods_id: str
    order_date: datetime
    order_status: list[Order_status] 
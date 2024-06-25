import random
from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from db import users, database, goods, orders
from models.users import User, UserIn
from models.goods import Goods
from models.orders import Orders


router = APIRouter()

# добавляем фейковых юзеров
@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(user_name=f'user{i}',email=f'mail{i}@mail.ru', password= f'password{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


# добавляем фейковые товары 
@router.get("/fake_goods/{count}")
async def create_goods(count: int):
    for i in range(count):
        query = goods.insert().values(name=f'name{i}', description=f'{*(random.choice("qwer tyy") for _ in range(400))}', price = f'{i * random.randint(1, 40)}')
        await database.execute(query)
    return {'message': f'{count} fake goods create'}


# добавляем фейковые заказы
@router.get("/fake_orders/{count}")
async def create_orders(count: int):
    for i in range(count):
        query = orders.insert().values(user_id= i)
        await database.execute(query)
    return {'message': f'{count} fake orders create'}


# создание юзера
@router.post("/users/", response_model=User)
async def create_user(user: UserIn):
    query = users.insert().values(user_name=user.user_name, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


# создание товара
@router.post("/goods/", response_model=Goods)
async def create_goods(good: Goods):
    query = users.insert().values(name= goods.name, description = goods.description, price= goods.price)
    last_record_id = await database.execute(query)
    return {**goods.dict(), "id": last_record_id}


# создание заказа
@router.post("/orders/", response_model= Orders)
async def create_orders(oreder: Orders):
    query = orders.insert().values(user_id= users.id, goods_id = goods.id, order_date = orders.order_date, order_status= orders.order_status)
    last_record_id = await database.execute(query)
    return {**orders.dict(), "id": last_record_id}


# чтение всех юзеров
@router.get("/users/", response_model=list[User])
async def read_users():
    query = select(users.c.id, users.c.user_name, users.c.email)
    return await database.fetch_all(query)


# чтение всего товара
@router.get("/goods/", response_model=list[Goods])
async def read_goods():
    query = select(goods.c.id, users.c.name, users.c.description)
    return await database.fetch_all(query)


# чтение всех заказов
@router.get("/orders/", response_model=list[Orders])
async def read_orders():
    query = select(orders.c.id, orders.c.user_id, orders.c.goods_id, orders.c.order_date, orders.c.order_status)
    return await database.fetch_all(query)


# просмотр одного юзера
@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    if not query:
        raise HTTPException(status_code= 404, detail='User not found')
    return await database.fetch_one(query)


# просмотр одного товара
@router.get("/goods/{good_id}", response_model= Goods)
async def read_good(good_id: int):
    query = goods.select().where(goods.c.id == good_id)
    if not query:
        raise HTTPException(status_code= 404, detail='goods not found')
    return await database.fetch_one(query)


# просмотр одного заказа
@router.get("/orders/{order_id}", response_model= Orders)
async def read_order(order_id: int):
    query = orders.select().where(orders.c.id == order_id)
    if not query:
        raise HTTPException(status_code= 404, detail='order not found')
    return await database.fetch_one(query)

# удаление юзера
@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}


# удаление товара
@router.delete("/goods/{good_id}")
async def delete_good(good_id: int):
    query = goods.delete().where(goods.c.id == good_id)
    await database.execute(query)
    return {'message': 'Good deleted'}


# удаление заказа
@router.delete("/orders/{order_id}")
async def delete_order(order_id: int):
    query = orders.delete().where(orders.c.id == order_id)
    await database.execute(query)
    return {'message': 'Orders deleted'}
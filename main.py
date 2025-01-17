from fastapi import FastAPI
import uvicorn
import models.users
from routers.user import router
from db import database


app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()


app.include_router(router, tags=['users'])  


if __name__ == '__main__':
    uvicorn.run("__main__:app", host="127.0.0.1", port=8000, reload=True)
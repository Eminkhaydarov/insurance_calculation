from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from routers import router
from settings import DATABASE_CONFIG

app = FastAPI()

app.include_router(router)
register_tortoise(app=app, config=DATABASE_CONFIG)

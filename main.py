from fastapi import FastAPI
from routes.user import consultas

app = FastAPI()

app.include_router(consultas)
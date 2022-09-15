from sqlite3 import connect
from venv import create
from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://u653914786_henrypi123:Administrador1@45.132.157.154:3306/u653914786_henrypi")
meta = MetaData()

conn = engine.connect()
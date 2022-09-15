from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import circuits, constructors, drivers, pit_stops, races, results, consulta1, consulta2, consulta3, consulta4
from schemas.user import Circuits1, Constructor1, Drivers1, Pit_Stops1, Races1, Results1, Consul1, Consul2, Consul3, Consul4


consultas = APIRouter()

@consultas.get("/pregunta2")
def get_users():
    bart2 = conn.execute(consulta2.select()).fetchall()
    return bart2

@consultas.get("/pregunta3")
def get_users():
    bart3 = conn.execute(consulta3.select()).fetchall()
    return bart3

@consultas.get("/pregunta4")
def get_users():
    bart4 = conn.execute(consulta4.select()).fetchall()
    return bart4

@consultas.get("/pregunta1")
def get_users():
    print("Lewis Hamilton 95 veces")
    bart1 = conn.execute(consulta1.select()).fetchall()
    return bart1


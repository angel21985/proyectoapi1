from cgitb import text
from email.policy import strict
import string
from tokenize import Double
from typing import Text
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Float
from config.db import meta


circuits = Table("circuits_a", meta, 
    Column("circuitId", Integer, primary_key=True), 
    Column("circuitRef", String(255)), 
    Column("name", String(255)), 
    Column("location", String(255)),
    Column("country", String(255)),
    Column("Lat", String(255)),
    Column("Ing", String(255)),
    Column("alt", Integer))

constructors = Table("constructors_a", meta,
    Column("constructorId", Integer, primary_key=True),
    Column("constructorRef", Integer),
    Column("name", String(255)),
    Column("nationality", String(255)))

drivers = Table("drivers_a", meta,
    Column("driverId", Integer, primary_key=True),
    Column("driverRef", String(255)),
    Column("number", String(255)),
    Column("code", String(255)),
    Column("dob", String(255)),
    Column("nationality", String(255)),
    Column("forename", String(255)),
    Column("surname", String(255)))

pit_stops = Table("pit_stops_a", meta,
    Column("raceId", Integer, primary_key=True),
    Column("driverId", String(255)),
    Column("stop", String(255)),
    Column("lap", String(255)),
    Column("time", String(255)),
    Column("duration", String(255)),
    Column("milliseconds", String(255)))

races = Table("races_a", meta, 
    Column("raceId", Integer, primary_key=True), 
    Column("year", Integer), 
    Column("round", Integer), 
    Column("circuitId", Integer),
    Column("name", String(255)),
    Column("date", Float),
    Column("time", String(255)),
    Column("url", String(255)))

results = Table("results_a", meta, 
    Column("resultsId", Integer, primary_key=True), 
    Column("raceId", String(255)), 
    Column("driverId", String(255)), 
    Column("circuitId", String(255)),
    Column("number", String(255)),
    Column("grid", Float),
    Column("position", String(255)),
    Column("points", String(255)),
    Column("laps", Integer),
    Column("time", String(255)),
    Column("milliseconds", String(255)),
    Column("fastestLap", String(255)),
    Column("rank", String(255)),
    Column("fastestLapTime", String(255)),
    Column("fastestLapSpeed", String(255)),
    Column("statusId", String(255)))

consulta1 = Table("consulta1", meta,
    Column("driverReg", String(255)),
    Column("cuenta", Integer),
    Column("position", Integer))

consulta2 = Table("consulta2", meta,
    Column("nombre", String(255)),
    Column("cuenta", Integer),
    Column("nationality", String(255)))

consulta3 = Table("consulta3", meta,
    Column("year", Integer),
    Column("maximo", Integer))

consulta4 = Table("consulta4", meta,
    Column("name", String(255)),
    Column("cuenta", Integer))



    
    # todas las tablas con sus columnas
#conection a la bd


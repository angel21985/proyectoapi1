from cgitb import text
from pydantic import BaseModel
from typing import Optional




class Circuits1(BaseModel):
    circuitId: int
    circuitRef: int
    name: str
    nationality: str

class Constructor1(BaseModel):
    constructorId: int
    constructorRef: int
    name: str
    nationality: str

class Drivers1(BaseModel):
    driverId: int
    driverRef: str
    number: str
    code: str
    dob: str
    nationality: str
    forename: str
    surname: str

class Pit_Stops1(BaseModel):
    raceId: int
    driverId: str
    stop: str
    lap: str
    time: str
    duration: str
    milliseconds: str

class Races1(BaseModel):
    raceId: int
    year: str
    round: str
    circuitId: str
    name: str
    date: float
    time: str
    url: str
    
class Results1(BaseModel):
    resultsId: int
    raceId: str
    driverid: str
    circuitId: str
    number: str
    grid: float
    position: str
    points: str
    laps: int
    time: str
    milliseconds: str
    fastestLap: str
    rank: str
    fastestLapTime: str
    fastestLapSpeed: str
    statusid: str

class Consul1(BaseModel):
    driverReg: str
    cuenta: int
    position: int

class Consul2(BaseModel):
    nombre: str
    cuenta: int
    nationality: str

class Consul3(BaseModel):
    year: int
    maximo: int

class Consul4(BaseModel):
    name: str
    cuenta: int
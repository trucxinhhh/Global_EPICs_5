from pydantic import BaseModel

class User(BaseModel):
    Voltage: float
    Current: float
    Power: float
    Frequency:float 
    PF:float 

class Data(BaseModel): 
    BT1: int
    BT2: int
    BT3: int
    
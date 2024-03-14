from fastapi import FastAPI
from droids import Droid

app = FastAPI()

droids = {
    1: {"model": "HBA", "type": "happy", "job": "analist", "status": "active"},
    2:{"model": "HBO", "type": "obedient", "job": "guard", "status": "active"},
    3:{"model": "HBX", "type": "drunk", "job": "barman", "status": "active"},
}

@app.get("/")
def home():
    return droids 

@app.get("/droids/{id_droid}")
def list_droid(id_droid: int):
    if id_droid in droids:
        return droids[id_droid]
    else:
        return "this droid doesn't exist"


@app.post("/droids/")
def create_droid(droid: Droid):  
    new_id = max(droids.keys()) + 1
    droids[new_id] = droid.dict()  
    return {"message": "Droid created successfully", "droid_id": new_id}


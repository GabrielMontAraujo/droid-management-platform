from fastapi import FastAPI

app = FastAPI()

robots = {
    1: {"name": "HBA", "type": "happy"},
    2:{"name": "HBO", "type": "obedient"},
    3:{"name": "HBX", "type": "drunk"},
}

@app.get("/")
def home():
    return robots 

@app.get("/robots/{id_robot}")
def list_robot(id_robot: int):
    if id_robot in robots:
        return robots[id_robot]
    else:
        return "this robot doesn't exist"
    
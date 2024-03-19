from fastapi import FastAPI, HTTPException, status
from droids import Droid

app = FastAPI()

droids = {
    1: {"model": "HBA", "type": "happy", "job": "analist", "status": "active"},
    2: {"model": "HBO", "type": "obedient", "job": "guard", "status": "active"},
    3: {"model": "HBX", "type": "drunk", "job": "barman", "status": "active"},
}

@app.get("/")
def home():
    return droids, status.HTTP_200_OK 

@app.get("/droids/{id_droid}")
def list_droid(id_droid: int):
    if id_droid in droids:
        return droids[id_droid]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Droid not found")
    
    


@app.post("/droids/")
def create_droid(droid: Droid):  
    new_id = max(droids.keys()) + 1
    droids[new_id] = droid.dict()  
    return {"message": "Droid created successfully", "droid_id": new_id}, status.HTTP_201_CREATED



@app.put("/droids/{id_droid}")
def update_droid(id_droid: int, droid: Droid):
    if id_droid in droids:
        droids[id_droid] = droid.dict()
        return {"message": f"Droid with ID {id_droid} updated successfully"}, status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Droid not found")
    
@app.delete("/droids/{id_droid}")
def delete_droid(id_droid: int):
    if id_droid in droids:
        del droids[id_droid]
        return {"message": f"Droid with ID {id_droid} deleted successfully"}, status.HTTP_200_OK
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Droid not found")


# Lidar com outros status codes

@app.exception_handler(400)
async def bad_request_handler(request, exc):
    return {"error": "Bad Request"}, 400

@app.exception_handler(401)
async def unauthorized_handler(request, exc):
    return {"error": "Unauthorized"}, 401

@app.exception_handler(403)
async def forbidden_handler(request, exc):
    return {"error": "Forbidden"}, 403

@app.exception_handler(500)
async def internal_server_error_handler(request, exc):
    return {"error": "Internal Server Error"}, 500


app.exception_handler(400)
async def bad_request_handler(request, exc):
    return {"error": "Bad Request"}, status.HTTP_400_BAD_REQUEST

@app.exception_handler(401)
async def unauthorized_handler(request, exc):
    return {"error": "Unauthorized"}, status.HTTP_401_UNAUTHORIZED

@app.exception_handler(403)
async def forbidden_handler(request, exc):
    return {"error": "Forbidden"}, status.HTTP_403_FORBIDDEN

@app.exception_handler(500)
async def internal_server_error_handler(request, exc):
    return {"error": "Internal Server Error"}, status.HTTP_500_INTERNAL_SERVER_ERROR


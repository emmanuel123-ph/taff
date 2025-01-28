from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()
# @app.get("/")
# def read_root():
#     return {"message": "Bienvenue sur FastAPI !"}
@app.get("/bienvenue dans mon fastAPI/{item_id}")
# Déclare une route GET pour récupérer un élément spécifique en fonction de son ID.
def read_item(item_id: int):
# La fonction prend en paramètre `item_id`, unbg entier fourni dans l'URL.
    return {"item_id": item_id}
# Retourne une réponse JSON contenant l'ID de l'élément

class User (BaseModel):
    username:str
    email:str
    phone_number:str
    date_added:datetime

class UserCreate (User):
    pass

@app.post("/users")
def create_users (user:User):
    return {"username":user.username, "email":user.email,"phone_number":user.phone_number, "date_added": user.date_added}
    
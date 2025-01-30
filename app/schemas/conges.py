from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional



class  congesBase(BaseModel):
     start_date:datetime
     total_duration:int
     comment:str
     end_date:datetime


class CongesCreate(congesBase):
     pass 

class CongesUpdate(BaseModel):
    uuid:str
    start_date:Optional[str]
    total_duration:Optional[str]
    comment:Optional[str]
    end_date:Optional[datetime]


#pour supprimer plusieur utilisateurs au choix
class CongesDeleteList(BaseModel):
    uuid:list[str]


class CongesResponse(BaseModel):
    uuid:str
    start_date:datetime
    total_duration:int
    comment:str
    end_date:datetime
    status :str
    is_active:bool
    created_at:datetime
    updated_at:datetime
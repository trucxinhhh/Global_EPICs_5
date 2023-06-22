from fastapi import APIRouter
from models.user import User , Data
from config.db import conn ,get,send
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter() 

@user.post('/send')
async def create_send_data(user: Data):
    conn.local.data.insert_one(dict(user))
    return serializeList(conn.local.data.find())
    
@user.post('/post')
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return get()

@user.put('/{id}')
async def update_user(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,user: User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))
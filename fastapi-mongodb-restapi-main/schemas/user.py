# # Normal way
# def userEntity(item) -> dict:
#     return {
#         "id":str(item["_id"]),
#         "Voltage":item["Voltage"],
#         "Current":item["Current"],
#         "Power":item["Power"],
#         "Frequency":item["Frequency"],
#         "PF":item["PF"]
#     }
# def DataEntity(item) -> dict:
#     return {
#         "id":str(item["_id"]),
#         "BT1":item["BT1"],
#         "BT2":item["BT2"],
#         "BT3":item["BT3"]
#     }



# def usersEntity(entity) -> list:
#     return [userEntity(item) for item in entity]

# def DataEntity(entity) -> list:
#     return [DataEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}
def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]


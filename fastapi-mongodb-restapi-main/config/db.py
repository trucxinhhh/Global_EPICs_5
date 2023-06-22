from pymongo import MongoClient
import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd 
import time 

mo_hinh = load_model("D:/THI/Global_EPICs_5/Database_server/fastapi-mongodb-restapi-main/New_18")
conn = MongoClient()
mydb = conn["local"]
list=[]
list_1=[]
mycol = mydb["user"]
mycol_1 = mydb["data"]
def get(): 
    
    for x in mycol.find():
        list.append(x)
    df=pd.DataFrame(list)

    X=df.iloc[-1:,1:6]
    Y =(mo_hinh.predict(X))
    check=[]

    Num=[]
    for v in range(0,len(Y)):
        for x in Y[v]:
            Num.append(x)
    c= 0 
    for i in Num:
        c=c+1
        print(c)
        if i <=0.5: 
            check.append(" LED : OFF, CEILING FANS : OFF, FAN : OFF  ")
        elif i > 0.5 and i <=1.5 : 
            check.append(" LED1 : OFF, CEILING FANS : OFF, FAN : ON ")
        elif i > 1.5 and i <=2.5: 
            check.append(" LED : OFF, CEILING FANS : ON, FAN : OFF ")
        elif i >2.5    and i <= 3.5 : 
            check.append(" LED : OFF, CEILING FANS : ON, FAN : ON ")
        elif i > 3.5  and i <= 4.5 : 
            check.append(" LED : ON, CEILING FANS : OFF, FAN : OFF ")
        elif i > 4.5 and i<= 5.5 :
            check.append(" LED : ON, CEILING FANS : OFF, FAN : ON ",X)
        elif i > 5.5 and i<= 6.5 :
            check.append(" LED : ON, CEILING FANS : ON, FAN : OFF ")
        elif i > 6.5 and i<= 7 :
            check.append(" LED : ON, CEILING FANS : ON, FAN : ON ")
        else :
            check.append("DEVICE IS PROBLEM!!!")
    return check[-1],X

def send():
    list_1=[]
    for x in mycol_1.find():
        list_1.append(x)
    df=pd.DataFrame(list_1)
    X1=df.iloc[-1:,1:4]
    print(X1)
    return  X1
send()
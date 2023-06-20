import numpy as np
import pandas as pd
import csv
import time 


import tensorflow as tf
from tensorflow.keras.models import load_model
# import matplotlib.pyplot as plt

data =pd.read_csv("D:/THI/Global_EPICs_5/data/train/Book1.csv")
mo_hinh = load_model("D:/THI/Global_EPICs_5/train/test_1/New_18")
X = (data.iloc[:,1:6].values)
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
        check.append(" LED : OFF, CEILING FANS : OFF, FAN : OFF ")
        # print(i,"1") 
        print(" LED  : OFF, CEILING FANS : OFF, FAN : OFF ")
        time.sleep(0.5)
    elif i > 0.5 and i <=1.5 : 
        check.append(" LED1 : OFF, CEILING FANS : OFF, FAN : ON ")
        # print(i,"2")
        print(" LED : OFF,CEILING FANS : OFF, FAN : ON ")
        time.sleep(0.5)
    elif i > 1.5 and i <=2.5: 
        check.append(" LED : OFF, CEILING FANS : ON, FAN : OFF ")
        # print(i, '3')
        print(" LED 1 : OFF, CEILING FANS : ON, FAN : OFF ")
        time.sleep(0.5)
    elif i >2.5    and i <= 3.5 : 
        check.append(" LED : OFF, CEILING FANS : ON, FAN : ON ")
        # print(i,'4')
        print(" LED : OFF, CEILING FANS: ON, FAN : ON ")
        time.sleep(0.5)
    elif i > 3.5  and i <= 4.5 : 
        check.append(" LED : ON, CEILING FANS : OFF, FAN : OFF ")
        # print(i,'5') 
        print(" LED : ON, CEILING FANS : OFF, FAN : OFF ")
        time.sleep(0.5)
    elif i > 4.5 and i<= 5.5 :
        check.append(" LED : ON, CEILING FANS : OFF, FAN : ON ")
        # print(i,'6')
        print(" LED 1 : ON, CEILING FANS : OFF, FAN : ON ")
        time.sleep(0.5)
    elif i > 5.5 and i<= 6.5 :
        check.append(" LED : ON, CEILING FANS : ON, FAN : OFF ")
        # print(i,'7')
        print(" LED : ON, CEILING FANS: ON, FAN : OFF ")
        time.sleep(0.5)
    elif i > 6.5 and i<= 7 :
        check.append(" LED : ON, CEILING FANS : ON, FAN : ON ")  
        print(" LED : ON, CEILING FANS : ON, FAN : ON ")  
        # print(i,'8')
        time.sleep(0.5)
    else :
         check.append("DEVICE IS PROBLEM!!!")
         print("DEVICE IS PROBLEM !!!")
        #  print(i,'9')
         time.sleep(0.5)

df=pd.DataFrame(check,columns=['relust'])
df['Num']=Num
# df['Voltage']=data['Voltage']
# df['Current']=data['Current']
# df['Power']=data['Power']
# df['Frequency']=data['Frequency']
# df['PF']=data['PF']
# df['LED']=data['LED']  
# df['FAN']=data['FAN']
# df.to_csv('D:/THI/Global_EPICs_5/check/new_book_ok_hu_3.csv')
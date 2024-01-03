import pandas as pd
import numpy as np

df=pd.read_csv("landslide_data_original.csv")
temp=df['temperature'].tolist()
humi=df['humidity'].tolist()
press=df['pressure'].tolist()
rain=df['rain'].tolist()
lavg=df['lightavg'].tolist()
limax=df['lightmax'].tolist()
mois=df['moisture'].tolist()


def mul(l1,l2):
    l3=[]
    for i in range(0,max(len(l1),len(l2))):
        a=l1[i]*l2[i]
        l3.append(a)
    return l3


def crr(para1, para2):
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    mean1 = sum(para1) / len(para1)
    mean2 = sum(para2) / len(para2)
    for i in para1:
        l1.append(i - mean1)
        l3.append((i - mean1) ** 2)
    for j in para2:
        l2.append(j - mean2)
        l4.append((j - mean2) ** 2)

    num = sum(mul(l1, l2))
    sum1 = sum(l3)
    sum2 = sum(l4)
    deno = np.sqrt(sum1 * sum2)
    return round(num / deno, 2)

dict = {'' : ['Temperature', 'Humidity', 'Pressure', 'Rain','Lightavg',"LightMax","Moisture"],
        'Temperature' : [crr(temp,temp),crr(temp,humi),crr(press,temp),crr(rain,temp),crr(lavg,temp),crr(limax,temp),crr(mois,temp)],
        'Humidity' : [crr(humi,temp), crr(humi,humi), crr(humi,press), crr(humi,rain),crr(humi,lavg),crr(humi,limax),crr(humi,mois)],
       'Pressure':[crr(press,temp),crr(press,humi),crr(press,press),crr(press,rain),crr(press,lavg),crr(press,limax),crr(press,mois)],    
       'Rain':[crr(rain,temp),crr(rain,humi),crr(rain,press),crr(rain,rain),crr(rain,lavg),crr(rain,limax),crr(rain,mois)],
       'LightAvg':[crr(lavg,temp),crr(lavg,humi),crr(lavg,press),crr(lavg,rain),crr(lavg,lavg),crr(lavg,limax),crr(lavg,mois)] ,
        'LightMax':[crr(limax,temp),crr(limax,humi),crr(limax,press),crr(limax,rain),crr(limax,lavg),crr(limax,limax),crr(limax,mois)],
       'Moisture':[crr(mois,temp),crr(mois,humi),crr(mois,press),crr(mois,rain),crr(mois,lavg),crr(mois,limax),crr(mois,mois)] 
       }
df1 = pd.DataFrame(dict)
df1=df1.set_index("")
print(df1)
# print()
# print()
# print(f"The redundant attribute w.r.t Light avg is Light Max as it has a strong correlation of {crr(limax,lavg)} .")
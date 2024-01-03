import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("landslide_data_original.csv")
newdf=df['stationid']=='t12'
reqd=df[newdf]['humidity']
bin=np.arange(reqd.min(),reqd.max(),5)

plt.hist(reqd,bins=bin,color='purple')
plt.xticks(bin)
plt.xlabel("Values ----->")
plt.ylabel("Frequency----->")
plt.title("Plot for Humidity For T12")
plt.grid('b')
plt.show()

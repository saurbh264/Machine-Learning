import pandas as pd
import numpy as np
df=pd.read_csv("landslide_data_original.csv")
df2=pd.read_csv("landslide_data_miss.csv")
temp=df['temperature'].tolist()
temp.sort()
temp2=df2['temperature']
print(f"There are {temp2.isnull().sum()} missing values in missing dataset.\n So Dropped Them.")
temp2=temp2.dropna()
temp2=temp2.tolist()
temp2.sort()


#Mean
def sumof(l1):
    s=0
    for i in l1:
        s+=i
    return s
mean1=round((sumof(temp)/len(temp)),2)

mean2=round(sumof(temp2)/len(temp2),2)


#Minimum
def minof(l1):
    min=10000
    for i in l1:
        if i<min:
            min=i
    return min

mini1=round(minof(temp),2)
mini2=round(minof(temp2),2)



#Maximum
def maxof(l1):
    max=-10000
    for i in l1:
        if i>max:
            max=i
    return max

maxi1=round(maxof(temp),2)
maxi2=round(maxof(temp2),2)



#Median

median1=round(temp[int((len(temp)+1)/2)],2)
median2=round(temp2[int((len(temp2)+1)/2)],2)


#Standard Deviation
def stnd(l1,mean):
    sigma = 0
    for i in l1:
        sigma += ((i - mean) ** 2)
    std = np.sqrt(sigma / len(l1))
    return std

std1=round(stnd(temp,mean1),2)
std2=round(stnd(temp2,mean2),2)

#Answers
print(f'The statistical measures of Temperature attribute of Complete Data are:')
print(f"Mean: {mean1}")
print(f"Minimum: {mini1}")
print(f'Maximum: {maxi1}')
print(f"Since the no of terms is {len(temp)} in complete data which is odd.")
print(f"Median: {median1}")
print(f"Standard Deviation: {std1}")

print()
print()

print(f'The statistical measures of Temperature attribute of Incomplete Data are:')
print(f"Mean: {mean2}")
print(f"Minimum: {mini2}")
print(f'Maximum: {maxi2}')
print(f"Since the no of terms is {len(temp2)} in missing data which is odd.")
print(f"Median: {median2}")
print(f"Standard Deviation: {std2}")
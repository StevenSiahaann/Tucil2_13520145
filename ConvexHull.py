import numpy as np 
import pandas as pd
import math
import matplotlib.pyplot as plt 
from sklearn import datasets
import matplotlib.pyplot as plt
def sortByXCoord(points):
    points=sorted(points,key=lambda x:x[0])
    return points
def sortByYCoord(points):
    points=sorted(points,key=lambda x:x[1])
    return points
def jarakTitik(p1,p2):
    return (math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2))
def jarakTitikKeGaris(point,line) :
    line=sortByXCoord(line)
    slope=gradien(line[0],line[1])
    yInt = line[0][1]-(slope*line[0][0]) #mencari konstanta pers garis
    dist= abs(-slope*point[0]+1*point[1]-yInt)/(math.sqrt(1**2+(slope**2)))
    return (dist)
def gradien(point1,point2) :
    if(point2[0]!=point1[0]):
        slope = (point2[1]-point1[1])/(point2[0]-point1[0])
        return slope
    else :
        return False
def sisiTitik(point1,point2,point3):
    det=point1[0]*point2[1]+ point3[0]*point1[1]+point2[0]*point3[1]-point3[0]*point2[1]-point2[0]*point1[1]-point1[0]*point3[1]
    return det 
def upperSide(point1,point2,point3):
    if(sisiTitik(point1, point2, point3)>0.00) :
        return True
    else : 
        return False 
def lowerSide(point1, point2, point3):
    if(sisiTitik(point1, point2, point3)<0.00):
        return True
    else :
        return False
def segaris(point1, point2, point3): 
    if(sisiTitik(point1, point2, point3)==0):
        return True 
    else:
        return False
def LuasSegitiga(point1, point2, point3) :
    if(isTriangle(point1, point2, point3) and segaris(point1, point2, point3) is not True) :
        luas=0
        s=(jarakTitik(point1,point2)+jarakTitik(point2,point3)+jarakTitik(point1, point3))/2
        luas = s*(s-jarakTitik(point1,point2))*(s-jarakTitik(point2,point3))*(s-jarakTitik(point3,point1))
    return math.sqrt(luas) 
def isTriangle(point1, point2, point3) :
    a=jarakTitik(point1, point2)
    b=jarakTitik(point2, point3)
    c= jarakTitik(point1,point3)
    s=[a,b,c]
    s.sort()
    if(segaris(point1, point2, point3) is True):
        return False
    if(segaris(point1, point2, point3) is not True and (s[0]+s[1])>s[2]) :
        return True
    else :
        return False
def isInsideTriangle(point1, point2, point3,point4): #ada di dalam segitiga    
    if(isTriangle(point1, point2, point3) is True):
        s=[point1, point2, point3]
        s=sortByXCoord(s)
        if(sisiTitik(s[0], s[1],point4 )>=0.00 and sisiTitik(s[0], s[2], point4)<=0.00 and sisiTitik(s[1], s[2], point4)>=0.00):
            return True
        else :
            return False
def titik_terjauh(s,point1,point2): #s=kumpulan titik,point1=titik minimumabsis,point2=titik maximum absis
    s=sortByXCoord(s)
    titikTerjauh = s[0]
    patokan=0
    for i in range(0,len(s)):
        if(jarakTitikKeGaris(s[i], [point1, point2])>=patokan):
            patokan=jarakTitikKeGaris(s[i], [point1, point2])
            titikTerjauh=s[i]
    return titikTerjauh
def ConvexHullAlaAla(s) :
    hull=[]
    if s is not list :
      s=s.tolist()
    s=sortByXCoord(s)
    hull.append(s[0])
    hull.append(s[-1])
    s1=[]#kiri/atas
    s2=[]#kanan/bawah
    for z in range(0,len(s)):
        if(s[z]!=s[0] and s[z]!=s[-1]):
            if(lowerSide(s[0], s[-1], s[z])):
                s2.append(s[z]) #sisi kanan/bawah untuk variabel x
            if(upperSide(s[0],s[-1],s[z])>0.00):
                s1.append(s[z]) #sisi kiri/atas untuk variabel x
    findHull(s1,s[0],s[-1],hull)
    findHull(s2,s[-1],s[0],hull)
    return hull
def findHull(sk,p,q,hull):
    sk=sortByXCoord(sk)
    sub_s1=[]#kiri/atas yang bagian kiri harusnya
    sub_s2=[]#kiri/atas yang bagian kanan harusnya
    if(len(sk)==0): return #udh berenti titik s[0] dan s[-1] yg ada di hull jadi convex hull bagian sisi tersebut(s1 atau s2) 
    else :
        a=titik_terjauh(sk,p,q)
        sk.remove(a)
        hull.insert(1,a)
        for j in range(0,len(sk)):
            if(isInsideTriangle(p,q,a,sk[j])==False) :
                if(upperSide(p,a,sk[j] )):
                    (sub_s1).append(sk[j])
                if(upperSide(a,q,sk[j])):
                    (sub_s2).append(sk[j])
    findHull(sub_s1,p,a,hull)
    findHull(sub_s2,a,q,hull)
def splitandMergeHull(hull):
    hull=sortByXCoord(hull)
    upHull=[]
    downHull=[]
    for j in range(1,len(hull)-1):
        if(upperSide(hull[0],hull[-1],hull[j]) is True):
            upHull.append(hull[j])
        if(lowerSide(hull[0],hull[-1],hull[j]) is True):
            downHull.append(hull[j])
    downHull.append(hull[0])
    upHull.append(hull[0])
    downHull.append(hull[-1])
    upHull.append(hull[-1])                           
    upHull=sortByXCoord(upHull)
    downHull=sorted(downHull,reverse=True,key=lambda x:x[0])
    hull=upHull+downHull
    x=getX(hull)
    y=getY(hull)
    hull=[x]+[y]
    return(hull)
def getX(hull) :
    hull_x=[]
    for e in hull :
        hull_x.append(e[0])
    return hull_x
def getY(hull):
    hull_y=[]
    for e in hull :
        hull_y.append(e[1]) 
    return hull_y
def displayConvexHull(df,a,b,hull):
  plt.figure(figsize = (10, 6))
  colors = ['b','r','g','c','m','y','k','w']
  plt.title(data.feature_names[a] + ' vs ' + data.feature_names[b])
  plt.xlabel(data.feature_names[a])
  plt.ylabel(data.feature_names[b])
  for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[a,b]].values
    hull=ConvexHullAlaAla(bucket)
    hull= splitandMergeHull(hull)
    plt.scatter(getX(bucket), getY(bucket), label=data.target_names[i])
    print(hull)
    plt.plot(hull[0],hull[-1],colors[i%8])

  plt.legend()
hull=[]
data = datasets.load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()
displayConvexHull(df,0,1,hull)

import numpy as np 
import pandas as pd
import math
import matplotlib.pyplot as plt 
from sklearn import datasets 
data = datasets.load_iris() 
#create a DataFrame 
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Target'] = pd.DataFrame(data.target) 
print(df.shape)
df.head()
#visualisasi hasil ConvexHull
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title('Petal Width vs Petal Length')
plt.xlabel(data.feature_names[0])
plt.ylabel(data.feature_names[1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[0,1]].values
    hull=[]
    def sortByXCoord(points):
        points=sorted(points,key=lambda x:x[0])
        return points
    def sortByYCoord(points):
        points=sorted(points,key=lambda x:x[1])
        return points
    def jarakTitik(p1,p2):
        return (math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2))
    def jarakTitikKeGaris(point,line) : # q=line=[[],[]]
        line=sortByXCoord(line)
        slope=gradien(line[0],line[1])
        yInt = line[0][1]-(slope*line[0][0]) #mencari konstanta pers garis
        dist= abs(-slope*point[0]+1*point[1]-yInt)/(math.sqrt(1**2+(slope**2)))
        return (dist)
    def gradien(s1,s2) :
        if(s2[0]!=s1[0]):
            slope = (s2[1]-s1[1])/(s2[0]-s1[0])
            return slope
        else :
            return False
    def sisiTitik(s1,s2,z):
        det=s1[0]*s2[1]+ z[0]*s1[1]+s2[0]*z[1]-z[0]*s2[1]-s2[0]*s1[1]-s1[0]*z[1]
        return det 
    def upperSide(s1,s2,z):
        if(sisiTitik(s1, s2, z)>0.00) :
            return True
        else : 
            return False 
    def lowerSide(s1,s2,z):
        if(sisiTitik(s1, s2, z)<0.00):
            return True
        else :
            return False
    def segaris(s1,s2,z): 
        if(sisiTitik(s1, s2, z)==0):
            return True 
        else:
            return False
    def LuasSegitiga(A,B,C) :
        if(isTriangle(A, B, C) and segaris(A, B, C) is not True) :
            luas=0
            s=(jarakTitik(A,B)+jarakTitik(B,C)+jarakTitik(A, C))/2
            luas = s*(s-jarakTitik(A,B))*(s-jarakTitik(B,C))*(s-jarakTitik(C,A))
        return math.sqrt(luas) 
    def isTriangle(A,B,C) :
        a=jarakTitik(A, B)
        b=jarakTitik(B,C)
        c= jarakTitik(A, C)
        s=[a,b,c]
        s.sort()
        if(segaris(A,B,C) is True):
            return False
        if(segaris(A,B,C) is not True and (s[0]+s[1])>s[2]) :
            return True
        else :
            return False
    def isInsideTriangle(A,B,C,p): #ada di dalam segitiga    
        if(isTriangle(A, B, C) is True):
            s=[A,B,C]
            s=sortByXCoord(s)
            if(sisiTitik(s[0], s[1],p )>=0.00 and sisiTitik(s[0], s[2], p)<=0.00 and sisiTitik(s[1], s[2], p)>=0.00):
                return True
            else :
                return False
    def titik_terjauh(s,p,q): #s=kumpulan titik
        s=sortByXCoord(s)
        titikTerjauh = s[0]
        patokan=0
        for i in range(0,len(s)):
            if(sisiTitik(p, q, s[i])>=patokan):
                patokan=sisiTitik(p, q, s[i])
                titikTerjauh=s[i]
        return titikTerjauh
    def ConvexHullAlaAla(s) :
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
        findHull(s1,s[0],s[-1])
        findHull(s2,s[-1],s[0])
    def findHull(sk,p,q):
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
        findHull(sub_s1,p,a)
        findHull(sub_s2,a,q)
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
    ConvexHullAlaAla(bucket)
    hull=splitandMergeHull(hull)
    plt.scatter(getX(bucket), getY(bucket), label=data.target_names[i])
    plt.plot(hull[0],hull[-1],colors[i])
plt.legend()

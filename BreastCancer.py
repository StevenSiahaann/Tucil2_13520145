import numpy as np 
import pandas as pd
import math
import matplotlib.pyplot as plt 
from sklearn import datasets
import matplotlib.pyplot as plt
def sortByXCoord(points):
# Mengurutkan absis dari yang terkecil #
    points=sorted(points,key=lambda x:x[0])
    return points
def sortByYCoord(points):
#Mengurutkan Y dari yang paling kecil #
    points=sorted(points,key=lambda x:x[1])
    return points
def jarakTitik(p1,p2):
# Menghitung jarak titik p1 dan p2 #
    return (math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2))
def jarakTitikKeGaris(point,line) :
# Menghitung jarak titik terhadap garisi #
    line=sortByXCoord(line)
    slope=gradien(line[0],line[1])
    yInt = line[0][1]-(slope*line[0][0]) #mencari konstanta pers garis
    dist= abs(-slope*point[0]+1*point[1]-yInt)/(math.sqrt(1**2+(slope**2)))
    return (dist)
def gradien(point1,point2) :
# Menghitung gradien #
    if(point2[0]!=point1[0]):
        slope = (point2[1]-point1[1])/(point2[0]-point1[0])
        return slope
    else :
        return False
def sisiTitik(point1,point2,point3):
# Menghitung nilai determinan untuk membantu menentukan posisi titik terhadap garis #
    det=point1[0]*point2[1]+ point3[0]*point1[1]+point2[0]*point3[1]-point3[0]*point2[1]-point2[0]*point1[1]-point1[0]*point3[1]
    return det 
def upperSide(point1,point2,point3):
# Memeriksa apakah point 3 terletak dibagian atas garis yang dibentuk point 2 dan point 3 #
    if(sisiTitik(point1, point2, point3)>0.00) :
        return True
    else : 
        return False 
def lowerSide(point1, point2, point3):
# Memeriksa apakah point 3 terletak dibagian bawah garis yang dibentuk point 2 dan point 3 #
    if(sisiTitik(point1, point2, point3)<0.00):
        return True
    else :
        return False
def segaris(point1, point2, point3): 
# Memeriksa apakah point 3 terletak pada garis yang dibentuk point 2 dan point 3 #
    if(sisiTitik(point1, point2, point3)==0):
        return True 
    else:
        return False
def LuasSegitiga(point1, point2, point3) :
# Menghitung luas segitiga yang dibentuk oleh point1,point2,point3 #
    if(isTriangle(point1, point2, point3) and segaris(point1, point2, point3) is not True) :
        luas=0
        s=(jarakTitik(point1,point2)+jarakTitik(point2,point3)+jarakTitik(point1, point3))/2
        luas = s*(s-jarakTitik(point1,point2))*(s-jarakTitik(point2,point3))*(s-jarakTitik(point3,point1))
    return math.sqrt(luas) 
def isTriangle(point1, point2, point3) :
# Memeriksa apakah point1,point2,point3 akan membentuk segitiga #
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
def isInsideTriangle(point1, point2, point3,point4):    
# Memeriksa apakah point4 terletak di dalam segitiga #
    if(isTriangle(point1, point2, point3) is True):
        s=[point1, point2, point3]
        s=sortByXCoord(s)
        if(sisiTitik(s[0], s[1],point4 )>=0.00 and sisiTitik(s[0], s[2], point4)<=0.00 and sisiTitik(s[1], s[2], point4)>=0.00):
            return True
        else :
            return False
def titik_terjauh(s,point1,point2): 
# s=kumpulan titik,point1=titik minimumabsis,point2=titik maximum absis #
# Mencari titik terjauh dari garis yang dibentuk oleh 2 titik #
    s=sortByXCoord(s)
    titikTerjauh = s[0]
    patokan=0
    for i in range(0,len(s)):
        if(jarakTitikKeGaris(s[i], [point1, point2])>=patokan):
            patokan=jarakTitikKeGaris(s[i], [point1, point2])
            titikTerjauh.append(s[i])
    return titikTerjauh[-1]
def firstSecondHull(points):#points=list of points
# Mencari hull pertama dan kedua yang akan membagi himpunan menjadi 2 bagian #
    points=sorted(points)
    palingKanan=[]
    firstSecondHull=[points[0]]
    if(points[-1][0]==points[-2][0]):
        for i in range(len(points)):
            if(points[i][0]==points[-1][0]) :
                palingKanan.append(points[i])
                break
    else :
        palingKanan.append(points[-1])
    firstSecondHull.append(palingKanan[0])
    return(firstSecondHull)
def myConvexHull(s) :
    hull=[]
    if s is not list :
        s=s.tolist()
    first_Second_Hull=firstSecondHull(s)
    hull.append(first_Second_Hull[0])
    hull.append(first_Second_Hull[-1])    
    s1=[]#kiri/atas
    s2=[]#kanan/bawah
# Membagi himpunan menjadi 2 bagian yang dibatasi oleh garis yang dibentuk 2 titik hull pertama yang ditemukan(titik paling kiri dan paling kanan) 
    for z in range(0,len(s)):
        if(s[z]!=first_Second_Hull[0] and s[z]!=first_Second_Hull[-1]):
            if(lowerSide(first_Second_Hull[0], first_Second_Hull[-1], s[z])):
                s2.append(s[z]) #sisi kanan/bawah untuk variabel x
            if(upperSide(first_Second_Hull[0], first_Second_Hull[-1],s[z])>0.00):
                s1.append(s[z]) #sisi kiri/atas untuk variabel x
# Mencari hull dari 2 sub bagian tersebut #
    findHull(s1,first_Second_Hull[0], first_Second_Hull[-1],hull)
    findHull(s2,first_Second_Hull[-1],first_Second_Hull[0],hull)
    return hull
def findHull(sk,p,q,hull):
# Mencari hull dari 2 bagian yang sudah dibuat #
    sk=sortByXCoord(sk)
    sub_s1=[]#kiri/atas yang bagian kiri 
    sub_s2=[]#kiri/atas yang bagian kanan 
    if(len(sk)==0): return  
    else :
# Menemukan hull dengan fungsi titik terjauh #
        a=titik_terjauh(sk,p,q)
        sk.remove(a)
        hull.insert(1,a)
# Membagi kembali menjadi sub bagian yang lebih kecil #
        for j in range(0,len(sk)):
            if(isInsideTriangle(p,q,a,sk[j])==False) :
                if(upperSide(p,a,sk[j] )):
                    (sub_s1).append(sk[j])
                if(upperSide(a,q,sk[j])):
                    (sub_s2).append(sk[j])
# Mencari kembali hull dari sub bagian tersebut #
    findHull(sub_s1,p,a,hull)
    findHull(sub_s2,a,q,hull)
def splitandMergeHull(hull):
# Memecah dan menggabungkan namun secara terurut untuk membantu proses visualisasi #
    first_Second_Hull=firstSecondHull(hull)
    upHull=[]
    downHull=[]
    for j in range(1,len(hull)-1):
        if(upperSide(first_Second_Hull[0],first_Second_Hull[-1],hull[j]) is True):
            upHull.append(hull[j])
        if(lowerSide(first_Second_Hull[0],first_Second_Hull[-1],hull[j]) is True):
            downHull.append(hull[j])
    downHull.append(first_Second_Hull[0])
    upHull.append(first_Second_Hull[0])
    downHull.append(first_Second_Hull[-1])
    upHull.append(first_Second_Hull[-1])                         
    upHull=sorted(upHull)
    downHull=sorted(downHull,reverse=True,key=lambda x:x[0])
    combine=upHull+downHull
    plot=[getX(combine)]+[getY(combine)]
    return(plot)
def getX(hull) :
# Mengambil nilai x dari (x,y) #
    hull_x=[]
    for e in hull :
        hull_x.append(e[0])
    return hull_x
def getY(hull):
# Mengambil nilai y dari (x,y) #
    hull_y=[]
    for e in hull :
        hull_y.append(e[1]) 
    return hull_y
def displayConvexHull(df,a,b,hull):
# Visualisasi Convex Hull dengan pustaka myConvexHull
  plt.figure(figsize = (10, 6))
  colors = ['b','r','g','c','m','y','k','w']
  plt.title(data.feature_names[a] + ' vs ' + data.feature_names[b])
  plt.xlabel(data.feature_names[a])
  plt.ylabel(data.feature_names[b])
  for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[a,b]].values
    hull=myConvexHull(bucket)
    hull= splitandMergeHull(hull)
    print(hull)
    plt.scatter(getX(bucket), getY(bucket), label=data.target_names[i])
    plt.plot(hull[0],hull[-1],colors[i%8])
  plt.legend()
hull=[]
data = datasets.load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['Target'] = pd.DataFrame(data.target)
print(df.shape)
df.head()
displayConvexHull(df,0,1,hull)

import pandas as pd
#import matplotlib.pyplot as plt
from sklearn import tree

#training phase
df = pd.read_csv('new.csv')
df1 = pd.read_csv('new.csv')
df = df[pd.notnull(df['id'])]
df = df.drop(['id','name','sslc','plustwo','ug'],axis='columns')
def trans_pg(x):
    if x>90:
        return 9
    elif x>80:
        return 7
    elif x>70:
          return 5
    elif x>60:
          return 3
    else:
        return 1
def trans_prac(x):
    if x>95:
        return 9
    elif x>90:
        return 7
    elif x>85:
          return 5
    elif x>70:
          return 3
    else:
        return 1   
def trans_attnd(x):
    if x>90:
        return 2
    elif x>80:
        return 1
    else:
        return 0
def choice(x):
    if x=='yes':
        return 1
    else:
        return 0
def neg(x):
    if x=='no':
        return 1
    else:
        return 0
def fail(x):
    if x==0:
        return 5
    if x<3:
        return 3
    elif x<5:
        return 1
    else:
        return 0
def trans_tym(x):
    if x==0:
        return 3
    if x<=3:
        return 2
    elif x<=5:
        return 1
    else:
        return 0
def trans_sub(x):
    list=['bigdata','cryptography','ml','ai','nural network','mining','deep learning']
    for i in list:
        if x==i:
            return 2
    if x=='no':
        return 0
    else:
        return 1
df['pg_cgpa']=df['pg_cgpa'].apply(trans_pg)
df['pg_prac']=df['pg_prac'].apply(trans_prac)
df['attend']=df['attend'].apply(trans_attnd)
df['internal']=df['internal'].apply(trans_pg)
df['like_sub']=df['like_sub'].apply(trans_sub)
df['seminar']=df['seminar'].apply(trans_sub)
df['work_exp']=df['work_exp'].apply(choice)
df['project']=df['project'].apply(trans_sub)
df['alcohol']=df['alcohol'].apply(neg)
df['mob_time']=df['mob_time'].apply(trans_tym)
#df['extra_cert']=df['extra_cert'].apply(choice)
df['fail_no']=df['fail_no'].apply(fail)
df['edu_sup']=df['edu_sup'].apply(choice)
df['score'] = 0
df['score'] =df.sum(axis = 1, skipna = True)
df['final_grade'] = 'na'
df.loc[(df.score >= 60), 'final_grade'] = 'exellent' 
df.loc[(df.score >= 50) & (df.score <= 59), 'final_grade'] = 'good' 
df.loc[(df.score >= 41) & (df.score <= 49), 'final_grade'] = 'fair' 
df.loc[(df.score <= 40), 'final_grade'] = 'poor' 
df1['final_grade'] = 'na'
df1['final_grade']=df['final_grade']

a = pd.DataFrame(df1)
a.to_csv("ori_g.csv",index=False)
b = pd.DataFrame(df)
b.to_csv("pre.csv",index=False)

train = pd.read_csv("pre.csv")
inputs = train.drop(['score','final_grade'],axis='columns')
target = train['final_grade']

#model creation
model = tree.DecisionTreeClassifier()
model.fit(inputs, target)
#model.predict([[69,80,85,5,2,6,5,1,1,3,1,1,2,0,0]])

#prepare data
df2 = pd.read_csv("test.csv")
df2= df2[pd.notnull(df2['id'])]
#un_id=df2['id']
list=["id", "name", "sslc", "plustwo", "ug", "pg_cgpa", "pg_prac", "internal",
       "attend", "like_sub", "seminar", "self_evl", "work_exp", "project",
       "alcohol", "health", "mob_time", "code_evl", "sub_evl", "std_time",
       "fail_no", "edu_sup"]
data=[]
data1=[]
import csv
for i in range(22):
    k=list[i]
    data.append(df2[k])
for i in range(22):
    k=data[i][0]
    data1.append(k)
'''with open('test.csv','a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(data1)
csvFile.close()'''
#tm.showinfo("Message", "Successful")
df2['pg_cgpa']=df2['pg_cgpa'].apply(trans_pg)
df2['pg_prac']=df2['pg_prac'].apply(trans_prac)
df2['attend']=df2['attend'].apply(trans_attnd)
df2['internal']=df2['internal'].apply(trans_pg)
df2['like_sub']=df2['like_sub'].apply(trans_sub)
df2['seminar']=df2['seminar'].apply(trans_sub)
df2['work_exp']=df2['work_exp'].apply(choice)
df2['project']=df2['project'].apply(trans_sub)
df2['alcohol']=df2['alcohol'].apply(neg)
df2['mob_time']=df2['mob_time'].apply(trans_tym)
#df['extra_cert']=df['extra_cert'].apply(choice)
df2['fail_no']=df2['fail_no'].apply(fail)
df2['edu_sup']=df2['edu_sup'].apply(choice)

val=[]
list=["pg_cgpa", "pg_prac", "internal",
       "attend", "like_sub", "seminar", "self_evl", "work_exp", "project",
       "alcohol", "health", "mob_time", "code_evl", "sub_evl", "std_time",
       "fail_no", "edu_sup"]

for i in range(17):
    k=list[i]
    val.append(df2[k])
r=model.predict([[int(val[0]),int(val[1]),int(val[2]),int(val[3]),int(val[4]),
                  int(val[5]),int(val[6]),int(val[7]),int(val[8]),int(val[9]),int(val[10]),int(val[11]),int(val[12]),
                  int(val[13]),int(val[14]),int(val[15]),int(val[16])]])
data1.append(r[0])

with open('ds.csv','a') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(data1)
csvFile.close()

q=pd.DataFrame(df2)
q.drop(0).to_csv("test.csv",index=False)

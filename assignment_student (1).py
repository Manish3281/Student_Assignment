import pandas as pd
import numpy as np



maths = pd.read_excel('Python_Assignment.xlsx',sheet_name='Maths')


phy = pd.read_excel('Python_Assignment.xlsx',sheet_name='Physics')


hindi = pd.read_excel('Python_Assignment.xlsx',sheet_name='Hindi')


eco = pd.read_excel('Python_Assignment.xlsx',sheet_name='Economics')


music = pd.read_excel('Python_Assignment.xlsx',sheet_name='Music')


maths['%maths'] = (((maths['Theory Marks'] + maths['Numerical Marks'] + maths['Practical Marks'])/300)*100).round(2)


maths.drop(['Theory Marks','Numerical Marks','Practical Marks'],axis=1,inplace=True)


print(maths.head())


eco['%eco'] = (((eco['Theory Marks']+eco['Numerical Marks'])/200)*100).round(2)


eco.drop(['Theory Marks','Numerical Marks'],axis=1,inplace=True)


print(eco.head())


hindi['%hindi'] = hindi['Marks'].round(2)
hindi.drop('Marks',axis=1,inplace=True)


print(hindi.head())


music['%music'] = (((music['Theory Marks']+music['Practical Marks'])/200)*100).round(2)
music.drop(['Theory Marks','Practical Marks'],axis=1,inplace=True)


print(music.head())


phy['%phy'] = (((phy['Theory Marks'] + phy['Numerical Marks'] + phy['Practical Marks'])/300)*100).round(2)
phy.drop(['Theory Marks','Numerical Marks','Practical Marks'],axis=1,inplace=True)


print(phy.head())


df1 = pd.merge(maths,phy,on = ['Roll No','Class'],how = 'outer')


print(df1.head())


df2 = pd.merge(df1,eco,on = ['Roll No','Class'],how = 'outer')


print(df2.head())


df3 = pd.merge(df2,hindi,on = ['Roll No','Class'],how = 'outer')


df = pd.merge(df3,music,on = ['Roll No','Class'],how = 'outer')


df['%total'] = (df['%maths']+df['%eco']+df['%hindi']+df['%music']+df['%phy'])/5
df.to_csv('final_student.csv')
print(df.head())


# no. of students enrolled with the tution provider
sol1 = df['Roll No'].count()
print(sol1)


# no of students taken all 5 subjects
sol2 = df.dropna()['Roll No'].count()
print(sol2)


# class which has most no. of students
sol3 = df['Class'].value_counts()
print(sol3)


sol4 = df.dropna().groupby('Class').mean()['%total'].sort_values(ascending=False).iloc[0:2]
print(sol4)


sol5 = df.drop(['Roll No','Class','%total'],axis=1).describe().loc['50%'].sort_values(ascending=False).iloc[0:2]
print(sol5)






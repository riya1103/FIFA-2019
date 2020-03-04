import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

df=pd.read_csv('data.csv')
df.columns
df.info()
df=df.drop(columns=['Unnamed: 0','ID','Photo','Flag','Club Logo'])
null=df.isnull().sum()
sbn.scatterplot(x=df['Potential'],y=df['Club'])
sbn.boxplot(x=df['Potential'],y=df['Club'])
a=df.groupby(['Club']).Potential.mean()
b=df.groupby(['Name']).Potential.mean()
c=df.groupby(['Nationality']).Potential.mean()
c.idxmax()
b.idxmax()
a.idxmax()
b.idxmin()

df[df['Name']=='K. Mbappé'].Club
df[df['Name']=='K. Mbappé'].Nationality
df[df['Name']=='K. Mbappé'].Overall

df[df['Nationality']=='Dominican Republic'].Club
df[df['Nationality']=='Dominican Republic'].Name
df[df['Name']=='K. Pilkington'].Potential
df['Potential'].mode()
df['Potential'].mean()
df['Potential'].max()
df['Overall'].mean()
df['Overall'].mode()
df['Overall'].max()
df['Overall'].min()
df['Overall'].idxmax()

df['Wage']=df['Wage'].str.replace('€','')
df['Wage']=df['Wage'].str.replace('K','')
df['Value']=df['Value'].str.replace('€','')
df['Value']=df['Value'].str.replace('M','')
df['Value']=df['Value'].str.replace('K','')

df['Value']=df['Value'].astype(float)
df['Wage']=df['Wage'].astype(int)
df.info()
df.columns
df1=df[['Name', 'Age', 'Nationality', 'Overall', 'Potential', 'Club', 'Value',
       'Wage', 'Special', 'Preferred Foot', 'International Reputation',
       'Weak Foot', 'Skill Moves', 'Work Rate', 'Body Type','Position', 'Joined',
       'Height', 'Weight','Crossing', 'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys',
       'Dribbling', 'Curve', 'FKAccuracy', 'LongPassing', 'BallControl',
       'Acceleration', 'SprintSpeed', 'Agility', 'Reactions', 'Balance',
       'ShotPower', 'Jumping', 'Stamina', 'Strength', 'LongShots',
       'Aggression', 'Interceptions', 'Positioning', 'Vision', 'Penalties',
       'Composure', 'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving',
       'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes',
       'Release Clause']]

unique=df1.nunique()

unique=unique.to_frame()
unique=unique.reset_index()

sbn.scatterplot(x=unique['index'],y=unique[0])
sbn.boxplot(x=unique['index'],y=unique[0])
plt.hist(unique['index'])

df2=df1.loc[0:100]
df1['ShortPassing'].fillna(df1['ShortPassing'].mean(), inplace = True)
df1['Volleys'].fillna(df1['Volleys'].mean(), inplace = True)
df1['Dribbling'].fillna(df1['Dribbling'].mean(), inplace = True)
df1['Curve'].fillna(df1['Curve'].mean(), inplace = True)
df1['FKAccuracy'].fillna(df1['FKAccuracy'], inplace = True)
df1['LongPassing'].fillna(df1['LongPassing'].mean(), inplace = True)
df1['BallControl'].fillna(df1['BallControl'].mean(), inplace = True)
df1['HeadingAccuracy'].fillna(df1['HeadingAccuracy'].mean(), inplace = True)
df1['Finishing'].fillna(df1['Finishing'].mean(), inplace = True)
df1['Crossing'].fillna(df1['Crossing'].mean(), inplace = True)



df1['Weight'].fillna('200lbs', inplace = True)
df1['Height'].fillna("5'11", inplace = True)
df1['Joined'].fillna('Jul 1, 2018', inplace = True)
df1['Body Type'].fillna('Normal', inplace = True)
df1['Position'].fillna('ST', inplace = True)
df1['Club'].fillna('No Club', inplace = True)
df1['Work Rate'].fillna('Medium/ Medium', inplace = True)
df1['Skill Moves'].fillna(df1['Skill Moves'].median(), inplace = True)
df1['Weak Foot'].fillna(3, inplace = True)
df1['Preferred Foot'].fillna('Right', inplace = True)
df1['International Reputation'].fillna(1, inplace = True)
df1['Wage'].fillna('€200K', inplace = True)
df1['Stamina'].fillna(df1['Stamina'].mean(),inplace=True)

df1.isnull().sum()

df1.fillna(0,inplace=True)

plt.scatter(df1['Overall'], df1['International Reputation'], s = df1['Age']*1000, c = 'pink')
plt.xlabel('Overall Ratings', fontsize = 20)
plt.ylabel('International Reputation', fontsize = 20)
plt.title('Ratings vs Reputation', fontweight = 20, fontsize = 20)
#plt.legend('Age', loc = 'upper left')
plt.show()
plt.rcParams['figure.figsize'] = (15, 5)
plt.xlabel('Wage Range for Players', fontsize = 16)
plt.ylabel('Count of the Players', fontsize = 16)
plt.title('Distribution of Wages of Players', fontsize = 20)
plt.xticks(rotation = 90)
sbn.distplot(df1['Wage'],hist=True,kde=True, color = 'blue')

sbn.relplot(x='Wage',y='Club',hue='Value',data=df2)
sbn.relplot(x='Wage',y='Age',kind='line',data=df2)

sbn.relplot(x='Wage',y='Name',hue='Age',data=df2)
sbn.catplot(x='Club',y='Value',data=df2)
sbn.catplot(x='Club',y='Value',kind='swarm',data=df2)
sbn.catplot(x='Club',y='Value',data=df2)

from scipy import stats
#univariate distributions
c=np.random.normal(loc=5,size=100,scale=2)
sbn.distplot(c)
#bivariate distribution


facet=sbn.FacetGrid(df2,col='Club')
facet.map(plt.hist,'Age')


facet=sbn.FacetGrid(df2,col='Club')
facet.map(plt.hist,'Wage')













































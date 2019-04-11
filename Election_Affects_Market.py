
# coding: utf-8

# In[2]:


import pandas as pd
import os
import time
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from matplotlib.ticker import EngFormatter


# In[6]:


election_dates = {'Election_dates':['6MonthsBefore','3MonthsBefore','1MonthBefore','ElectionMonth','1MonthAfter','3MonthsAfter','6MonthsAfter'],'dates2014': ['Dec-2013','Feb-2014','Apr-2014','May-2014','Jun-2014','Aug-2014','Nov-2014'],
                  'dates2009': ['Dec-2008','Feb-2009','Apr-2009','May-2009','Jun-2009','Aug-2009','Nov-2009'],'dates2004': ['Dec-2003','Feb-2004','Apr-2004','May-2004','Jun-2004','Aug-2004','Nov-2004'],
                  'dates1999': ['Apr-1999','Jul-1999','Sep-1999','Oct-1999','Nov-1999','Jan-2000','Apr-2000'],
                  'dates1998': ['Aug-1997','Nov-1997','Jan-1998','Feb-1998','Mar-1998','May-1998','Aug-1998'],
                  'dates1996': ['Dec-1995','Feb-1996','Apr-1996','May-1996','Jun-1996','Aug-1996','Nov-1996'],
                 }
election_dates = pd.DataFrame.from_dict(election_dates)
election_dates['dates2014'] = pd.to_datetime(election_dates['dates2014'])
election_dates['dates2009'] = pd.to_datetime(election_dates['dates2009'])
election_dates['dates2004'] = pd.to_datetime(election_dates['dates2004'])
election_dates['dates1999'] = pd.to_datetime(election_dates['dates1999'])
election_dates['dates1998'] = pd.to_datetime(election_dates['dates1998'])
election_dates['dates1996'] = pd.to_datetime(election_dates['dates1996'])

election_dates = election_dates.melt(id_vars=['Election_dates'],value_vars=['dates1996','dates1998','dates1999','dates2004','dates2009','dates2014'],var_name='Date_year',value_name='Dates')


# In[7]:


path1 = 'C:/Users/nairr/Python Codes Practice/ElectionStockMarket/'
files = os.listdir(path1)
b = {}

for i, f in enumerate(files):
    data = pd.read_csv(r'C:/Users/nairr/Python Codes Practice/ElectionStockMarket/' + f,index_col=False)
    a = f.replace('.csv','')
    a = a.replace(' ','_')
    b[a] = pd.DataFrame()
    b[a] = data.copy()
b.keys()


# In[9]:


BSE_100 = pd.DataFrame.from_dict(b['BSE_100'])
BSE_100['Month'] = pd.to_datetime(BSE_100['Month'])
BSE_100.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_200 = pd.DataFrame.from_dict(b['BSE_200'])
BSE_200['Month'] = pd.to_datetime(BSE_200['Month'])
BSE_200.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_500 = pd.DataFrame.from_dict(b['BSE_500'])
BSE_500['Month'] = pd.to_datetime(BSE_500['Month'])
BSE_500.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_Sensex = pd.DataFrame.from_dict(b['BSE_Sensex'])
BSE_Sensex['Month'] = pd.to_datetime(BSE_Sensex['Month'])
BSE_Sensex.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_Auto = pd.DataFrame.from_dict(b['BSE_Auto'])
BSE_Auto['Month'] = pd.to_datetime(BSE_Auto['Month'])
BSE_Auto.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_FMCG = pd.DataFrame.from_dict(b['BSE_FMCG'])
BSE_FMCG['Month'] = pd.to_datetime(BSE_FMCG['Month'])
BSE_FMCG.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_Healthcare = pd.DataFrame.from_dict(b['BSE_Healthcare'])
BSE_Healthcare['Month'] = pd.to_datetime(BSE_Healthcare['Month'])
BSE_Healthcare.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_IT = pd.DataFrame.from_dict(b['BSE_IT'])
BSE_IT['Month'] = pd.to_datetime(BSE_IT['Month'])
BSE_IT.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_Metal = pd.DataFrame.from_dict(b['BSE_Metal'])
BSE_Metal['Month'] = pd.to_datetime(BSE_Metal['Month'])
BSE_Metal.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_OIl_Gas = pd.DataFrame.from_dict(b['BSE_OIl_Gas'])
BSE_OIl_Gas['Month'] = pd.to_datetime(BSE_OIl_Gas['Month'])
BSE_OIl_Gas.drop(['Open','High','Low'],axis=1,inplace=True)
BSE_Banks = pd.DataFrame.from_dict(b['BSE_Banks'])
BSE_Banks['Month'] = pd.to_datetime(BSE_Banks['Month'])
BSE_Banks.drop(['Open','High','Low'],axis=1,inplace=True)


# In[10]:


BSE_Sensex_2014 = BSE_Sensex.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_Sensex_2014['Index'] = 'BSE_Sexsex'
BSE_100_2014 = BSE_100.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_100_2014['Index'] = 'BSE_100'
BSE_200_2014 = BSE_200.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_200_2014['Index'] = 'BSE_200'
BSE_500_2014 = BSE_500.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_500_2014['Index'] = 'BSE_500'
BSE_Sensex_2014['Ret%']= ((BSE_Sensex_2014['Close'].pct_change(1))*100).round(2)
BSE_Sensex_2014['Num'] = range(7)
BSE_100_2014['Ret1%']= ((BSE_100_2014['Close'].pct_change(1))*100).round(2)
BSE_100_2014['Num'] = BSE_Sensex_2014['Num'] + 0.2
BSE_200_2014['Ret2%']= ((BSE_200_2014['Close'].pct_change(1))*100).round(2)
BSE_200_2014['Num'] = BSE_100_2014['Num'] + 0.2
BSE_500_2014['Ret3%']= ((BSE_500_2014['Close'].pct_change(1))*100).round(2)
BSE_500_2014['Num'] = BSE_200_2014['Num'] + 0.2
BSE_2014 = pd.concat([BSE_Sensex_2014,BSE_100_2014,BSE_200_2014,BSE_500_2014])


# In[108]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-muted')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Sensex','BSE 100','BSE 200','BSE 500']
BSE_2014.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%','Ret3%'],ax=ax,edgecolor='black',animated=True)
plt.legend(leg,loc=2)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Index movements - 2014 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[11]:


BSE_Auto_2014 = BSE_Auto.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_Auto_2014['Index'] = 'BSE_Auto'
BSE_FMCG_2014 = BSE_FMCG.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_FMCG_2014['Index'] = 'BSE_FMCG'
BSE_Healthcare_2014 = BSE_Healthcare.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_Healthcare_2014['Index'] = 'BSE_Healthcare'
BSE_IT_2014 = BSE_IT.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_IT_2014['Index'] = 'BSE_IT'
BSE_Metal_2014 = BSE_Metal.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_Metal_2014['Index'] = 'BSE_Metal'
BSE_Oil_Gas_2014 = BSE_Oil_Gas.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_Oil_Gas_2014['Index'] = 'BSE_Oil_Gas'
BSE_Banks_2014 = BSE_Banks.merge(election_dates[election_dates['Date_year']=='dates2014'],left_on='Month',right_on='Dates')
BSE_Banks_2014['Index'] = 'BSE_Banks'

BSE_Auto_2014['Ret%']= ((BSE_Auto_2014['Close'].pct_change(1))*100).round(2)
BSE_Auto_2014['Num'] = range(7)
BSE_FMCG_2014['Ret1%']= ((BSE_FMCG_2014['Close'].pct_change(1))*100).round(2)
BSE_FMCG_2014['Num'] = BSE_Auto_2014['Num'] + 0.5
BSE_Healthcare_2014['Ret2%']= ((BSE_Healthcare_2014['Close'].pct_change(1))*100).round(2)
BSE_Healthcare_2014['Num'] = BSE_FMCG_2014['Num'] + 0.5
BSE_IT_2014['Ret3%']= ((BSE_IT_2014['Close'].pct_change(1))*100).round(2)
BSE_IT_2014['Num'] = BSE_Healthcare_2014['Num'] + 0.5
BSE_Metal_2014['Ret4%']= ((BSE_Metal_2014['Close'].pct_change(1))*100).round(2)
BSE_Metal_2014['Num'] = BSE_IT_2014['Num'] + 0.5
BSE_Oil_Gas_2014['Ret5%']= ((BSE_Oil_Gas_2014['Close'].pct_change(1))*100).round(2)
BSE_Oil_Gas_2014['Num'] = BSE_Metal_2014['Num'] + 0.5
BSE_Banks_2014['Ret6%']= ((BSE_Banks_2014['Close'].pct_change(1))*100).round(2)
BSE_Banks_2014['Num'] = BSE_Oil_Gas_2014['Num'] + 0.5

BSE_Sector_2014 = pd.concat([BSE_Auto_2014,BSE_FMCG_2014,BSE_Healthcare_2014,BSE_IT_2014,BSE_Metal_2014,BSE_Oil_Gas_2014,BSE_Banks_2014])


# In[111]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-white')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Auto','BSE FMCG','BSE Healthcare','BSE IT','BSE Metal','BSE Oil&Gas','BSE Banks']
BSE_Sector_2014.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%','Ret3%','Ret4%','Ret5%','Ret6%'],ax=ax,edgecolor='black',width=.8)
plt.legend(leg,loc=2,fontsize=10)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Sector Index movements - 2014 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[12]:


BSE_Sensex_2009 = BSE_Sensex.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_Sensex_2009['Index'] = 'BSE_Sexsex'
BSE_100_2009 = BSE_100.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_100_2009['Index'] = 'BSE_100'
BSE_200_2009 = BSE_200.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_200_2009['Index'] = 'BSE_200'
BSE_500_2009 = BSE_500.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_500_2009['Index'] = 'BSE_500'

BSE_Sensex_2009['Ret%']= ((BSE_Sensex_2009['Close'].pct_change(1))*100).round(2)
BSE_Sensex_2009['Num'] = range(7)
BSE_100_2009['Ret1%']= ((BSE_100_2009['Close'].pct_change(1))*100).round(2)
BSE_100_2009['Num'] = BSE_Sensex_2009['Num'] + 0.2
BSE_200_2009['Ret2%']= ((BSE_200_2009['Close'].pct_change(1))*100).round(2)
BSE_200_2009['Num'] = BSE_100_2009['Num'] + 0.2
BSE_500_2009['Ret3%']= ((BSE_500_2009['Close'].pct_change(1))*100).round(2)
BSE_500_2009['Num'] = BSE_200_2009['Num'] + 0.2

BSE_2009 = pd.concat([BSE_Sensex_2009,BSE_100_2009,BSE_200_2009,BSE_500_2009])


# In[114]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-muted')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Sensex','BSE 100','BSE 200','BSE 500']
BSE_2009.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%','Ret3%'],ax=ax,edgecolor='black',animated=True)
plt.legend(leg,loc=2)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Index movements - 2009 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[13]:


BSE_Auto_2009 = BSE_Auto.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_Auto_2009['Index'] = 'BSE_Auto'
BSE_FMCG_2009 = BSE_FMCG.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_FMCG_2009['Index'] = 'BSE_FMCG'
BSE_Healthcare_2009 = BSE_Healthcare.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_Healthcare_2009['Index'] = 'BSE_Healthcare'
BSE_IT_2009 = BSE_IT.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_IT_2009['Index'] = 'BSE_IT'
BSE_Metal_2009 = BSE_Metal.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_Metal_2009['Index'] = 'BSE_Metal'
BSE_Oil_Gas_2009 = BSE_Oil_Gas.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_Oil_Gas_2009['Index'] = 'BSE_Oil_Gas'
BSE_Banks_2009 = BSE_Banks.merge(election_dates[election_dates['Date_year']=='dates2009'],left_on='Month',right_on='Dates')
BSE_Banks_2009['Index'] = 'BSE_Banks'

BSE_Auto_2009['Ret%']= ((BSE_Auto_2009['Close'].pct_change(1))*100).round(2)
BSE_Auto_2009['Num'] = range(7)
BSE_FMCG_2009['Ret1%']= ((BSE_FMCG_2009['Close'].pct_change(1))*100).round(2)
BSE_FMCG_2009['Num'] = BSE_Auto_2009['Num'] + 0.5
BSE_Healthcare_2009['Ret2%']= ((BSE_Healthcare_2009['Close'].pct_change(1))*100).round(2)
BSE_Healthcare_2009['Num'] = BSE_FMCG_2009['Num'] + 0.5
BSE_IT_2009['Ret3%']= ((BSE_IT_2009['Close'].pct_change(1))*100).round(2)
BSE_IT_2009['Num'] = BSE_Healthcare_2009['Num'] + 0.5
BSE_Metal_2009['Ret4%']= ((BSE_Metal_2009['Close'].pct_change(1))*100).round(2)
BSE_Metal_2009['Num'] = BSE_IT_2009['Num'] + 0.5
BSE_Oil_Gas_2009['Ret5%']= ((BSE_Oil_Gas_2009['Close'].pct_change(1))*100).round(2)
BSE_Oil_Gas_2009['Num'] = BSE_Metal_2009['Num'] + 0.5
BSE_Banks_2009['Ret6%']= ((BSE_Banks_2009['Close'].pct_change(1))*100).round(2)
BSE_Banks_2009['Num'] = BSE_Oil_Gas_2009['Num'] + 0.5

BSE_Sector_2009 = pd.concat([BSE_Auto_2009,BSE_FMCG_2009,BSE_Healthcare_2009,BSE_IT_2009,BSE_Metal_2009,BSE_Oil_Gas_2009,BSE_Banks_2009])


# In[115]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-white')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Auto','BSE FMCG','BSE Healthcare','BSE IT','BSE Metal','BSE Oil&Gas','BSE Banks']
BSE_Sector_2009.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%','Ret3%','Ret4%','Ret5%','Ret6%'],ax=ax,edgecolor='black',width=.8)
plt.legend(leg,loc=2,fontsize=10)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Sector Index movements - 2009 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[14]:


BSE_Sensex_2004 = BSE_Sensex.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_Sensex_2004['Index'] = 'BSE_Sexsex'

BSE_100_2004 = BSE_100.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_100_2004['Index'] = 'BSE_100'

BSE_200_2004 = BSE_200.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_200_2004['Index'] = 'BSE_200'

BSE_500_2004 = BSE_500.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_500_2004['Index'] = 'BSE_500'

BSE_Sensex_2004['Ret%']= ((BSE_Sensex_2004['Close'].pct_change(1))*100).round(2)
BSE_Sensex_2004['Num'] = range(7)
BSE_100_2004['Ret1%']= ((BSE_100_2004['Close'].pct_change(1))*100).round(2)
BSE_100_2004['Num'] = BSE_Sensex_2004['Num'] + 0.2
BSE_200_2004['Ret2%']= ((BSE_200_2004['Close'].pct_change(1))*100).round(2)
BSE_200_2004['Num'] = BSE_100_2004['Num'] + 0.2
BSE_500_2004['Ret3%']= ((BSE_500_2004['Close'].pct_change(1))*100).round(2)
BSE_500_2004['Num'] = BSE_200_2004['Num'] + 0.2

BSE_2004 = pd.concat([BSE_Sensex_2004,BSE_100_2004,BSE_200_2004,BSE_500_2004])


# In[129]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-muted')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Sensex','BSE 100','BSE 200','BSE 500']
BSE_2004.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%','Ret3%'],ax=ax,edgecolor='black',animated=True)
plt.legend(leg,loc=2)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Index movements - 2004 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[15]:


BSE_Auto_2004 = BSE_Auto.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_Auto_2004['Index'] = 'BSE_Auto'
BSE_FMCG_2004 = BSE_FMCG.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_FMCG_2004['Index'] = 'BSE_FMCG'
BSE_Healthcare_2004 = BSE_Healthcare.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_Healthcare_2004['Index'] = 'BSE_Healthcare'
BSE_IT_2004 = BSE_IT.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_IT_2004['Index'] = 'BSE_IT'
BSE_Metal_2004 = BSE_Metal.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_Metal_2004['Index'] = 'BSE_Metal'
BSE_Oil_Gas_2004 = BSE_Oil_Gas.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_Oil_Gas_2004['Index'] = 'BSE_Oil_Gas'
BSE_Banks_2004 = BSE_Banks.merge(election_dates[election_dates['Date_year']=='dates2004'],left_on='Month',right_on='Dates')
BSE_Banks_2004['Index'] = 'BSE_Banks'

BSE_Auto_2004['Ret%']= ((BSE_Auto_2004['Close'].pct_change(1))*100).round(2)
BSE_Auto_2004['Num'] = range(7)
BSE_FMCG_2004['Ret1%']= ((BSE_FMCG_2004['Close'].pct_change(1))*100).round(2)
BSE_FMCG_2004['Num'] = BSE_Auto_2004['Num'] + 0.5
BSE_Healthcare_2004['Ret2%']= ((BSE_Healthcare_2004['Close'].pct_change(1))*100).round(2)
BSE_Healthcare_2004['Num'] = BSE_FMCG_2004['Num'] + 0.5
BSE_IT_2004['Ret3%']= ((BSE_IT_2004['Close'].pct_change(1))*100).round(2)
BSE_IT_2004['Num'] = BSE_Healthcare_2004['Num'] + 0.5
BSE_Metal_2004['Ret4%']= ((BSE_Metal_2004['Close'].pct_change(1))*100).round(2)
BSE_Metal_2004['Num'] = BSE_IT_2004['Num'] + 0.5
BSE_Oil_Gas_2004['Ret5%']= ((BSE_Oil_Gas_2004['Close'].pct_change(1))*100).round(2)
BSE_Oil_Gas_2004['Num'] = BSE_Metal_2004['Num'] + 0.5
BSE_Banks_2004['Ret6%']= ((BSE_Banks_2004['Close'].pct_change(1))*100).round(2)
BSE_Banks_2004['Num'] = BSE_Oil_Gas_2004['Num'] + 0.5

BSE_Sector_2004 = pd.concat([BSE_Auto_2004,BSE_FMCG_2004,BSE_Healthcare_2004,BSE_IT_2004,BSE_Metal_2004,BSE_Oil_Gas_2004,BSE_Banks_2004])


# In[121]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-white')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Auto','BSE FMCG','BSE Healthcare','BSE IT','BSE Metal','BSE Oil&Gas','BSE Banks']
BSE_Sector_2004.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%','Ret3%','Ret4%','Ret5%','Ret6%'],ax=ax,edgecolor='black',width=.8)
plt.legend(leg,loc=2,fontsize=10)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Sector Index movements - 2004 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[16]:


BSE_Sensex_1999 = BSE_Sensex.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_Sensex_1999['Index'] = 'BSE_Sexsex'
BSE_100_1999 = BSE_100.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_100_1999['Index'] = 'BSE_100'
BSE_200_1999 = BSE_200.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_200_1999['Index'] = 'BSE_200'
BSE_500_1999 = BSE_500.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_500_1999['Index'] = 'BSE_500'

BSE_Sensex_1999['Ret%']= ((BSE_Sensex_1999['Close'].pct_change(1))*100).round(2)
BSE_Sensex_1999['Num'] = range(7)
BSE_100_1999['Ret1%']= ((BSE_100_1999['Close'].pct_change(1))*100).round(2)
BSE_100_1999['Num'] = BSE_Sensex_1999['Num'] + 0.2
BSE_200_1999['Ret2%']= ((BSE_200_1999['Close'].pct_change(1))*100).round(2)
BSE_200_1999['Num'] = BSE_100_1999['Num'] + 0.2
BSE_500_1999['Ret3%']= ((BSE_500_1999['Close'].pct_change(1))*100).round(2)
BSE_500_1999['Num'] = BSE_200_1999['Num'] + 0.2

BSE_1999 = pd.concat([BSE_Sensex_1999,BSE_100_1999,BSE_200_1999,BSE_500_1999])


# In[130]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-muted')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Sensex','BSE 100','BSE 200','BSE 500']
BSE_1999.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%','Ret3%'],ax=ax,edgecolor='black',animated=True)
plt.legend(leg,loc=3)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Index movements - 1999 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[17]:


BSE_Auto_1999 = BSE_Auto.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_Auto_1999['Index'] = 'BSE_Auto'
BSE_FMCG_1999 = BSE_FMCG.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_FMCG_1999['Index'] = 'BSE_FMCG'
BSE_Healthcare_1999 = BSE_Healthcare.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_Healthcare_1999['Index'] = 'BSE_Healthcare'
BSE_IT_1999 = BSE_IT.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_IT_2004['Index'] = 'BSE_IT'
BSE_Metal_1999 = BSE_Metal.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_Metal_1999['Index'] = 'BSE_Metal'
BSE_Oil_Gas_1999 = BSE_Oil_Gas.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_Oil_Gas_1999['Index'] = 'BSE_Oil_Gas'
BSE_Banks_1999 = BSE_Banks.merge(election_dates[election_dates['Date_year']=='dates1999'],left_on='Month',right_on='Dates')
BSE_Banks_1999['Index'] = 'BSE_Banks'

BSE_Auto_1999['Ret%']= ((BSE_Auto_1999['Close'].pct_change(1))*100).round(2)
BSE_Auto_1999['Num'] = range(7)
BSE_FMCG_1999['Ret1%']= ((BSE_FMCG_1999['Close'].pct_change(1))*100).round(2)
BSE_FMCG_1999['Num'] = BSE_Auto_1999['Num'] + 0.5
BSE_Healthcare_1999['Ret2%']= ((BSE_Healthcare_1999['Close'].pct_change(1))*100).round(2)
BSE_Healthcare_1999['Num'] = BSE_FMCG_1999['Num'] + 0.5
BSE_IT_1999['Ret3%']= ((BSE_IT_1999['Close'].pct_change(1))*100).round(2)
BSE_IT_1999['Num'] = BSE_Healthcare_1999['Num'] + 0.5
BSE_Metal_1999['Ret4%']= ((BSE_Metal_1999['Close'].pct_change(1))*100).round(2)
BSE_Metal_1999['Num'] = BSE_IT_1999['Num'] + 0.5
BSE_Oil_Gas_1999['Ret5%']= ((BSE_Oil_Gas_1999['Close'].pct_change(1))*100).round(2)
BSE_Oil_Gas_1999['Num'] = BSE_Metal_1999['Num'] + 0.5
BSE_Banks_1999['Ret6%']= ((BSE_Banks_1999['Close'].pct_change(1))*100).round(2)
BSE_Banks_1999['Num'] = BSE_Oil_Gas_1999['Num'] + 0.5

BSE_Sector_1999 = pd.concat([BSE_Auto_1999,BSE_FMCG_1999,BSE_Healthcare_1999,BSE_IT_1999,BSE_Metal_1999,BSE_Oil_Gas_1999,BSE_Banks_1999])


# In[133]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-white')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Auto','BSE FMCG','BSE Healthcare','BSE IT','BSE Metal','BSE Oil&Gas','BSE Banks']
BSE_Sector_1999.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%','Ret3%','Ret4%','Ret5%','Ret6%'],ax=ax,edgecolor='black',width=.8)
plt.legend(leg,loc=1,fontsize=10)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Sector Index movements - 1999 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[61]:


BSE_Sensex_1998 = BSE_Sensex.merge(election_dates[election_dates['Date_year']=='dates1998'],left_on='Month',right_on='Dates')
BSE_Sensex_1998['Index'] = 'BSE_Sexsex'

BSE_100_1998 = BSE_100.merge(election_dates[election_dates['Date_year']=='dates1998'],left_on='Month',right_on='Dates')
BSE_100_1998['Index'] = 'BSE_100'

BSE_200_1998 = BSE_200.merge(election_dates[election_dates['Date_year']=='dates1998'],left_on='Month',right_on='Dates')
BSE_200_1998['Index'] = 'BSE_200'

BSE_Sensex_1998['Ret%']= ((BSE_Sensex_1998['Close'].pct_change(1))*100).round(2)
BSE_Sensex_1998['Num'] = range(7)
BSE_100_1998['Ret1%']= ((BSE_100_1998['Close'].pct_change(1))*100).round(2)
BSE_100_1998['Num'] = BSE_Sensex_1998['Num'] + 0.2
BSE_200_1998['Ret2%']= ((BSE_200_1998['Close'].pct_change(1))*100).round(2)
BSE_200_1998['Num'] = BSE_100_1998['Num'] + 0.2

BSE_1998 = pd.concat([BSE_Sensex_1998,BSE_100_1998,BSE_200_1998])


# In[136]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-muted')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Sensex','BSE 100','BSE 200']
BSE_1998.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%'],ax=ax,edgecolor='black',animated=True)
plt.legend(leg,loc=3)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Index movements - 1998 Elections',fontsize=14,fontweight='bold')
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[59]:


BSE_Sensex_1996 = BSE_Sensex.merge(election_dates[election_dates['Date_year']=='dates1996'],left_on='Month',right_on='Dates')
BSE_Sensex_1996['Index'] = 'BSE_Sexsex'

BSE_100_1996 = BSE_100.merge(election_dates[election_dates['Date_year']=='dates1996'],left_on='Month',right_on='Dates')
BSE_100_1996['Index'] = 'BSE_100'

BSE_200_1996 = BSE_200.merge(election_dates[election_dates['Date_year']=='dates1996'],left_on='Month',right_on='Dates')
BSE_200_1996['Index'] = 'BSE_200'

BSE_Sensex_1996['Ret%']= ((BSE_Sensex_1996['Close'].pct_change(1))*100).round(2)
BSE_Sensex_1996['Num'] = range(7)
BSE_100_1996['Ret1%']= ((BSE_100_1996['Close'].pct_change(1))*100).round(2)
BSE_100_1996['Num'] = BSE_Sensex_1996['Num'] + 0.2
BSE_200_1996['Ret2%']= ((BSE_200_1996['Close'].pct_change(1))*100).round(2)
BSE_200_1996['Num'] = BSE_100_1996['Num'] + 0.2

BSE_1996 = pd.concat([BSE_Sensex_1996,BSE_100_1996,BSE_200_1996])


# In[60]:


get_ipython().magic('matplotlib inline')
style.use('seaborn-muted')
fig, ax = plt.subplots(figsize=(8,4))
leg = ['BSE Sensex','BSE 100','BSE 200']
BSE_1996.groupby('Index').plot.bar(x='Num',y=['Ret%','Ret1%','Ret2%'],ax=ax,edgecolor='black',animated=True)
plt.legend(leg,loc=3)
ax.set_xticklabels(BSE_Sensex_1996.Election_dates.values)
plt.xticks(rotation='25')
ax.grid(False)
plt.title('BSE Index movements - 1996 Elections',fontsize=14)
plt.ylabel('% Movements per Duration',color='black',fontsize=12)
plt.xlabel('Durations - Before and after Election',color='black',fontsize=12)
ax.yaxis.set_major_formatter(EngFormatter(unit=u"%"))
plt.show()


# In[19]:


BSE_Sensex_2014['Index'] = 'BSE_Sensex_2014'
BSE_Sensex_2009['Index'] = 'BSE_Sensex_2009'
BSE_Sensex_2004['Index'] = 'BSE_Sensex_2004'
BSE_Sensex_1999['Index'] = 'BSE_Sensex_1999'
BSE_Sensex_f = pd.concat([BSE_Sensex_2014,BSE_Sensex_2009,BSE_Sensex_2004,BSE_Sensex_1999])

BSE_Sensex_fi = BSE_Sensex_f.groupby(['Election_dates'],as_index=False).agg({'Ret%':'mean'})
BSE_Sensex_fi['Index'] = 'BSE_Sensex_Mean'
BSE_Sensex_fins = pd.concat([BSE_Sensex_f,BSE_Sensex_fi])
BSE_Sensex_fin = BSE_Sensex_fins.pivot(index='Index',columns='Election_dates',values='Ret%')
BSE_Sensex_fin['6MonthsBefore'] = 0
column_titles=['6MonthsBefore','3MonthsBefore','1MonthBefore','ElectionMonth','1MonthAfter','3MonthsAfter','6MonthsAfter']
BSE_Sensex_fin = BSE_Sensex_fin.reindex(columns=column_titles)
BSE_Sensex_fin =BSE_Sensex_fin.round(2)
BSE_Sensex_fin


# In[22]:


BSE_Auto_2014['Index'] = 'Auto_2014'
BSE_Auto_2009['Index'] = 'Auto_2009'
BSE_Auto_2004['Index'] = 'Auto_2004'
BSE_Auto_1999['Index'] = 'Auto_1999'

BSE_Auto_f = pd.concat([BSE_Auto_2014,BSE_Auto_2009,BSE_Auto_2004,BSE_Auto_1999])
BSE_Auto_fi = BSE_Auto_f.groupby(['Election_dates'],as_index=False).agg({'Ret%':'mean'})
BSE_Auto_fi['Index'] = 'BSE_Auto_Mean'
BSE_Auto_fins = pd.concat([BSE_Auto_f,BSE_Auto_fi])
BSE_Auto_fin = BSE_Auto_fins.pivot(index='Index',columns='Election_dates',values='Ret%')
BSE_Auto_fin['6MonthsBefore'] = 0
column_titles=['6MonthsBefore','3MonthsBefore','1MonthBefore','ElectionMonth','1MonthAfter','3MonthsAfter','6MonthsAfter']
BSE_Auto_fin = BSE_Auto_fin.reindex(columns=column_titles)
BSE_Auto_fin =BSE_Auto_fin.round(2)
BSE_Auto_fin


# In[26]:


BSE_Metal_2014['Index'] = 'Metal_2014'
BSE_Metal_2009['Index'] = 'Metal_2009'
BSE_Metal_2004['Index'] = 'Metal_2004'
BSE_Metal_1999['Index'] = 'Metal_1999'

BSE_Metal_f = pd.concat([BSE_Metal_2014,BSE_Metal_2009,BSE_Metal_2004,BSE_Metal_1999])
BSE_Metal_fi = BSE_Metal_f.groupby(['Election_dates'],as_index=False).agg({'Ret4%':'mean'})
BSE_Metal_fi['Index'] = 'Metal_Mean'
BSE_Metal_fins = pd.concat([BSE_Metal_f,BSE_Metal_fi])
BSE_Metal_fin = BSE_Metal_fins.pivot(index='Index',columns='Election_dates',values='Ret4%')
BSE_Metal_fin['6MonthsBefore'] = 0
column_titles=['6MonthsBefore','3MonthsBefore','1MonthBefore','ElectionMonth','1MonthAfter','3MonthsAfter','6MonthsAfter']
BSE_Metal_fin = BSE_Metal_fin.reindex(columns=column_titles)
BSE_Metal_fin =BSE_Metal_fin.round(2)
BSE_Metal_fin


# In[33]:


BSE_Healthcare_2014['Index'] = 'Healthcare_2014'
BSE_Healthcare_2009['Index'] = 'Healthcare_2009'
BSE_Healthcare_2004['Index'] = 'Healthcare_2004'
BSE_Healthcare_1999['Index'] = 'Healthcare_1999'

BSE_Healthcare_f = pd.concat([BSE_Healthcare_2014,BSE_Healthcare_2009,BSE_Healthcare_2004,BSE_Healthcare_1999])
BSE_Healthcare_fi = BSE_Healthcare_f.groupby(['Election_dates'],as_index=False).agg({'Ret2%':'mean'})
BSE_Healthcare_fi['Index'] = 'Healthcare_Mean'
BSE_Healthcare_fins = pd.concat([BSE_Healthcare_f,BSE_Healthcare_fi])
BSE_Healthcare_fin = BSE_Healthcare_fins.pivot(index='Index',columns='Election_dates',values='Ret2%')
BSE_Healthcare_fin['6MonthsBefore'] = 0
column_titles=['6MonthsBefore','3MonthsBefore','1MonthBefore','ElectionMonth','1MonthAfter','3MonthsAfter','6MonthsAfter']
BSE_Healthcare_fin = BSE_Healthcare_fin.reindex(columns=column_titles)
BSE_Healthcare_fin =BSE_Healthcare_fin.round(2)
BSE_Healthcare_fin


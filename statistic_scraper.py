# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:21:37 2019

@author: dherriott
"""
import requests
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


url = 'https://fantasy.premierleague.com/a/statistics/total_points'


# Make a get request to get the latest position of the international space station from the opennotify api.
response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static")
data = response.json()

# Print the status code of the response.
#print(response.content)

#print(data.keys())

elements = data['elements']

#print(elements[0].keys())

ds = pd.DataFrame(elements)

#Converts cost into millions
ds['now_cost'] = ds['now_cost'] /10
print(ds.columns.values)


is_gk = ds['element_type']==1
is_def = ds['element_type']==2
is_mid = ds['element_type']==3
is_att = ds['element_type']==4

gks = ds[is_gk]
defs = ds[is_def]
mids = ds[is_mid]
atts = ds[is_att]


#defs.plot.scatter(x = 'now_cost', y = 'total_points')
#mids.plot.scatter(x = 'now_cost', y = 'total_points')
#atts.plot.scatter(x = 'now_cost', y = 'total_points')
 


#sns.jointplot(x='now_cost', y='total_points', data=gks)
#sns.regplot(x="now_cost", y="total_points", data=gks, order=1);

print('MIDFIELDERS')
z = np.polyfit(mids['now_cost'], mids['total_points'], 1)
p = np.poly1d(z)

plt.figure()
sns.scatterplot(x='now_cost', y='total_points', data=mids)
sns.lineplot(x=mids['now_cost'], y=p(mids['now_cost']))

mids['delta'] = mids['total_points'] - p(mids['now_cost'])
print(mids[['second_name','now_cost', 'delta']].sort_values(by=['delta'], ascending=False))
print(mids[['second_name','now_cost', 'delta']].sort_values(by=['delta'], ascending=True).head())


print('ATTACKERS')

z = np.polyfit(atts['now_cost'], atts['total_points'], 1)
p = np.poly1d(z)
plt.figure()
sns.scatterplot(x='now_cost', y='total_points', data=atts)
sns.lineplot(x=atts['now_cost'], y=p(atts['now_cost']))

atts['delta'] = atts['total_points'] - p(atts['now_cost'])
print(atts[['second_name','now_cost', 'delta']].sort_values(by=['delta'], ascending=False).head())
print(atts[['second_name','now_cost', 'delta']].sort_values(by=['delta'], ascending=True).head())






plt.figure()
sns.jointplot(x='now_cost', y='total_points', data=defs)


#print(gks[['second_name', 'now_cost']])

#print(gks[['second_name', 'total_points']].sort_values(by=['total_points'], ascending=False).head())
#print(defs[['second_name', 'total_points']].sort_values(by=['total_points'], ascending=False).head())
#print(mids[['second_name', 'total_points']].sort_values(by=['total_points'], ascending=False).head())
#print(atts[['second_name', 'total_points']].sort_values(by=['total_points'], ascending=False).head())

#for i in elements :
 #   print(i['web_name'])

#print(response.headers)
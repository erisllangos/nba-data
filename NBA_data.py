
# coding: utf-8

# In[1]:

import requests, json
import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import lxml.html as lh
import numpy as np


# In[241]:

yo = requests.get('https://www.basketball-reference.com/players/s/satorto01/gamelog/2019#pgl_basic::none')


# In[242]:

html = yo.content
soup = BeautifulSoup(html,'lxml')
table = soup.find_all('table')[7]
dfs = pd.read_html(str(table))
dfsato = dfs[0]
dfsato.head()


# In[243]:

dfsato = dfsato.drop('Tm', 1)


# In[244]:

dfsato.head()


# In[245]:

dfsato =  dfsato.drop(dfsato.columns[dfsato.columns.str.contains('Unnamed',case = False)],axis = 1)


# In[246]:

dfsato.head()


# In[247]:

dfsato['G'] = pd.to_numeric(dfsato['G'], errors='coerce')
satostart = dfsato.loc[dfsato['G'] > 35]


# In[248]:

satostart.head()


# In[249]:

print(satostart)


# In[250]:

####21 starts


# In[251]:

satostart.dtypes


# In[252]:

mains = ['TRB', 'PTS', 'AST', 'TOV']
for s in mains:
    satostart[s] = pd.to_numeric(satostart[s], errors='coerce')


# In[253]:

satostart.dtypes


# In[254]:

satostart.head()


# In[255]:

satostart['total_main'] = satostart['PTS'] + satostart['TRB'] + satostart['AST']


# In[256]:

satostart.head()


# In[257]:

satostart[(satostart.total_main > 20)].count()


# In[258]:

ax1 = satostart.plot.scatter(x='G', y='total_main', c='DarkBlue')
ax1.axhline(y=21)


# In[259]:

ax1.figure


# In[260]:

print(satostart.loc[satostart['total_main'] < 21]['Opp'])


# In[261]:

ax2 = satostart.plot.scatter(x='G', y='TOV', c='DarkBlue')
ax2.axhline(y=1.5)


# In[262]:

ax2.figure


# In[263]:

print(satostart['TOV'].median())


# In[264]:

######end of satoransky
######start of blake griffin


# In[265]:

bg = requests.get('https://www.basketball-reference.com/players/g/griffbl01/gamelog/2019#pgl_basic::none')


# In[266]:

htmlbg = bg.content
soupbg = BeautifulSoup(htmlbg,'lxml')
tablebg = soupbg.find_all('table')[7]
dfsbg = pd.read_html(str(tablebg))
dfbg = dfsbg[0]
dfbg.head()


# In[267]:

dfbg =  dfbg.drop(dfbg.columns[dfbg.columns.str.contains('Unnamed',case = False)],axis = 1)


# In[268]:

dfbg.head()


# In[269]:

mainsbg = ['TRB', 'PTS', 'AST', 'TOV', 'G', 'FT', 'FTA', 'STL', 'BLK', 'PF', '3P', '3PA', 'FG', 'FGA']
for s in mainsbg:
    dfbg[s] = pd.to_numeric(dfbg[s], errors='coerce')


# In[270]:

dfbg['total_main'] = dfbg['PTS'] + dfbg['TRB'] + dfbg['AST']


# In[271]:

ax3 = dfbg.plot.scatter(x='G', y='PTS', c='DarkBlue')
ax3.axhline(y=25.5)


# In[272]:

ax3.figure


# In[273]:

#####reggie jackson


# In[274]:

rj = requests.get('https://www.basketball-reference.com/players/j/jacksre01/gamelog/2019#pgl_basic::none')


# In[275]:

htmlrj = rj.content
souprj = BeautifulSoup(htmlrj,'lxml')
tablerj = souprj.find_all('table')[7]
dfsrj = pd.read_html(str(tablerj))
dfrj = dfsrj[0]
dfrj.head()


# In[276]:

dfrj =  dfrj.drop(dfrj.columns[dfrj.columns.str.contains('Unnamed',case = False)],axis = 1)


# In[277]:

for s in mainsbg:
    dfrj[s] = pd.to_numeric(dfrj[s], errors='coerce')


# In[278]:

rj2019 = dfrj.loc[dfrj['G'] >= 35]


# In[279]:

ax4 = dfrj.plot.scatter(x='G', y='PTS', c='DarkBlue')
ax4.axhline(y=16)


# In[280]:

ax4.figure


# In[281]:

fg_makes_rj = rj2019['FG'].sum()
fga_rj = rj2019['FGA'].sum()

fgperc = float(fg_makes_rj) / float(fga_rj)
print(fgperc)

TSA =  rj2019['FGA'].mean() + 0.44 * rj2019['FTA'].mean()
TS_perc = rj2019['PTS'].mean() / (2*TSA)
print(TS_perc)


# In[282]:

###dredrumm


# In[283]:

drummond = requests.get('https://www.basketball-reference.com/players/d/drumman01/gamelog/2019#pgl_basic::none')


# In[284]:

htmldre = drummond.content
soupdre = BeautifulSoup(htmldre,'lxml')
tabledre = soupdre.find_all('table')[7]
dfsdre = pd.read_html(str(tabledre))
dfdre = dfsdre[0]


# In[285]:

dfdre =  dfdre.drop(dfdre.columns[dfdre.columns.str.contains('Unnamed',case = False)],axis = 1)


# In[286]:

for s in mainsbg:
    dfdre[s] = pd.to_numeric(dfdre[s], errors='coerce')


# In[287]:

dresample = dfdre.loc[dfdre['G'] >= 39]


# In[288]:

dresample.head()


# In[289]:

ft_makes_dre = dresample['FT'].sum()
fta_dre = dresample['FTA'].sum()
##adding tonight's numbers
ft_makes_dre += 7
fta_dre += 8
ftperc = float(ft_makes_dre) / float(fta_dre)


# In[290]:

print("Andre Drummond 20 game FT%", ftperc)


# In[291]:

##lebronFT


# In[292]:

bronFT = requests.get('https://www.basketball-reference.com/players/j/jamesle01/gamelog/2019#pgl_basic::none')


# In[293]:

htmllft = bronFT.content
souplay = BeautifulSoup(htmllft,'lxml')
tablelay = souplay.find_all('table')[7]
dfslay = pd.read_html(str(tablelay))
dflay = dfslay[0]


# In[294]:

dflay =  dflay.drop(dflay.columns[dflay.columns.str.contains('Unnamed',case = False)],axis = 1)


# In[295]:

for s in mainsbg:
    dflay[s] = pd.to_numeric(dflay[s], errors='coerce')


# In[296]:

laysample = dflay.loc[dflay['G'] >= 28]


# In[297]:

print(laysample.mean())


# In[298]:

laysample.head()


# In[299]:

ft_makes_bron = laysample['FT'].sum()
fta_bron = laysample['FTA'].sum()
ft_makes_bron += 3
fta_bron += 7
ftperc = float(ft_makes_bron) / float(fta_bron)
print("Lebron 20 game FT%", ftperc)


# In[300]:

##pipm


# In[301]:

pipm = requests.get('https://www.bball-index.com/18-pipm/')


# In[302]:

doc = lh.fromstring(pipm.content)


# In[303]:

tr_elements = doc.xpath('//tr')


# In[304]:

[len(T) for T in tr_elements[:12]]


# In[305]:

col = []
i = 0
for t in tr_elements[0]:
    i+=1
    name=t.text_content()
    col.append((name,[]))
    
print(col)


# In[306]:

for j in range(1,len(tr_elements)):
    #T is our j'th row
    T=tr_elements[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=12:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=float(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1


# In[307]:

Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)


# In[308]:

df.head()


# In[309]:

mainsdf = ['O-PIPM', 'D-PIPM', 'Age', 'Minutes', 'PIPM', 'Multi-Year O-PIPM', 'Multi-Year D-PIPM', 'Multi-Year PIPM', 'Wins Added']
df["Minutes"] = df["Minutes"].astype(str).str.replace(",","")
for s in mainsdf:
    df[s] = pd.to_numeric(df[s], errors='coerce')


# In[310]:

print(df)


# In[311]:

listof = df.groupby(['Team'])['PIPM'].sum()


# In[312]:

listof.sort_values()


# In[313]:

df.head()


# In[314]:

teams = df['Team'].unique()


# In[315]:

print(teams)


# In[316]:

teams = np.delete(teams, [20,31])


# In[317]:

gb = df.groupby('Team')    
dfsplit = [gb.get_group(x) for x in gb.groups]


# In[318]:

dfsplit[0].head()


# In[319]:

teams.sort()
print(teams)


# In[320]:

###check on one specific game. For example: DET at MIA


# In[321]:

pistonsPIPM = dfsplit[8]
heatPIPM = dfsplit[15]
cavsPIPM = dfsplit[5]


# In[322]:

print(pistonsPIPM)


# In[323]:

###create a total minute pipm with guesses based on last competitive game of who will play and for how long pistons
pistons_tot = 0 * pistonsPIPM['PIPM'].iloc[0]   #blake
pistons_tot += 40 * pistonsPIPM['PIPM'].iloc[1]   #drummond
pistons_tot += 25 * pistonsPIPM['PIPM'].iloc[2]   #rj
pistons_tot += 24 * pistonsPIPM['PIPM'].iloc[5]   #ish
pistons_tot += 14 * pistonsPIPM['PIPM'].iloc[6]   #LG
pistons_tot += 30 * (pistonsPIPM['PIPM'].iloc[10])   #luke
pistons_tot += 25 * pistonsPIPM['PIPM'].iloc[9]   #bruce
#thon maker
pistons_tot += 13 * -0.6
pistons_tot += 4 * pistonsPIPM['PIPM'].iloc[11]   #gr3
##ellington
pistons_tot -= 25
print(pistons_tot)


# In[324]:

print(cavsPIPM)


# In[325]:

heat_tot = 20 * heatPIPM['PIPM'].iloc[0]
heat_tot += 25 * heatPIPM['PIPM'].iloc[1]
heat_tot += 36 * heatPIPM['PIPM'].iloc[2]
heat_tot += 34 * heatPIPM['PIPM'].iloc[3]
heat_tot += 20 * heatPIPM['PIPM'].iloc[7]
heat_tot += 20 * heatPIPM['PIPM'].iloc[9]
heat_tot += 2 * heatPIPM['PIPM'].iloc[8]
heat_tot += 27 * heatPIPM['PIPM'].iloc[11]
print(heat_tot)


# In[326]:

####get RPM


# In[327]:

rpm = requests.get('http://www.espn.com/nba/statistics/rpm')


# In[328]:

doc_rpm = lh.fromstring(rpm.content)
tr_elements_rpm = doc_rpm.xpath('//tr')
col = []
i = 0
for t in tr_elements_rpm[0]:
    i+=1
    name=t.text_content()
    col.append((name,[]))
    
print(col)


# In[329]:

for j in range(1,len(tr_elements_rpm)):
    #T is our j'th row
    T=tr_elements_rpm[j]
    
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=9:
        break
    
    #i is the index of our column
    i=0
    
    #Iterate through each element of the row
    for t in T.iterchildren():
        data=t.text_content() 
        #Check if row is empty
        if i>0:
        #Convert any numerical value to integers
            try:
                data=float(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1


# In[330]:

Dict_rpm={title:column for (title,column) in col}
dfrpm=pd.DataFrame(Dict_rpm)


# In[331]:

dfrpm.head()


# In[332]:

dfrpm.shape


# In[ ]:




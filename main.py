from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

star_url='https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page=requests.get(star_url)
soup=bs(page.text,'html.parser')
star_table=soup.find('table')

temp_list=[]
table_rows=star_table.find_all('tr')

for tr in table_rows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

star_name=[]
star_dist=[]
star_rad=[]
star_mass=[]
star_lum=[]

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    star_dist.append(temp_list[i][3])
    star_rad.append(temp_list[i][6])
    star_mass.append(temp_list[i][5])
    star_lum.append(temp_list[i][7])

df=pd.DataFrame(list(zip(star_name,star_dist,star_rad,star_mass,star_lum)),columns=['star_name','star_dist','star_mass','star_rad','star_lum'])

print(df)
df.to_csv('bright_stars.csv')



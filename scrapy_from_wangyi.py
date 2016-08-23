# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 12:39:42 2016

@author: Administrator
"""


import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup
import lxml

html = urlopen("http://quotes.money.163.com/1000001.html")
soup = BeautifulSoup(html,"lxml")
# 这个地方主要是借助firebug或者chrome的F12 来确定Xpath ,或者找出关键的节点、属性 
# 获取前十大股东信息

data = soup.find_all('div',attrs={'class':'col_ml'})
# 这个时候一定要记得看data的长度，因为上式出来的结果是list
count = 0
name = []
hold_ratio = []
hold_num = []
hold_change= []


for td in data[0].find_all('td'):
    count += 1
    if count % 4 == 1:
        name.append(td.string)
    elif count % 4 == 2:
        hold_ratio.append(td.string)
    elif count % 4 == 3:
        hold_num.append(td.string)
    else :
        hold_change.append(td.string)
        
top10_df = pd.DataFrame({"name":name,"hold_ratio":hold_ratio,"hold_num":hold_num,'hold_change':hold_change})
    
top10_df = top10_df[['name','hold_ratio','hold_num','hold_change']]
    
 
# 获取财务报表
data = soup.find_all('table',attrs={'class':'table_bg001 border_box fund_analys'})        
# 获取时间表  
index_name = []    
for td in data[0].find_all('th'):
    if isinstance(td.string,str) == True:
        index_name.append(td.string)
        
 
indice = ["basic_EPS","net_value_share","cash_flow_share","return_equity",
          "main_business_income","income_main_operation","operating_profit",
          "net_profit"
          ]
 
index_lst = index_name
index_lst_1 = []
index_lst_2 = []
index_lst_3 = []
index_lst_4 = []
index_lst_5 = []
count = 0

for td in data[0].find_all('td'):   
    count += 1  
    if count % 6 ==1 :
        pass
    if count % 6 == 2:
        index_lst_1.append(td.string)
    elif count % 6 == 3:
       index_lst_2.append(td.string)
    elif count % 6 == 4:
        index_lst_3.append(td.string)
    elif count % 6 == 5:
        index_lst_4.append(td.string)
    elif count % 6 == 0:
        index_lst_5.append(td.string)
        
financial_df = pd.DataFrame({
"%s"%index_lst[0]:index_lst_1,
"%s"%index_lst[1]:index_lst_2,
"%s"%index_lst[2]:index_lst_3,
"%s"%index_lst[3]:index_lst_4,
"%s"%index_lst[4]:index_lst_5,
},index = indice)
 
        
 

     
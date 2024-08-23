# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 15:31:40 2024

@author: USER
"""


# 引進相關套件
import streamlit as st
import datetime
import requests
from io import StringIO
import pandas as pd

# st.set_option('deprecation.showPyplotGlobalUse', False)

line="""
---
"""

st.set_page_config(layout="wide")
st.title("Stock Finder")

st.markdown(line)

col1, col2 =st.columns(2)

with col1:
    # 取得日期
    date = st.date_input("Date to find: ", datetime.date(2024, 8, 23))

with col2:
    st.write("您選擇的日期: ", date)

    # 產生連線網址
    date1=str(date).replace("-","")
    url= "https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date="+date1+"&type=ALLBUT0999&response=csv"

    # 判斷網址狀態，用以跳過不存在(沒有開市)的日期
    response = requests.get(url)
    if response.text=="":
        status="Fail"
        st.write("連線狀態: ",status)
        st.write("該日期並無相關資料")
    else:
        status="Success"
        st.write("連線狀態: ",status)

st.markdown(line)

if status=="Success":
    # 資料處理，刪除ETF以及其他資料，只留股票
    clean_data=[]
    for row in response.text.split('\n'):
        fields=row.split('",')
        if len(fields) == 17 and row[0] != '=':
            clean_data.append(row.replace(' ',''))
    
    csv_data = "\n".join(clean_data)
    
    # 將抓下來的檔案，以dataframe的方式讀取
    df = pd.read_csv(StringIO(csv_data))
    
    # 將以下欄位轉為數值
    numeric_columns=['成交股數','成交筆數','成交金額','開盤價','最高價','最低價','收盤價', '本益比']
    for i in numeric_columns:
        df[i]=df[i].map(lambda x:x.replace(',', '').replace('--', ''))
        df[i]=pd.to_numeric(df[i])
    
    # 計算漲跌價差
    df["漲跌價差"] = df.apply(lambda r: 0-r["漲跌價差"] if r["漲跌(+/-)"] =='-' else r["漲跌價差"], axis=1)
    
    # 計算漲跌幅
    df["漲跌幅"] = round(df["漲跌價差"] / (df["收盤價"] - df["漲跌價差"]), 2)  
    
    # 丟掉無用的欄位
    df.drop(columns=["漲跌(+/-)","Unnamed: 16"], inplace=True)
    
    # 顯示完整表格
    pd.set_option("display.max_rows",None)
    pd.set_option("display.max_columns",None)


    if st.checkbox("顯示股票資料"):
        st.write(df)     

    if st.checkbox("顯示特定股票資料: "):
        sel=st.radio("要以何種方式選擇股票? ",["證券代號", "證券名稱"])
        if sel=="證券代號":
            num=st.selectbox("證券代號: ",
                             df["證券代號"],
                             index=None,
                             placeholder="2330")
        if sel=="證券名稱":
            num=st.selectbox("選取證券名稱",
                             df["證券名稱"],
                             index=None,
                             placeholder="台積電")
        
        if st.button("顯示"):
            st.write(df[df[sel]==num])
    
    
    
    
    if st.button("儲存 CSV 檔 "):
        # 存檔
        df.to_csv("./stock/每日收盤行情_"+date1+".csv", index=False)














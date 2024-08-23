# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 20:42:43 2024

@author: USER
"""


import streamlit as st
import datetime
import yfinance as yt
import mplfinance as mpf

# st.set_option('deprecation.showPyplotGlobalUse', False)

line="""
---
"""

st.set_page_config(layout="wide")
st.title("K-line Maker")

st.markdown(line)

cola1, cola2 =st.columns(2)

with cola1:
    # 取得日期
    date_s = st.date_input("Start: ", datetime.date(2023, 8, 22))
    date_e = st.date_input("End: ", datetime.date(2024, 8, 23))

    # 取得股票代號
    stock_inp=st.text_area("請輸入股票代號","2330")
    stock_name=stock_inp+".TW"
    
    # 選擇時間
    day0 = ["週","雙週","月","季","半年"]
    day1 = [5,10,20,60,120]

    ran = st.selectbox("觀察時間",day0)

    day= 0-day1[day0.index(ran)]

with cola2:
    # 取得歷史股價
    df = yt.download(stock_name, start=str(date_s), end=str(date_e))
        
    # 畫箱型圖
    st.write("K線")
    
    mc = mpf.make_marketcolors(up='g',down='r')
    s  = mpf.make_mpf_style(marketcolors=mc)
    plot2=mpf.plot(df[day:], type='candle', style=s)
    st.pyplot(plot2)


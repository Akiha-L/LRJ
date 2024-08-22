# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 23:48:34 2024

@author: USER
"""

import streamlit as st
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# fix 中文亂碼
plt.rcParams['font.sans-serif'] = ['Calibri'] 

# 架設網頁
st.set_page_config(layout="wide")
st.title("EDA processer")

prolog="""
操作說明:
1. 這是一個處理各種資料的程式，分成幾個部分\n
(1) 第一部分是資料處理區，可以選擇要對資料做什麼樣的處理(取log, 代號變換, One-Hot, 刪除欄位等等\n
  (2) 第二部分是資料檢閱區，可以看到資料的細節與各種作圖，會根據第一區所選擇的處理方式而變化\n
  (3) 第三部分是存檔區，可以將修改後的資料存檔，供後續使用\n
  (4) 可以輸入各種dataset的檔案名(CSV檔)，都可以解讀\n
  \n
2.  未完成版，待修正 \n
  (1) nan會被 object分類功能分為一類，導致種類變多 \n
  (2) nan會讓 One-Hot 功能 error\n
  (3) 刪除欄位的功能會造成 error (已先註解處理)\n
"""
st.write(prolog)

# dataset 檔案名稱
data_input=st.text_area("Dataset file: ","train.csv")
data_name="./EDAdata/"+data_input

# Kaggle預測，輸入文件
df0 = pd.read_csv(data_name) # 原本的文件，只顯示不刪改
df = pd.read_csv(data_name) # 用來刪改存檔的文件


# 收集數據類和物件類資料
col=list(df.columns)

datatp=[]
datatp_number=[] # 格式為int or int
datatp_obj=[] # 格式為object
datatp_del=[] # 格式為deleted ( 預計要刪掉的數據 )


for a in range(0,len(col)):
    datatp+=[df[col[a]].dtype]

for a in range(0,len(datatp)):
    if datatp[a]=="int64" or datatp[a]=="float64":
      datatp_number+=[col[a]]
    if datatp[a]=="object":
      datatp_obj+=[col[a]]
    if datatp[a]=="deleted":
      datatp_del+=[col[a]]


# 這是分隔線
line="""
---
"""

# 針對資料進行刪減區
# 顯示面板，包含數據名稱、數據種類(數字,數字log,OBJ,有序OBJ,無序OBJ,刪除)，並可選擇處理方式
pro_tag=["Numeric","Numeric(log)","Object","Object(order)","Object(not order)(one-hot)","Deleted"]

table_row=len(col)//5

st.markdown(line)
st.write("選擇個參數處理方式")
col_process=[0]*len(col)

# 欄位
tabcol1,tabcol2,tabcol3,tabcol4,tabcol5 = st.columns(5)

for k in range(0,len(col)):    
    if col[k] in datatp_number:
        aaa=0
    if col[k] in datatp_obj:
        aaa=2
    if col[k] in datatp_del:
        aaa=5
        
    if k<table_row*1+1:
        with tabcol1:
            col_process[k]=st.selectbox(col[k],pro_tag,index=aaa)
    elif k<table_row*2+1:
        with tabcol2:
            col_process[k]=st.selectbox(col[k],pro_tag,index=aaa) 
    elif k<table_row*3+1:
        with tabcol3:
            col_process[k]=st.selectbox(col[k],pro_tag,index=aaa)
    elif k<table_row*4+1:
        with tabcol4:
            col_process[k]=st.selectbox(col[k],pro_tag,index=aaa) 
    else:
        with tabcol5:
            col_process[k]=st.selectbox(col[k],pro_tag,index=aaa)
       
    

# 數據處理區

for p in range(0,len(col)):
    
    # 普通數據 (不特別處理)
    if col_process[p]==pro_tag[0]:
        pass
    
    # 普通數據 ( log處理)
    elif col_process[p]==pro_tag[1]:    
        for r in range(0,len(df[col[p]])):
            df[col[p]][r]=np.log10(df[col[p]][r])

    # 普通Object (暫時先不處理)
    if col_process[p]==pro_tag[2]:
        pass

    # 有序物件數據 (要轉變成數字)
    elif col_process[p]==pro_tag[3]:
        uni_name=list(df[col[p]].unique())
        dic={}
        
        for s in range(0,len(uni_name)):
            dic[uni_name[s]]=s
        
        df[col[p]] = df[col[p]].map(dic)

    # 無序物件數據 (one hot 處理)
    elif col_process[p]==pro_tag[4]:    
        # Scikit-learn One-hot encoding 處理方式
        from sklearn.preprocessing import OneHotEncoder
        
        ohe = OneHotEncoder()
        X2 = ohe.fit_transform(df[[col[p]]].values).toarray()
        
        set(df[col[p]].unique())
        
        # 欄位處理
        ohe_list = np.sort('is_'+df[col[p]].unique())
        df2 = pd.DataFrame(X2, columns=ohe_list)
        
        # 合併
        df = pd.concat((df.drop(col[p], axis=1), df2), axis=1)
        


    # 不採用的數據 (刪除column) (會error，先註解)
    #elif col_process[p]==pro_tag[5]:    
    #    df.drop(col[p],axis=0)




# 整體數據分析區
st.markdown(line)
st.write("整體數據分析區")

## head(10)
ck_head10 = st.checkbox("Top 10 data: ")
if ck_head10:
    st.write(df.head(10))

## info
ck_info = st.checkbox("Show data information: ")
if ck_info:
    st.write(df.info())

## describe
ck_desc = st.checkbox("Show data description: ")
if ck_desc:
    rad_desc = st.radio("Which kind of data to see? ", ["all","Quality","Quantity"]) 
    if rad_desc=="all":
        st.write(df.describe(include='all'))
    if rad_desc=="Quality":
        st.write(df.describe(include='O'))
    if rad_desc=="Quantity":
        st.write(df.describe())
        


# 單一數據分析區
st.markdown(line)
st.write("單一數據分析區")
ck_single = st.checkbox("Analysis: Single data")

#判斷data種類，並且跳到數據分析頁面 or 物件分析頁面
if ck_single:
    col_sel = st.selectbox("Date Properties (Quantity) : ",col, index=1 , placeholder="Select column")
    
    part=0
    if col_sel in datatp_number:
        part=1
    if col_sel in datatp_obj:
        part=2
    
    sp = df[col_sel]
    
    # 數據型 data
    if part==1:
        cola1,cola2,cola3 = st.columns(3)
        with cola1:
            # 長條圖
            plot1 = plt.figure()
            sns.countplot(x=sp)
            plt.title('Barplot', fontsize=20)
            st.pyplot(plot1)
            
            colaa, colab=st.columns(2)    
            with colaa:
                st.write("平均值: ",sp.mean())
                st.write("中位數: ",sp.median())
                st.write("眾數: ",sp.mode())
                
            with colab:
                st.write("各組數據統計: ",sp.value_counts())
        
        with cola2:
            # 偏態(Skewness)
            plot2 = plt.figure()
            sns.histplot(sp, kde=True)
            plt.title('Skewness', fontsize=20)
            plt.axvline(sp.mean(), color='magenta', linestyle='dashed', linewidth=2)
            plt.axvline(sp.median(), color='green', linestyle='dashed', linewidth=2)
            st.pyplot(plot2)
            
            colba, colbb=st.columns(2)    
            with colba:
                # 判斷左右偏
                skew=sp.skew()
                if skew>=1:
                    skew_text="右偏"
                if skew<=-1:
                    skew_text="左偏"
                if skew>-1 and skew<1:
                    skew_text="無偏態"
                    
                st.write("偏態: ",skew,skew_text)
                st.write("峰度: ",sp.kurt())
                st.write("最大值: ",sp.max())
                st.write("最小值: ",sp.min())
                st.write("級距(最大值-最小值): ",sp.max()-sp.min())
            with colbb:
                st.write("百分位數: ",sp.describe(np.arange(0.1, 1.0, 0.1)))
        
        with cola3:
            plot3 = plt.figure()
            sns.boxplot(sp)
            plt.title('Boxplot', fontsize=20)
            st.pyplot(plot3)
            
            st.write("樣本標準差: ",sp.var())
            st.write("母體標準差: ",sp.var(ddof=0))
            st.write("樣本變異數: ",sp.std())
            st.write("母體變異數: ",sp.std(ddof=0))
    
    # 物件型 data
    if part==2:
        colb1, colb2, colb3=st.columns(3)
        with colb1:
            # 長條圖
            plot4 = plt.figure()
            sns.countplot(x=sp)
            plt.title('Barplot', fontsize=20)
            st.pyplot(plot4)
        
        with colb2:
            uni_name=list(sp.unique())
            
            plot5 = plt.figure()
            sp.value_counts().plot.pie(title='Pie plot', labels=uni_name ) 
            plt.legend()
            st.pyplot(plot5)
        
        with colb3:
            st.write("眾數: ",sp.mode())
            st.write("各組數據統計: ",sp.value_counts())
            
            
    # other data
    if part==0:
        st.write("Wait for data input.")


# 雙數據分析區
st.markdown(line)
st.write("雙數據分析區")
ck_double = st.checkbox("Analysis: Two data")
if ck_double:   
    # 兩兩數據分析區
    col_sel1 = st.selectbox("y data : ",datatp_number, index=1 , placeholder="Select column")
    sp1 = df[col_sel1]
    col_sel2 = st.selectbox("x data : ",datatp_obj, index=1 , placeholder="Select column")
    sp2 = df[col_sel2]
    
    cola1, cola2=st.columns(2)
    with cola1:         #  箱型圖
        plot6 = plt.figure()
        plt.title("Boxplot", fontsize=20)
        sns.boxplot(x=sp2, y=sp1)
        st.pyplot(plot6)

    with cola2:         # 長條圖(數據配obj)
        plot7 = plt.figure()
        plt.title("Barplot", fontsize=20)
        sns.countplot(x=sp1, hue=sp2)
        st.pyplot(plot7)


    col_sel3 = st.selectbox("y data : ",datatp_number, index=1 , placeholder="Select y column")
    sp3 = df[col_sel3]
    col_sel4 = st.selectbox("x data : ",datatp_number, index=1 , placeholder="Select x column")
    sp4 = df[col_sel4]
    
    colb1, colb2=st.columns(2)
    with colb1:         #  散布圖
        plot7 = plt.figure()
        plt.title("Scatter plot", fontsize=20)
        sns.scatterplot(x=sp4, y=sp3)
        st.pyplot(plot7)




# 存檔區
st.markdown(line)
st.write("存檔區")
if st.button("Save Modified Dataset"):
    df.to_csv("modified_dataset.csv")



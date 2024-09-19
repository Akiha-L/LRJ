# https://docs.streamlit.io/library/cheatsheet
# streamlit run app.py
import streamlit as st
import numpy as np 
import joblib
import base64

def get_image_html(page_name, file_name):
    with open(file_name, "rb") as f:
        contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    return f'<a href="{page_name}"><img src="data:image/png;base64,{data_url}" style="width:300px"></a>'

data_url_1 = get_image_html("分類", "./pic/iris.png")
data_url_2 = get_image_html("迴歸", "./pic/taxi.png")
data_url_3 = get_image_html("辨識", "./pic/emnist.png")
data_url_4 = get_image_html("乳癌預測", "./pic/cancer.png")
data_url_5 = get_image_html("方程式", "./pic/math.png")
data_url_6 = get_image_html("梯度下降", "./pic/GD.png")
data_url_7 = get_image_html("資料處理", "./pic/EDA.png")
data_url_8 = get_image_html("每日收盤", "./pic/stock.png")
data_url_9 = get_image_html("Kline", "./pic/kline.png")
data_url_10 = get_image_html("Space", "./pic/space.png")
data_url_11 = get_image_html("titanic", "./pic/titanic.png")

st.set_page_config(
    page_title="Streamlit Program List ",
    page_icon="👋",
    layout="wide")

line="""
---
"""

st.markdown(line)
st.title('Machine Learning 學習歷程(HW)')
st.markdown(line)
cola1, cola2, cola3 = st.columns(3)
with cola1:
    st.markdown('### (分類)企鵝品種辨識')
    st.markdown('''
    ##### 特徵(X):
        - 島嶼
        - 嘴巴長度
        - 嘴巴寬度
        - 翅膀長度
        - 體重
        - 性別
    ##### 預測類別(Class):
        - Adelie
        - Chinstrap
        - Gentoo
        ''')
    st.markdown(data_url_1, unsafe_allow_html=True)
with cola2:
    st.markdown('### (迴歸)計程車小費預測')
    st.markdown('''
    ##### 特徵(X):
        - 車費
        - 性別
        - 吸菸
        - 星期
        - 時間
        - 同行人數
    ##### 目標：預測小費金額

        ''')
    st.markdown(data_url_2, unsafe_allow_html=True)
    
with cola3:
    st.markdown('### 字母辨識 EMNIST')
    st.markdown('''
    ##### 特色
        - 26個英文字母
        - 可線上手寫
        - 立即線上辨識
    ##### 字母辨識
        ''')
    st.markdown(data_url_3, unsafe_allow_html=True)




st.markdown(line)
st.title('過去曾經製作的程式')
st.markdown(line)

colb1, colb2, colb3 = st.columns(3)
with colb1:
    st.markdown('### (分類)乳癌預測 Breast Cancer')
    st.markdown('''
    ##### 特徵(X)
        - radius_mean
        - texture_mean
        - smoothness_mean
        - symmetry_mean
        - etc.
    ##### 診斷結果 (diagnosis)
        - 惡性 Malignant
        - 良性 Benign
        ''')
    st.markdown(data_url_4, unsafe_allow_html=True)
    
with colb2:
    st.markdown('### 聯立方程式求解')
    st.markdown('''
    ##### 特色:
        - 可自行輸入1~6組方程式
        - 可支援至多3個變數
    ##### 方程式求解
        - 可單獨求解
        - 可聯立求解
        ''')
    st.markdown(data_url_5, unsafe_allow_html=True)

with colb3:
    st.markdown('### 梯度下降法(Gradient Descent)')
    st.markdown('''
    ##### 這是什麼?
        - 梯度下降法(Gradient descent)是一種一階最佳
        化算法，通常也稱為最陡下降法。要使用梯度下降法找
        到一個函數的局部極小值，必須向函數上當前點對應梯
        度(或者是近似梯度)的反方向的規定步長距離點進行疊
        代搜索。如果相反地向梯度正方向疊代進行搜索，則會
        接近函數的局部極大值點；這個過程則被稱為梯度上
        升法。
    ##### 特色
        - 可以調整各項參數
        - 可以自行輸入f(x)
        ''')
    st.markdown(data_url_6, unsafe_allow_html=True)
    
    
st.markdown(line)  
colc1, colc2, colc3 = st.columns(3)

with colc1:
    st.markdown('### 探索式資料分析 EDA')
    st.markdown('''
    ##### 這是什麼?
        - 探索式資料分析EDA
        - EDA是 Exploratory Data Analysis的縮寫
        ，其實就是一種透過檢視、視覺化、統計工具這三
        個手段,從各個面向探索數據來了解資料性質、發
        現異常、分析關聯性的作法。
        
    ##### 特色
        - 可以觀察各種參數資料
        - 可以修改參數類型
        - 可以針對各參數作圖
        - 可以輸出成新的資料集
        ''')
    st.markdown(data_url_7, unsafe_allow_html=True)
    
with colc2:
    st.markdown('### 每日收盤行情')
    st.markdown('''
    ##### 功能
        - 收集指定日期之收盤行情
        - 可尋找單支股票之收盤行情
        - 計算漲跌幅
    ##### 資料來源
        - 台灣證券交易所
        ''')
    st.markdown(data_url_8, unsafe_allow_html=True)

with colc3:
    st.markdown('### K-line 產生器')
    st.markdown('''
    ##### 這是什麼
        - K線(Candlestick chart)，又稱陰陽燭、蠟
        燭線，是反映價格走勢的一種圖線，其特色在於將
        一段時間內標的價格走勢做濃縮整理，並用不同的
        顏色和形態來透露價格訊息及市場情緒，以便投資
        者進行分析

    ##### 特色
        - 自動畫 K線
        - 可選擇時間區間
        - 可選擇不同股票
        ''')
    st.markdown(data_url_9, unsafe_allow_html=True)
        

st.markdown(line)  
cold1, cold2, cold3 = st.columns(3)

with cold1:
    st.markdown('### Space Titanic')
    st.markdown('''
    ##### 特徵(X)
        - HomePlanet
        - CryoSleep
        - Destination
        - RoomService
        - ShoppingMall
        - etc.
    ##### 傳送結果 (Transported)
        - 成功 Success
        - 失敗 Fail
        ''')
    st.markdown(data_url_10, unsafe_allow_html=True) 


with cold2:
    st.markdown('### Titanic')
    st.markdown('''
    ##### 經過挑選，找出最佳模型
        - Gradient Boosting Classifier
        - Logistic Regression
        - Nearest Neighbors
        - Decision Tree
        - Random Forest
        - Naive Bayes
    ##### 生存與否 (Survived)
        - 成功 Success
        - 失敗 Fail
        ''')
    st.markdown(data_url_11, unsafe_allow_html=True) 


        
        
        
        
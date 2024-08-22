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
    st.markdown('### [(分類)企鵝品種辨識](分類)')
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
    st.markdown('### [(迴歸)計程車小費預測](迴歸)')
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
    st.markdown('### [字母辨識 EMNIST](emnist)')
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
    st.markdown('### [(分類)乳癌預測 Breast Cancer](cancer)')
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
    st.markdown('### [聯立方程式求解](equsolve)')
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
    st.markdown('### [梯度下降法(Gradient Descent)](GradientDescent)')
    st.markdown('''
    ##### 這是什麼?
        - 梯度下降法(Gradient descent)是一種一階最佳化算
        法，通常也稱為最陡下降法。要使用梯度下降法找到一個
        函數的局部極小值，必須向函數上當前點對應梯度(或者
        是近似梯度)的反方向的規定步長距離點進行疊代搜索。
        如果相反地向梯度正方向疊代進行搜索，則會接近函數
        的局部極大值點；這個過程則被稱為梯度上升法。
    ##### 特色
        - 可以調整各項參數
        - 可以自行輸入f(x)
        ''')
    st.markdown(data_url_6, unsafe_allow_html=True)
    
    
st.markdown(line)  
colc1, colc2, colc3 = st.columns(3)

with colc1:
    st.markdown('### [探索式資料分析 EDA ](EDA)')
    st.markdown('''
    ##### 這是什麼?
        - 探索式資料分析EDA
        - EDA是 Exploratory Data Analysis的縮寫，其實
        就是一種透過檢視、視覺化、統計工具這三個手段,從
        各個面向探索數據來了解資料性質、發現異常、分析
        關聯性的作法。
        
    ##### 特色
        - 可以觀察各種參數資料
        - 可以修改參數類型
        - 可以針對各參數作圖
        - 可以輸出成新的資料集
        ''')
    st.markdown(data_url_7, unsafe_allow_html=True)
    
with colc2:
    st.markdown('### [Future works]()')
    st.markdown('''
    ##### 
        - 
    ##### 
        - 
        ''')
    #st.markdown(data_url_7, unsafe_allow_html=True)

with colc3:
    st.markdown('### [Future works]()')
    st.markdown('''
    ##### 
        - 
    ##### 
        - 
        ''')
    #st.markdown(data_url_7, unsafe_allow_html=True)
        
        
        
        
        
        
        
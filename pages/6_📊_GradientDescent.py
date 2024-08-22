# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 13:48:29 2024

@author: USER
"""


import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import sympy 
import math

st.set_page_config(layout="wide")

# 取得方程式
# 作業 1-1 x^3-2*x+100
# 作業 1-2 2*x^4-3*x^2+2*x-20
# 作業 1-3 sin(x)*E^(-0.1*(x-0.6)^2)
# 作業 2-1 -5*x^2+3*x+6
st.title('梯度下降法解方程式')
st.write(" (1) 「乘法」請使用「 * 」,   「e」請使用「 E」,   「次方」請使用「 ^ 」   ")
st.write(" (2) 「三角函數」請使用「 sin, cos, tan 」,不用加「math.」，不支援「 sec, csc, cot 」")
equ0= st.text_area(" 請輸入方程式  y  =  f(x)  = ", "sin(x)*E^(-0.1*(x-0.6)^2)")

sub0=["x","^","sin","cos","tan","E"]
sub1=["z","**","sympy.sin","sympy.cos","sympy.tan","math.e"]  
# 為避免把exp的x設定成變數，後續變數使用z

for n in range(0,len(sub0)):
    equ0=equ0.replace(sub0[n], sub1[n])
equ=equ0

# 版面配置，左邊參數，右邊作圖
bigcol1,bigcol2 = st.columns(2)  

with bigcol1:

    # 求解相關參數
    col1, col2, col3 = st.columns(3)  
    with col1:    # 求最大 or 最小
        maxmin = st.radio("Max or Min ? ",["Max", "min"])
        
    
    with col2:    # 設定訓練參數
        st.write("超參數設定(Hyperparameters) ")
        
        w_start0= st.text_area("起始權重 = ", "-6",)
        w_start=float(w_start0)
    
        epochs0= st.text_area("執行週期數 = ", "10")
        epochs=int(epochs0)
    
        lr0= st.text_area("學習率 = ", "0.01")
        lr=float(lr0)
    
       
    with col3:    # 設定圖表範圍
        st.write("坐標軸設定")
        
        z_max0= st.text_area("X 坐標軸最大值 = ", "6")
        z_max=int(z_max0)
    
        z_min0= st.text_area("X 坐標軸最小值 = ", "-6")
        z_min=int(z_min0)
        
        z_interval=round((z_max-z_min)/100,2)
    
    
    
    # 建立各種f(x)
    z = sympy.Symbol('z') # 為避免把exp的x設定成變數，變數使用z
    y = eval(equ)
    yprime = y.diff(z)
    
    def f(z_value): 
        equ1=equ.replace("z", "z_value")        
        return eval(equ1)
    
    df = lambda z_value: yprime.subs(z, z_value).evalf()
    
    
    # 梯度下降法
    def GD(w_start, epochs, lr):
        global maxmin
        
        w_list = np.zeros(epochs+1)    
        w = w_start    
        w_list[0] = w
        
        # w更新 w_new = w +- learning_rate * gradient
        if maxmin=="Max":
            for i in range(epochs):
                w += lr * df(w)
                w_list[i+1] = w    
        if maxmin=="min":
            for i in range(epochs):
                w -= lr * df(w)
                w_list[i+1] = w 
        return w_list


# 畫圖
with bigcol2:

    w = GD(w_start, epochs, lr=lr) 
    print('w的變化軌跡：', np.around(w, 2))
    
    # 設定中文字型
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']  
    # 矯正負號
    plt.rcParams['axes.unicode_minus'] = False
    
    color = 'r'    
    t = np.arange(z_min, z_max, z_interval)
    
    plt.plot(t, [f(z) for z in t], c='b')
    plt.plot(w, [f(z) for z in w], label='lr={}'.format(lr))    
    plt.scatter(w, [f(z) for z in w], c=color, ) 
    
    plt.title('梯度下降法', fontsize=20)
    plt.xlabel('W', fontsize=20)
    plt.ylabel('損失函數', fontsize=20)
    plt.show()
    
    st.pyplot(plt.gcf()) # instead of plt.show()

# 顯示結果 
with bigcol1:
    with col1:   
        st.write("搜尋結果：")
        ans=[f(z) for z in w][-1]
        st.write(maxmin,":",str(round(ans,5)))
        
        st.write("找尋路徑 (最新資料至頂) :",[f(z) for z in w][::-1], )
        




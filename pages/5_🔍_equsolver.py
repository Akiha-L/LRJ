# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 17:04:40 2024

@author: USER
"""

import streamlit as st
from sympy.solvers import solve
from sympy import symbols    

st.set_page_config(layout="wide")
st.title('Equation Solver')

x,y,z = symbols("x y z")
st.write("請依序輸入方程式組")
st.write(" (1) 至多6條方程式 , 至多3個變數: x, y, z")
st.write(" (2) 「乘法」請使用「 * 」,   「除法」請使用「 / 」,   「次方」請使用「 ^ 」   ")
st.write(" (3) 可直接使用以下範例做測試 ")
        
exp=[""]*7
exp_sol=[]
fun_sol=[]

col1,col2=st.columns(2)
with col1:
    exp[0] = ""  # 第0條方程式，只是為了避免號碼錯亂
    exp[1] = st.text_area('第 1 條方程式：', "x^2-6*x=-9")
    exp[2] = st.text_area('第 2 條方程式：', "y^2-8*y=-16")
    exp[3] = st.text_area('第 3 條方程式：', "z^2-10*z=-25")
    exp[4] = st.text_area('第 4 條方程式：', "x*y*z=60")
    exp[5] = st.text_area('第 5 條方程式：', "(x^4)+(y^3)=(z^2)+120")
    exp[6] = st.text_area('第 6 條方程式：', "(7*x+3*y-5*z)/(2*x-9*y+8*z)=4/5")


with col2:
    st.title("個別方程式求解")
    for m in range(1,7):
        if st.button('方程式'+str(m)):
            if exp[m]!="" and ("=" in exp[m]) :      # 格子裡面有東西，也有等號
                fun=exp[m].replace("^","**")
                fun=fun.split("=")
                if fun[0]!="" and fun[1]!="":         # 方程式有寫完
                    check=[("x" in fun[0]) or ("x" in fun[1]) ,("y" in fun[0]) or ("y" in fun[1]),("z" in fun[0]) or ("z" in fun[1])]
                    if check.count(True)>=2:
                        st.write("變數過多，應有無限多解")            
                    elif  check.count(True)==0:
                        st.write("無變數存在，無解")
                    else:
                        fun_s=fun[0]+"-("+fun[1]+")"
                        fun_sol+=[fun_s]
                    
                        sol=solve(fun_sol)             # 製作答題內容
                        num=len(sol)
                        text=""
                        for n in range(num):
                            text+="第 "+str(n+1)+" 組解:  "+str(sol[n])+"\n\n"
                        
                        st.write("共有  "+str(num)+"  組解: ")
                        st.write(text)  
                        
    st.title("聯立方程式求解")        
    if st.button('求解'):
        cou=exp.count("")              # 計算空格數，把空格都刪掉
        for a in range(cou):
            exp.remove("")
        
        for eq in exp:                 # 整理方程式
            eq.replace("^","**")
            eq=eq.split("=")
            eq_s=eq[0]+"-("+eq[1]+")"
            exp_sol+=[eq_s]
        
        sol=solve(exp_sol)             # 製作答題內容
        num=len(sol)
        text=""
        for n in range(num):
            text+="第 "+str(n+1)+" 組解:  "+str(sol[n])+"\n\n"
        
        st.write("共有  "+str(num)+"  組解: ")
        st.write(text)





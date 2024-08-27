
import streamlit as st
import joblib

import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OneHotEncoder

# 顯示網頁畫面

st.set_page_config(page_title="Space Titanic 生存預測",layout="wide")
st.title('Space Titanic 生存預測')

labels=["PassengerId","HomePlanet","CryoSleep","Cabin","Destination",
        "Age","VIP","RoomService","FoodCourt","ShoppingMall",
        "Spa","VRDeck","Name"]
data=[0]*13

st.title("請輸入旅客資料，並進行預測")

col1, col2 ,col3, col4 = st.columns(4)
with col1:
    st.write("旅客基本資料")
    
    data[12]=st.text_area("Name","John Wick")
    
    st.write("PassengerId")
    cola1, cola2 ,cola3 = st.columns(3)
    with cola1:        
        IDa=st.selectbox("group",list(range(1,10000)))
    with cola2:
        st.write("-")
    with cola3:
        IDb=st.selectbox("number",list(range(1,5)))
    st.write("PassengerId is: "+str(IDa)+str("_")+str(IDb))
    data[0]=str(IDa)+str("_")+str(IDb)
    
    data[5]=st.selectbox("Age",list(range(80)))
    
    
with col2:
    st.write("旅程資訊")
    
    HP_list=["Europa","Earth","Mars"]
    DS_list=["55 Cancri e","PSO J318.5-22","TRAPPIST-1e"]
    data[1]=st.selectbox("HomePlanet",HP_list) 
    data[4]=st.selectbox("Destination",DS_list)
    
    
    deck_list=["A","B","C","D","E","F","G","T"]
    side_list=["P","S"]
    data[2]=st.checkbox("CryoSleep")
    st.write("Cabin")
    Cd=st.selectbox("Deck",deck_list)
    Cn=st.selectbox("Num",list(range(1000)))
    Cs=st.selectbox("Side",side_list)
    st.write("Cabin is: "+str(Cd)+str("/")+str(Cn)+str("/")+str(Cs))
    data[3]=str(Cd)+str("/")+str(Cn)+str("/")+str(Cs)


with col3:
    st.write("加價服務")    
    
    data[6]=st.checkbox("VIP")
    data[7]=st.slider("RoomService",min_value=0,max_value=30000,value=0)
    data[8]=st.slider("FoodCourt",min_value=0,max_value=30000,value=0)
    data[9]=st.slider("ShoppingMall",min_value=0,max_value=30000,value=0)
    data[10]=st.slider("Spa",min_value=0,max_value=30000,value=0)
    data[11]=st.slider("VRDeck",min_value=0,max_value=30000,value=0)


S_test=pd.DataFrame([data],columns=labels)


# ----------------------------------------


# 數據處理
S_test["group"]=S_test["PassengerId"].map(lambda x:int(x[0:4]))

HP_col1=np.array(HP_list,dtype=object)
HP_col2=np.sort("HP_is_"+HP_col1)
for i in range(0,3):
    S_test[HP_col2[i]]=int(HP_col1[i] == data[1])

DS_col1=np.array(DS_list,dtype=object)
DS_col2=np.sort("DS_is_"+DS_col1)
for i in range(0,3):
    S_test[DS_col2[i]]=int(DS_col1[i] == data[4])

S_test['CryoSleep'] = S_test['CryoSleep'].ffill()
S_test['CryoSleep'] = S_test['CryoSleep'].bfill()
S_test['CryoSleep'] = S_test['CryoSleep'].astype(int)

S_test["VIP"] = S_test["VIP"].ffill()
S_test["VIP"] = S_test["VIP"].bfill()
S_test["VIP"] = S_test["VIP"].astype(int)

S_test["Cabin"]=S_test["Cabin"].ffill()
S_test["Cabin"]=S_test["Cabin"].bfill()

S_test["C_deck"]=S_test["Cabin"].map(lambda x:x.split("/")[0])
S_test["C_num"]=S_test["Cabin"].map(lambda x:x.split("/")[1])
S_test["C_side"]=S_test["Cabin"].map(lambda x:x.split("/")[2])

deck_col1=np.array(deck_list,dtype=object)
deck_col2=np.sort("Cdeck_is_"+deck_col1)
for i in range(0,8):
    S_test[deck_col2[i]]=int(deck_col1[i] == Cd)

side_col1=np.array(side_list,dtype=object)
side_col2=np.sort("Cside_is_"+side_col1)
for i in range(0,2):
    S_test[side_col2[i]]=int(side_col1[i] == Cs)



S_test.drop(columns=['Name','PassengerId','Cabin',"HomePlanet","Destination","C_deck","C_side"], inplace=True)

avglist=["Age", "RoomService", "FoodCourt", "ShoppingMall", "Spa","VRDeck"]
for p in range(0,len(avglist)):
    S_test[avglist[p]] = S_test[avglist[p]].fillna(S_test[avglist[p]].median())

"""
---
"""

# 進行預測
# 載入模型與標準化轉換模型
SVC = joblib.load('./space/models/SVC.joblib')
DT = joblib.load('./space/models/DT.joblib')
KNN = joblib.load('./space/models/KNN.joblib')
LR = joblib.load('./space/models/LR.joblib')
NB = joblib.load('./space/models/NB.joblib')
RF = joblib.load('./space/models/RF.joblib')


# 顯示預測結果
cata = ["Fail","Success"]

with col4:
    
    if st.button('預測'):
        X_new = [S_test]
        
        st.write("SVC 的預測結果是：",cata[int(SVC.predict(S_test))])
        st.write("DT  的預測結果是：",cata[int(DT.predict(S_test))])
        st.write("KNN 的預測結果是：",cata[int(KNN.predict(S_test))])
        st.write("LR  的預測結果是：",cata[int(LR.predict(S_test))])
        st.write("NB  的預測結果是：",cata[int(NB.predict(S_test))])
        st.write("RM  的預測結果是：",cata[int(RF.predict(S_test))])








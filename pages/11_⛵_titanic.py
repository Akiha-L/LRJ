
import streamlit as st
import joblib
import pandas as pd


# 顯示網頁畫面

st.set_page_config(page_title="Titanic 生存預測",layout="wide")
st.title('Titanic 生存預測')

labels=["Name","pclass","sex","age","sibsp","parch","fare","from_Cherbourg","from_Queenstown","from_Southampton"]
data=[0]*10

st.title("請輸入旅客資料，並進行預測")

col1, col2 ,col3 = st.columns(3)
with col1:
    st.write("旅客基本資料")    
    # Name
    data[0]=st.text_area("Name","John Wick")
    # Age
    data[3]=st.selectbox("Age",list(range(80)),index=40)
    # Sex
    fem=st.selectbox("Sex",["Female","Male"])
    adu=st.selectbox("Adult",["Yes","No"])
    
    if fem == "Male":
        if adu=="Yes":
            data[2] = 0
        else:
            data[2] = 1
    else:
        data[2] = 2

    # From_where
    fw=st.selectbox("Come from which Board? ",["Cherbourg","Queenstown","Southampton"])
    if fw=="Cherbourg":
        data[7]=1
        data[8]=0
        data[9]=0 
    elif fw=="Queenstown":
        data[7]=0
        data[8]=1
        data[9]=0 
    else:
        data[7]=0
        data[8]=0
        data[9]=1 
    

with col2:
    st.write("同行人資訊")
    # Sibsp
    data[4]=st.selectbox("Brothers or Sisters or Mate",list(range(8)),index=1)
    # parch
    data[5]=st.selectbox("Parents or Children",list(range(6)))
    
    st.write("旅程資訊")
    # Pclass
    cr=st.selectbox("Class Rank",["First","Second","Third"])
    if cr=="First":
        data[1]=1
    elif cr=="Second":
        data[1]=2
    else:
        data[1]=3
    
    # fare
    data[6]=st.slider("Fare",min_value=0,max_value=520,value=400)
    

S_test=pd.DataFrame([data],columns=labels)

# ----------------------------------------

# 數據處理
S_test.drop(columns='Name', inplace=True)

# 進行預測
# 載入模型與標準化轉換模型
GDBC = joblib.load('./titanic/models/Gradient Boosting Classifier.joblib')
RF = joblib.load('./titanic/models/Random Forest.joblib')
DT = joblib.load('./titanic/models/Decision Tree.joblib')
NB = joblib.load('./titanic/models/Naive Bayes.joblib')
LR = joblib.load('./titanic/models/Logistic Regression.joblib')
KNN = joblib.load('./titanic/models/Nearest Neighbors.joblib')


# 顯示預測結果
cata = ["Fail","Success"]

with col3:
    if st.button('預測'):
        
        st.write("GDBC 的預測結果是：",cata[int(GDBC.predict(S_test))])
        st.write("DT 的預測結果是：",cata[int(DT.predict(S_test))])
        st.write("RF  的預測結果是：",cata[int(RF.predict(S_test))])
        st.write("LR  的預測結果是：",cata[int(LR.predict(S_test))])
        st.write("NB  的預測結果是：",cata[int(NB.predict(S_test))])
        st.write("KNN  的預測結果是：",cata[int(KNN.predict(S_test))])

# ----------------------------------------

"""
---
"""

res={"classifier":["GDBC","DT","RF","LR","NB","KNN"],
     "Full Name":["Gradient Boosting Classifier","Decision Tree","Random Forest","Logistic Regression","Naive Bayes","Nearest Neighbors"],
     "train_score":[0.830056, 0.825843,0.983146,0.808989,0.787921,0.751404],
     "test_score":[0.865922,0.865922,0.865922,0.854749,0.815642,0.743017,],
     "training_time":[1.796751,0.078156,0.766835, 0.604646,0.062495,0.658215]}

df_result=pd.DataFrame(data=res)

st.title("各個模型比較結果：")
df_result

p1, p2, p3 = st.columns(3)
with p1:
    st.image("./titanic/Gradient Boosting Classifier.png")
    st.image("./titanic/Logistic Regression.png")
with p2:
    st.image("./titanic/Decision Tree.png")
    st.image("./titanic/Naive Bayes.png")
with p3:
    st.image("./titanic/Random Forest.png")
    st.image("./titanic/Nearest Neighbors.png")







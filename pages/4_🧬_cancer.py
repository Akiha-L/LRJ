from sklearn import datasets
import streamlit as st
import joblib


ds = datasets.load_breast_cancer()

# 載入模型與標準化轉換模型
clf = joblib.load('./cancer/model_cancer.joblib')
scaler = joblib.load('./cancer/scaler_cancer.joblib')

st.title('乳癌（Breath Cancer）預測')

labels=ds.feature_names
lblval=[0]*30
lblmin=[5, 5, 40, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 10, 40, 180, 0, 0, 0, 0, 0, 0]
lblmax=[40, 50, 200, 2600, 0.3, 0.5, 0.5, 0.3, 0.4, 0.1, 3, 5, 25, 550, 0.05, 0.2, 0.5, 0.1, 0.1, 0.05, 40, 50, 260, 4300, 0.3, 1.1, 1.3, 0.5, 0.8, 0.3]

col1, col2 ,col3 = st.columns(3)
with col1:
    for a in range(0,10):
        lblval[a] = st.slider(str(labels[a])+':', min_value=float(lblmin[a]) , max_value=float(lblmax[a]) , value=float((lblmin[a]+lblmax[a])/2))

with col2:
    for a in range(10,20):
        lblval[a] = st.slider(str(labels[a])+':', min_value=float(lblmin[a]) , max_value=float(lblmax[a]) , value=float((lblmin[a]+lblmax[a])/2))

with col3:
    for a in range(20,30):
        lblval[a] = st.slider(str(labels[a])+':', min_value=float(lblmin[a]) , max_value=float(lblmax[a]) , value=float((lblmin[a]+lblmax[a])/2))


cata = ["Malignant","Benign"]

if st.button('預測'):
    X_new = [lblval]
    X_new = scaler.transform(X_new)
    st.write('### 預測結果是：', cata[clf.predict(X_new)[0]])

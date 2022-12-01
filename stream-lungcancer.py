import pickle
import streamlit as st

# Membaca model
lungcancer_model =  pickle.load(open('lungcancer_model.sav', 'rb'))

# Judul Web
st.title('Data Mining Prediksi Kanker Paru-Paru')

# Membagi kolom
col1, col2 = st.columns(2)

with col1 :
    GENDER = st.text_input('Jenis Kelamin (Male= 0, Female= 1)')

with col1 :
    AGE = st.text_input('Input nilai Age (21-87)')

with col1 :
    SMOKING = st.text_input('Input nilai Smoking (Yes= 2 , No= 1)')

with col1 :
    YELLOW_FINGERS = st.text_input('Input nilai Yellow Fingers (Yes= 2 , No= 1)')

with col1 :
    ANXIETY = st.text_input('Input nilai Anxiety (Yes= 2 , No= 1)')

with col1 :
    PEER_PRESSURE = st.text_input('Input nilai Peer Pressure (Yes= 2 , No= 1)')

with col1 :
    CHRONIC_DISEASE = st.text_input('Input nilai Chronic Disease (Yes= 2 , No= 1)')

with col1 :
    FATIGUE = st.text_input('Input nilai Fatigue (Yes= 2 , No= 1)')

with col2 :
    ALLERGY = st.text_input('Input nilai Allergy (Yes= 2 , No= 1)')

with col2 :
    WHEEZING = st.text_input('Input nilai Wheezing (Yes= 2 , No= 1)')

with col2 :
    ALCOHOL_CONSUMING = st.text_input('Input nilai Alcohol Consuming (Yes= 2 , No= 1)')

with col2 :
    COUGHING = st.text_input('Input nilai Coughing (Yes= 2 , No= 1)')

with col2 :
    SHORTNESS_OF_BREATH = st.text_input('Input nilai Shortness Of Breath (Yes= 2 , No= 1)')

with col2 :
    SWALLOWING_DIFFICULTY = st.text_input('Input nilai Swallowing Difficulty (Yes= 2 , No= 1)')

with col2 :
    CHEST_PAIN = st.text_input('Input nilai Chest Pain (Yes= 2 , No= 1)')

# code untuk prediksi
lungcancer_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    lungcancer_prediction = lungcancer_model.predict([[GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])

    if(lungcancer_prediction[0] == 1):
        lungcancer_diagnosis = 'Pasien mengidap kanker paru-paru'
    else:
        lungcancer_diagnosis = 'Pasien tidak mengidap kanker paru-paru'

    st.success(lungcancer_diagnosis)





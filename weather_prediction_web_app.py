import numpy as np
import pickle
import streamlit as st
import pandas as pd

loaded_model = pickle.load(open("model_pack.json", 'rb'))

df = pd.read_csv("weather_forecast.csv")
'''
# Welcome!!!
'''
def weather_prediction(input_data):
    input_data_arr = np.asarray(input_data).reshape(1, -1)
    prediction = loaded_model.predict(input_data_arr)
    if prediction[0] == 0:
        return 'Rainy day'
    else:
        return 'Sunny day'

def main():
    st.title('Weather Prediction app')
    #left_column, right_column = st.columns(2)
    #left_column.radio('Outcome', np.unique(df.weather))
    #OR
    #with left_column:
        #left_column.radio('Outcome', np.unique(df.weather))
    
    precipitation = st.slider('What is the precipitation level:', 0.0, max(df['precipitation']))
    temp_max = st.slider('What is the maximum temperature?: ', 0.0, max(df.temp_max))
    temp_min = st.slider('What is the minimum temperature?; ', 0.0, max(df.temp_min))
    wind = st.slider('What is the wind level?: ', 0.0, max(df.wind))
    weather_result = ''
    if st.button('<-Weather prediction result->'):
        weather_result = weather_prediction([precipitation, temp_max, temp_min, wind])
        st.success(weather_result)
    #col = ['precipitation', 'temp_max', 'temp_min', 'wind', 'weather']
    
    if st.button('rain'):
        new_data = [precipitation, temp_max, temp_min, wind, 'rain']
        df2 = pd.DataFrame([new_data])
        df2.to_csv("weather_database.csv", header=False, index=False, mode='a')    
    if st.button('sun'):
        new_data = [precipitation, temp_max, temp_min, wind, 'sun']
        df2 = pd.DataFrame([new_data])
        df2.to_csv("weather_database.csv", header=False, index=False, mode='a')    
            
if __name__ == '__main__':
    main()

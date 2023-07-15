# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 21:54:21 2023

@author: pc
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd

loaded_model = pickle.load(open(r"C:\Users\pc\Desktop\Practice\model_pack.json", 'rb'))

df = pd.read_csv(r"C:\Users\pc\Desktop\Practice\weather_forecast.csv")
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
    
    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    def set_state(i):
        st.session_state.stage = i

    if st.session_state.stage == 0:
        weather_result = ''
        st.button('<-Weather prediction result->', on_click=set_state, args=[1])

    if st.session_state.stage >= 1:
        #name = st.text_input('Name', on_change=set_state, args=[2])
        weather_result = weather_prediction([precipitation, temp_max, temp_min, wind])
        st.success(weather_result)
        #st.write(f'Hello {name}!')
       
        correct_val = st.selectbox('What is the right value? ', [None, 'rain', 'sun'], on_change=set_state, args=[2])
        if correct_val is None:
            set_state(1)
    if (st.session_state.stage >= 2):
        #st.write(f':{color}[Thank you!]')
        new_data = [precipitation, temp_max, temp_min, wind, correct_val]
        df2 = pd.DataFrame([new_data])
        df2.to_csv(r"C:\Users\pc\Desktop\Practice\weather_database.csv", header=False, index=False, mode='a')

        st.button('Start Over', on_click=set_state, args=[0])
if __name__ == '__main__':
    main()

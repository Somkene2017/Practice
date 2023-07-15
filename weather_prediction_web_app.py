import numpy as np
import pickle
import streamlit as st
import pandas as pd
import gspread
loaded_model = pickle.load(open(r'C:\Users\pc\Desktop\Practice\model_pack.json', 'rb'))

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
    weather_result = ''
    if st.button('<-Weather prediction result->'):
        weather_result = weather_prediction([precipitation, temp_max, temp_min, wind])
        st.success(weather_result)
    #col = ['precipitation', 'temp_max', 'temp_min', 'wind', 'weather']
    
    if st.button('rain'):
        new_data = [precipitation, temp_max, temp_min, wind, 'rain']
        df2 = pd.DataFrame([new_data])
        #df2.to_csv("weather_database.csv", header=False, index=False, mode='a')
        sheet_id = "1_ncxr889kkMLo86QuKFbH736hYSpjNgO9JAfYGv6f_Y"
        worksheet_name = "weather_database"
        # Create a Google Sheet client
        gc = gspread.service_account(r"D:\Practice 2\somkenes-project-b2926c0c60a5.json")

        # Open the Google Sheet
        sh = gc.open_by_key(sheet_id)

        # Get the worksheet
        ws = sh.worksheet(worksheet_name)

        # Append the DataFrame to the worksheet
        ws.append_rows(df2.values.tolist(), value_input_option='USER_ENTERED')
    if st.button('sun'):
        new_data = [precipitation, temp_max, temp_min, wind, 'sun']
        df2 = pd.DataFrame([new_data])
        #df2.to_csv("weather_database.csv", header=False, index=False, mode='a')    
        sheet_id = "1_ncxr889kkMLo86QuKFbH736hYSpjNgO9JAfYGv6f_Y"
        worksheet_name = "weather_database"
        # Create a Google Sheet client
        gc = gspread.service_account(r"D:\Practice 2\somkenes-project-b2926c0c60a5.json")

        # Open the Google Sheet
        sh = gc.open_by_key(sheet_id)

        # Get the worksheet
        ws = sh.worksheet(worksheet_name)

        # Append the DataFrame to the worksheet
        ws.append_rows(df2.values.tolist(), value_input_option='USER_ENTERED')
            
if __name__ == '__main__':
    main()

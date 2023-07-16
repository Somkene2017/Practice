import numpy as np
import pickle
import pandas as pd
import sklearn

loaded_model = pickle.load(open('model_pack.json', 'rb'))
input_data = (0.0, 6.1, -1.1, 5.1)
input_data_arr = np.asarray(input_data).reshape(1, -1)

prediction = loaded_model.predict(input_data_arr)
if prediction[0] == 0:
    print('Rainy day')
else:
    print('Sunny day')


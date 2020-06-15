import numpy as np
import pickle
import json

__locations = None
__model = None
__data_columns = None

def get_locations():
    return __locations

def load_columns_data():
    print('Loading Columns Data...')
    global __data_columns
    global __locations
    global __model

    with open("./columns.json",'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[4:]

    with open("./home_prices_model.pickle",'rb') as f:
        __model = pickle.load(f)
    
    print('All Files Loaded')

def make_predictions(location,sqft,bath,balcony,bhk):
    loc_index = __data_columns.index(location.lower())   #TODO : Put a try except block so if location index is not found then set other as 1
    x = np.zeros(len(__data_columns))
    
    x[0] = sqft
    x[1] = bath
    x[2] = balcony
    x[3] = bhk
    loc_index = 10
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0][0],2)

if __name__ == '__main__':
    load_columns_data()
    print(get_locations())
    print(make_predictions('Rajaji Nagar', 3000, 2, 1, 3))
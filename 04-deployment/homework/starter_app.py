#!/usr/bin/env python
# coding: utf-8

import sys
import pickle
import pandas as pd

from flask import Flask
from flask import request
from flask import jsonify


def load_model():
    with open('model.bin', 'rb') as f_in:
        dv, model = pickle.load(f_in)
    return dv, model

def read_data(filename):
    df = pd.read_parquet(filename)

    categorical = ['PULocationID', 'DOLocationID']
    
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df

app = Flask('duration-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    arg = request.get_json()
    year = arg["year"]
    month = arg["month"]
    file_name = f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{year:04d}-{month:02d}.parquet'
    print("Filename : "+file_name)
    df = read_data(file_name)

    categorical = ['PULocationID', 'DOLocationID']
    dicts = df[categorical].to_dict(orient='records')
    dv, model = load_model()
    X_val = dv.transform(dicts)
    y_pred = model.predict(X_val)

    return jsonify({'Mean prediction':y_pred.mean()})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
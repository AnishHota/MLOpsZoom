import pickle

from flask import Flask
from flask import request
from flask import jsonify
import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient(tracking_uri="http://127.0.0.1:5000")

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("models-experiment")

logged_model = 'runs:/09ea924d01d943d090abc307b04dcb0e/model'

# Load model as a PyFuncModel.
model = mlflow.pyfunc.load_model(logged_model)

dv_path = client.download_artifacts(run_id="09ea924d01d943d090abc307b04dcb0e", path="preprocessor/preprocessor.b")

print(f"Downloading the dict vectorizer to {dv_path}")

with open(dv_path,'rb') as f_in:
    dv = pickle.load(f_in)


def prepare_features(ride):
    features = {
        'PU_DO': '%s_%s' % (ride["PULocationID"], ride["DOLocationID"]),
        'trip_distance': ride["trip_distance"]
    }
    return features

def predict(features):
    X = dv.transform([features])
    preds = model.predict(X)
    return float(preds[0])

app = Flask('duration-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()
    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration': pred
    }

    return jsonify(result)

if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
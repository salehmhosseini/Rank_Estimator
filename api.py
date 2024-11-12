from flask import Flask, request, jsonify
import numpy as np
import joblib

# Load Models
model_riazi_filename = 'konkoor_rank_predictor_model_riazi.pkl'
model_riazi = joblib.load(model_riazi_filename)

model_tajrobi_filename = 'konkoor_rank_predictor_model_tajrobi.pkl'
model_tajrobi = joblib.load(model_tajrobi_filename)

model_ensani_filename = 'konkoor_rank_predictor_model_ensani.pkl'
model_ensani = joblib.load(model_ensani_filename)

app = Flask(__name__)

# use models
def predict_rank_riazi(taraz, user_region):
    return model_riazi.predict([[taraz, user_region]])[0]

def predict_rank_tajrobi(taraz, user_region):
    return model_tajrobi.predict([[taraz, user_region]])[0]

def predict_rank_ensani(taraz, user_region):
    return model_ensani.predict([[taraz, user_region]])[0]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    taraz_moadel = data['taraz_moadel']
    taraz_konkoor = data['taraz_konkoor']
    reshte = data['reshte']
    region = data['region']

    total_taraz = (taraz_konkoor + taraz_moadel) / 2

    if reshte == 1:
        rank = int(predict_rank_riazi(total_taraz, region))
    elif reshte == 2:
        rank = int(     (total_taraz, region))
    elif reshte == 3:
        rank = int(predict_rank_ensani(total_taraz, region))
    else:
        return jsonify({'error': 'Invalid reshte value'}), 400

    return jsonify({'rank': rank})

if __name__ == '__main__':
    app.run(debug=True)




''' 
input with curl example : 

curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{
    "taraz_moadel": 7500,
    "taraz_konkoor": 7200,
    "reshte": 1,
    "region": 2
}'

'''
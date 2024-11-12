from flask import Flask, request, jsonify, render_template
import numpy as np
import joblib

app = Flask(__name__)

# Load Models
try:
    model_riazi = joblib.load('konkoor_rank_predictor_model_riazi.pkl')
    model_tajrobi = joblib.load('konkoor_rank_predictor_model_tajrobi.pkl')
    model_ensani = joblib.load('konkoor_rank_predictor_model_ensani.pkl')
except FileNotFoundError as e:
    print(f"Error: {e}. Make sure all mod   el files are in the correct directory.")
    exit(1) 

def predict_rank(model, taraz, user_region):
    return model.predict([[taraz, user_region]])[0]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        
        taraz_moadel = float(data['taraz_moadel'])
        taraz_konkoor = float(data['taraz_konkoor'])
        reshte = int(data['reshte'])
        region = int(data['region'])

        if not (1 <= reshte <= 3) or not (1 <= region <= 5):
            return jsonify({'error': 'Invalid reshte or region value'}), 400

        total_taraz = (taraz_konkoor + taraz_moadel) / 2

        if reshte == 1:
            rank = int(predict_rank(model_riazi, total_taraz, region))
        elif reshte == 2:
            rank = int(predict_rank(model_tajrobi, total_taraz, region))
        else:  # reshte == 3
            rank = int(predict_rank(model_ensani, total_taraz, region))

        return jsonify({'rank': rank})
    
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {str(e)}'}), 400
    except ValueError as e:
        return jsonify({'error': f'Invalid input type: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'An unexpected error occurred: {str(e)}'}), 500

if __name__ == '__main__':  
    app.run(debug=True)

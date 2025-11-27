from flask import Flask, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Load your model and scaler with error handling
try:
    model = joblib.load('heartModel.joblib')
    scaler = joblib.load('heartScaler.joblib')
    logger.info("Model and scaler loaded successfully")
except Exception as e:
    logger.error(f"Error loading model or scaler: {e}")
    model = None
    scaler = None

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None or scaler is None:
            return jsonify({'error': 'Model not loaded properly'}), 500
            
        data = request.json
        logger.info(f"Received data: {data}")
        
        # Extract features in the correct order as used in training
        features = [
            int(data['HighBP']),
            int(data['HighChol']),
            float(data['BMI']),
            int(data['Smoker']),
            int(data['Stroke']),
            int(data['Diabetes']),
            int(data['PhysActivity']),
            int(data['Fruits']),
            int(data['Veggies']),
            int(data['HeavyAlcohol']),
            int(data['GenHlth']),
            int(data['MentHlth']),
            int(data['PhysHlth']),
            int(data['Sex']),
            int(data['Age']),
            int(data['Education']),
            int(data['Income'])
        ]
        
        logger.info(f"Features array: {features}")
        
        # Scale features
        features_scaled = scaler.transform([features])
        logger.info(f"Scaled features shape: {features_scaled.shape}")
        
        # Predict
        prediction = model.predict(features_scaled)[0]
        logger.info(f"Prediction: {prediction}")
        
        return jsonify({'prediction': int(prediction)})
        
    except Exception as e:
        logger.error(f"Error in prediction: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'model_loaded': model is not None})

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
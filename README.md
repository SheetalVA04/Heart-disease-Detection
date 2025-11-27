# Heart Disease Detection App

A machine learning-based web application for heart disease risk assessment using Flask and scikit-learn.

## Features

- 🏥 AI-powered heart disease risk assessment
- 📊 Beautiful and responsive web interface
- 🔍 Real-time predictions
- 📱 Mobile-friendly design

## Quick Start

### Option 1: Using the helper script (Recommended)

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   python run_app.py
   ```

3. **Open in browser:**
   - Open `index.html` in your browser, or
   - Go to `http://127.0.0.1:5000` (if Flask serves the HTML)

### Option 2: Manual setup

1. **Install dependencies:**
   ```bash
   pip install flask flask-cors joblib numpy scikit-learn
   ```

2. **Run Flask app:**
   ```bash
   python app.py
   ```

3. **Open the HTML file:**
   - Open `index.html` in your web browser

## Troubleshooting

### "Error contacting server" message

This usually means the Flask server isn't running. Here's how to fix it:

1. **Make sure Flask is running:**
   - Open a terminal/command prompt
   - Navigate to the project directory
   - Run: `python app.py`
   - You should see: `Running on http://127.0.0.1:5000`

2. **Check if the server is accessible:**
   - Open your browser
   - Go to: `http://127.0.0.1:5000/health`
   - You should see: `{"status": "healthy", "model_loaded": true}`

3. **Common issues:**
   - **Port 5000 in use:** Change the port in `app.py` to 5001 or another free port
   - **Firewall blocking:** Allow Python/Flask through your firewall
   - **Missing dependencies:** Run `pip install -r requirements.txt`

### Model loading errors

If you see model loading errors:

1. **Check model files exist:**
   - `heartModel.joblib`
   - `heartScaler.joblib`

2. **Recreate models if needed:**
   - Run the Jupyter notebook `HTfinal.ipynb`
   - Export the trained model and scaler

## File Structure

```
Heart disease Detection/
├── app.py              # Flask backend server
├── index.html          # Web interface
├── styles.css          # CSS styling
├── heartModel.joblib   # Trained ML model
├── heartScaler.joblib  # Feature scaler
├── run_app.py          # Helper script to run the app
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── HTfinal.ipynb       # Jupyter notebook with model training
```

## Model Information

The app uses a Logistic Regression model trained on heart disease data with the following features:

- High Blood Pressure
- High Cholesterol
- BMI (Body Mass Index)
- Smoking status
- Stroke history
- Diabetes
- Physical activity
- Fruit consumption
- Vegetable consumption
- Heavy alcohol consumption
- General health rating
- Mental health days
- Physical health days
- Sex
- Age
- Education level
- Income level

## API Endpoints

- `POST /predict` - Get heart disease prediction
- `GET /health` - Check server and model status

## License

This project is for educational purposes. Always consult healthcare professionals for medical advice. 
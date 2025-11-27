#!/usr/bin/env python3
"""
Simple script to run the Heart Disease Detection Flask app
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required packages are installed"""
    required_packages = ['flask', 'flask-cors', 'joblib', 'numpy', 'scikit-learn']
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print("❌ Missing required packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\n📦 Install them using:")
        print(f"   pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ All required packages are installed")
    return True

def check_model_files():
    """Check if model files exist"""
    required_files = ['heartModel.joblib', 'heartScaler.joblib']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing model files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\n🔧 Please make sure the model files are in the current directory")
        return False
    
    print("✅ All model files found")
    return True

def main():
    print("🏥 Heart Disease Detection App")
    print("=" * 40)
    
    # Check dependencies
    if not check_dependencies():
        return
    
    # Check model files
    if not check_model_files():
        return
    
    print("\n🚀 Starting Flask app...")
    print("📱 Open your browser and go to: http://127.0.0.1:5000")
    print("🔗 Or open the index.html file directly")
    print("\n⏹️  Press Ctrl+C to stop the server")
    print("-" * 40)
    
    try:
        # Run the Flask app
        subprocess.run([sys.executable, 'app.py'])
    except KeyboardInterrupt:
        print("\n👋 Server stopped by user")
    except Exception as e:
        print(f"\n❌ Error running Flask app: {e}")

if __name__ == "__main__":
    main() 
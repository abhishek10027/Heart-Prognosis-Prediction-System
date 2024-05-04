from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
from joblib import load
import pandas as pd

# Load the trained machine learning model
model = load('E:\Web Development\Project\HeartSafePrognosisPredictionSystem\savedModels\model.joblib')

def predictor(request):
    return render(request, 'main.html')

def formInfo(request):
    try:
        # Extract user inputs from the request
        Smoking = int(request.GET.get('Smoking', -1))
        Stroke = int(request.GET.get('Stroke', -1))
        PhysicalHealth = int(request.GET.get('PhysicalHealth', -1))
        DiffWalking = int(request.GET.get('DiffWalking', -1))
        AgeCategory = int(request.GET.get('AgeCategory', -1))
        Diabetic = int(request.GET.get('Diabetic', -1))
        PhysicalActivity = int(request.GET.get('PhysicalActivity', -1))
        BMI = float(request.GET.get('BMI', -1))
        KidneyDisease = int(request.GET.get('KidneyDisease', -1))

        # Create a DataFrame with the user inputs
        new_input = pd.DataFrame({
            'Smoking': [Smoking],
            'Stroke': [Stroke],
            'PhysicalHealth': [PhysicalHealth],
            'DiffWalking': [DiffWalking],
            'AgeCategory': [AgeCategory],
            'Diabetic': [Diabetic],
            'PhysicalActivity': [PhysicalActivity],
            'BMI': [BMI],
            'KidneyDisease': [KidneyDisease]
        })

        # Use the loaded model to predict the outcome
        predicted_class = model.predict(new_input)

        # Map predictions to human-readable labels
        predicted_class_label = "Heart Disease" if predicted_class[0] == 1 else "No Heart Disease"

        # Render the result.html template with the prediction result
        return render(request, 'result.html', {"predicted_class_label": predicted_class_label})

    except MultiValueDictKeyError:
        # Handle missing keys in the request
        error_message = "Please provide values for all required fields."
        return render(request, 'error.html', {"error_message": error_message})
    except ValueError as e:
        # Handle value conversion errors
        error_message = f"ValueError: {e}"
        return render(request, 'error.html', {"error_message": error_message})

# Heart-Prognosis-Prediction-System


The Heart Disease Predictor Application is a web-based platform designed to predict the likelihood of heart disease using machine learning techniques. It allows users to input various health metrics and obtain accurate predictions regarding their risk of heart-related ailments.

## Project Description

The Heart Disease Predictor System utilizes advanced machine learning algorithms to forecast heart disease based on factors such as smoking habits, age, physical health, and more. It provides precise predictions crucial for diagnosis and prevention.

## Features

- **User-friendly interface:** The frontend interface is designed to be intuitive and easy to navigate.
- **Accurate predictions:** The system utilizes machine learning algorithms to provide accurate predictions based on inputted health data.
- **Responsive design:** The application is responsive and works seamlessly across different devices and screen sizes.

## Model Selection

The best model for predicting heart disease is selected based on accuracy. The following models are evaluated:

1. **KNeighborsClassifier:** Simple and effective classification algorithm.
2. **LogisticRegression:** Classic classification algorithm known for its simplicity and interpretability.
3. **DecisionTreeClassifier:** Versatile classification algorithm capable of capturing complex decision boundaries.
4. **LinearSVC:** Variant of Support Vector Machine suitable for linearly separable data.

The accuracy of each model is calculated on the test dataset, and the **Logistic Regression model**,  is chosen as one of the models for prediction.

## New User Input for Prediction

To predict the likelihood of heart disease for a new user, the application requires the following significant features:

- Smoking (1 for Yes, 0 for No)
- Stroke (1 for Yes, 0 for No)
- Physical Health Score
- Difficulty Walking (1 for Yes, 0 for No)
- Age Category
- Diabetic (1 for Yes, 0 for No)
- Physical Activity (1 for Yes, 0 for No)
- Body Mass Index (BMI)
- Kidney Disease (1 for Yes, 0 for No)

Fill out the form with the appropriate values for each feature and submit to generate the prediction result.

## Dependencies

- Django: 3.2.4
- Python: 3.9.5

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Run the Django development server:
   ```bash
   python manage.py runserver
   ```

3. Open the application in a web browser at http://localhost:8000.


## This project is developed by Abhishek Kushwaha

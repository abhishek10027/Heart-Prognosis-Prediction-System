# Heart-Prognosis-Prediction-System

This project is a web-based application designed to predict heart disease using machine learning techniques. It is developed with Django for the backend functionality and HTML, CSS, and JavaScript for the frontend interface. The application analyzes various health metrics inputted by the user to deliver accurate predictions regarding the likelihood of heart disease.


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

The accuracy of each model is calculated on the test dataset, and the **Logistic Regression model** is chosen as one of the models for prediction.

## Steps for Prediction

1. *Open the application in a web browser.*

   ![home_r1](https://github.com/abhishek10027/Heart-Prognosis-Prediction-System/assets/132592735/4c92ec35-ebaa-403e-924c-fa47513ab806)

2. *Click on the "Let's Predict" button to input your health data.*

   ![form_r1](https://github.com/abhishek10027/Heart-Prognosis-Prediction-System/assets/132592735/0a0191a9-27e1-46d1-8464-89125c75d046)

3. *Fill out the form with relevant information such as smoking habits, age, physical health score, etc.*
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

4. *Click the "Submit" button to generate the prediction result.*
5. *View the prediction result to see the likelihood of heart disease.*

   ![result_r1](https://github.com/abhishek10027/Heart-Prognosis-Prediction-System/assets/132592735/8bd34c07-b5a7-45e2-91cc-4b05cc8d171f)


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

3. Open the application in a web browser at like http://localhost:8000.

## Conclusion

The Heart-Prognosis-Prediction-System is a powerful tool designed to assist in the early detection and prevention of heart disease. By leveraging machine learning techniques and a user-friendly interface, the application provides accurate predictions based on inputted health data.

With its responsive design and precise predictions, this system aims to empower individuals to take proactive steps towards maintaining heart health. By identifying risk factors and providing personalized insights, it contributes to better healthcare outcomes and enhances overall well-being.

The accuracy of the Heart-Prognosis-Prediction-System's prediction models is an impressive 99%, ensuring reliable and trustworthy results for users. This high level of accuracy instills confidence in the system's ability to make informed predictions and assist healthcare professionals in making timely interventions.

As the project continues to evolve, future enhancements may include incorporating additional features, expanding the dataset for improved accuracy, and integrating with healthcare systems for seamless patient care.

With a commitment to innovation and excellence, the Heart-Prognosis-Prediction-System remains dedicated to advancing heart disease prediction and prevention for the betterment of society.

## About the Developer

This project is developed by **Abhishek Kushwaha**.

**LinkedIn:** https://www.linkedin.com/in/abhishek10027

**GitHub:**  https://github.com/abhishek10027

🚀🔍📈

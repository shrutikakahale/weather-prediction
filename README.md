# Seattle Weather Prediction App

This project is a Flask web application that predicts the weather condition in Seattle based on user inputs, using a logistic regression model. The model is trained on the Seattle weather dataset and can classify weather conditions based on input features like precipitation, minimum temperature, maximum temperature, and wind speed.

## Features
- Flask-based web application with a simple user interface.
- Logistic regression model using `scikit-learn` to predict weather conditions.
- Accepts user inputs for features like precipitation, minimum temperature, maximum temperature, and wind speed.
- Displays the predicted weather condition on the web page.

## Prerequisites
- Python 3.x
- Flask
- Pandas
- scikit-learn
## How It Works
The Flask app loads the seattle-weather.csv dataset using Pandas.
Features are extracted, and one-hot encoding is applied to handle categorical data.
The data is split into training and testing sets, and a logistic regression model is trained using scikit-learn.
The app provides a form where users can input:
Precipitation
Minimum Temperature
Maximum Temperature
Wind Speed
The user inputs are processed, and the trained model predicts the weather condition.
The predicted weather condition is displayed on the web page.
Example<br>
Input Fields:<br>

Precipitation: 0.5<br>
Min Temp: 45.0<br>
Max Temp: 55.0<br>
Wind: 10.0<br>
Prediction Output:<br>

Predicted Condition: Rain

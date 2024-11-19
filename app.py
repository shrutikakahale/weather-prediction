from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

app = Flask(__name__)

# Load the dataset
data = pd.read_csv("seattle-weather.csv")

# Select relevant features
features = data.iloc[:, 1:5]

# Select the target variable
targets = data['weather']

# Convert categorical features to numerical using one-hot encoding
features = pd.get_dummies(features)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, targets, test_size=0.2, random_state=42)

# Create a Logistic Regression model
classifier = LogisticRegression(max_iter=1000, random_state=42)

# Train the model on the training set
classifier.fit(X_train, y_train)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        user_precipitation = float(request.form['precipitation'])
        user_min_temp = float(request.form['min_temp'])
        user_max_temp = float(request.form['max_temp'])
        user_wind = float(request.form['wind'])

        user_input = pd.DataFrame({
            'temperature_min': [user_min_temp],
            'precipitation': [user_precipitation],
            'temperature_max': [user_max_temp],
            'wind': [user_wind],
        })

        # Convert categorical features to numerical using one-hot encoding
        user_input_encoded = pd.get_dummies(user_input)

        # Ensure the order of columns in user input matches the order during training
        user_input_encoded = user_input_encoded.reindex(columns=X_train.columns, fill_value=0)

        # Predict the condition
        predicted_condition = classifier.predict(user_input_encoded)

        return render_template('home.html', prediction=f'Predicted Condition: {predicted_condition[0]}')


if __name__ == '__main__':
    app.run(debug=True)

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data():
    data = pd.read_csv('deep_learning/loan_data.csv')
    return data

def preprocess_data(data):
    data = data.dropna()

    numerical_features = ['base_cost', 'interest_rate', 'admin_cost', 'num_years']
    scaler = StandardScaler()
    data[numerical_features] = scaler.fit_transform(data[numerical_features])

    data['interest_amount'] = data['base_cost'] * data['interest_rate'] * data['num_years']
    X = data[['base_cost', 'interest_rate', 'admin_cost', 'num_years', 'interest_amount']]
    y = data['total_cost']

    return X, y, scaler

def train_model(data):
    X, y, scaler = preprocess_data(data)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    return model, scaler

def make_prediction(base_cost, interest_rate, admin_cost, num_years, model, scaler):
    input_data = pd.DataFrame({'base_cost': [base_cost],
                                'interest_rate': [interest_rate],
                                'admin_cost': [admin_cost],
                                'num_years': [num_years]})

    input_data_scaled = scaler.transform(input_data)
    prediction = model.predict(input_data_scaled)

    return prediction[0]
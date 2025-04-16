import requests 

data = {
    "house_price_regression_dataset.csv/Square_Footage": 1800,
    "house_price_regression_dataset.csv/Num_Bedrooms": 3,
    "house_price_regression_dataset.csv/Num_Bathrooms": 2,
    "house_price_regression_dataset.csv/Year_Built": 2010,
    "house_price_regression_dataset.csv/Lot_Size": 0.25,
    "house_price_regression_dataset.csv/Garage_Size": 2,
    "house_price_regression_dataset.csv/Neighborhood_Quality": 8
}

url = 'http://127.0.0.1:5000/predict' 
 
 
response = requests.post(url, json=data) 
 

if response.status_code == 200: 
    prediction = response.json() 
    print(f"Predicted price is: {prediction['Prediction'][0]:.2f}") 
else: 
    print(f'API Request Failed with Status Code: {response.status_code}') 
    print(f'Response Content: {response.text}') 
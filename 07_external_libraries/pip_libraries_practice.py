# Fetch Bitcoin Price from API
import requests
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("Bitcoin Price (USD):", data['bitcoin']['usd'])
else:
    print("Failed to fetch data")



# Another Example 
import requests
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,pkr"
response = requests.get(url)     # Call API
if response.status_code == 200:
    data = response.json()
    print("Bitcoin Price USD:", data['bitcoin']['usd'])
    print("Bitcoin Price PKR:", data['bitcoin']['pkr'])
else:
    print("Failed to fetch data")



import requests
url = "https://httpbin.org/post"        #--< API Endpoint #httpbin   testing website ... just check request
data = {"name": "Momin", "task": "AI Practice"}
response = requests.post(url, json=data)
print(response.json())



# Pandas library ... Data Anlysis
import pandas as pd
df = pd.read_csv("dataa.csv")

print(df.head())     # first 5 rows
print(df.tail())     # last 5 rows

print(df.shape)      # Tell no of columns and rows

print(df.columns)    # Tell name of columns

print(df.info())     # data types + null values

print(df.describe())   # Give mean and max

print(df.isnull().sum())   # Checking missing values 

print(df.dropna())       # remove missing values


# Fill Missing Values 
print(df.fillna(0))
# print(df.fillna(df['Cause'].mean()))  

# Data Selection & Filtering
print(df['Data_value'])

print(df[df['Data_value'] > 50])
print(df[df['Cause'] == 'Pedestrian'])

df['price'].mean()
df['price'].sum()
df['price'].max()

# df.groupby('category')['price'].mean()

print(df.sort_values('Data_value'))




# Create CSV Report using Pandas
import requests
import pandas as pd
from datetime import datetime

# To fetch data
url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    price = data['bitcoin']['usd']
    time = datetime.now().strftime("%I-%M_%p")
    df = pd.DataFrame({
        "Currency": ["Bitcoin"],
        "Price_USD": [price],
        "Time": [time]
    })
    df.to_csv("btc_report.csv", index=False)
    print("CSV File saved Successfully")
    print(df)
else:
    print("Failed to fetch data")
    
# Read CSV and Perform Analysis
df = pd.read_csv("btc_report.csv")
print("Max BTC Price:", df['Price_USD'].max())

high_prices = df[df["Price_USD"] > 20000]
print("High Prices:\n", high_prices)


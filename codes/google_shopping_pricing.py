import pandas as pd
import requests

# Structure payload
payload = {
   'source': 'google_shopping_search',
   'domain': 'com',
   'query': 'levis',
   'pages': 1,
   'context': [
       {'key': 'sort_by', 'value': 'pd'},
       {'key': 'min_price', 'value': 30},
   ],
   'parse': 'true',
}

# Get response
response = requests.request(
   'POST',
   'https://realtime.oxylabs.io/v1/queries',
   auth=('username', 'password'),
   json=payload,
)

#Get the content from the response
result=response.json()['results'][0]['content']
products = result['results']['organic']

#Create a DataFrame
df = pd.DataFrame(columns=['Product Title', 'Price', 'Store'])

#iterate through all the products
for p in products:
    title = p['title']
    price = p['price_str']
    store = p['merchant']['name']
    df = pd.concat([pd.DataFrame([[title, price, store]], columns=df.columns),
                   df], ignore_index=True)

#Copy the DataFrame to CSV and JSON files
df.to_csv('google_shopping_search.csv' ,index=False)
df.to_json('google_shopping_search.json', orient='split', index=False)

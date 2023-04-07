import pandas as pd  # include the pandas library for DataFrame
import requests  # Include the requests library

# Structure payload.
payload = {
   'source': 'google_shopping_pricing',
   'domain': 'com',
   'query': '4505166624001087642',
   'parse': 'true'
}

# Get response.
response = requests.request(
   'POST',
   'https://realtime.oxylabs.io/v1/queries',
   auth=('username', 'password'),
   json=payload,
)

# Get the content from the response
result = response.json()['results'][0]['content']
print (response.json())
title = result['title']
pricing = result['pricing']
# Create a DataFrame
df = pd.DataFrame(columns=['Product Name', 'Special Offer',
                          'Item Price', 'Total Price', 'Shipping'])

for p in pricing:
    offer = p['details']
    item_price = p['price']
    total_price = p['price_total']
    shipping = p['price_shipping']
    df = pd.concat([pd.DataFrame([[title, offer, item_price,
                                  total_price, shipping]], columns=df.columns), df],
                  ignore_index=True)

# Copy the DataFrame to CSV and JSON files
df.to_csv('google_shopping_pricing.csv', index=False)
df.to_json('google_shopping_pricing.json', orient='split', index=False)

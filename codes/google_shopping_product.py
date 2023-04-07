import pandas as pd
import requests

# Structure payload.
payload = {
  'source': 'google_shopping_product',
  'domain': 'com',
  'query': '4505166624001087642',
  'parse': 'true',
}

# Get response.
response = requests.request(
  'POST',
  'https://realtime.oxylabs.io/v1/queries',
  auth=('username', 'password'),
  json=payload,
)

# Get the content
product=response.json()['results'][0]['content']

# create a DataFrame
df = pd.DataFrame(columns=['Product Title', 'Product Details',
                          'Highlights', 'Rating', 'Reviews Count'])

# Get the elements from the response object
title = product['title']
details = product['description']
highlights = product['highlights']
rating = product['reviews']['rating']
reviews_count = product['reviews']['reviews_count']

# Add all the elements in DataFrame
df = pd.concat([pd.DataFrame([[title, details, highlights, rating, reviews_count]],
                           columns=df.columns), df], ignore_index=True)

# Copy the data in CSV and JSON file
df.to_csv('google_shopping_product.csv', index=False)
df.to_json('google_shopping_product.json', orient = 'split', index = False)

# Print the data on screen
print ('Product Name: ' + title)
print ('Product Details: ' + details)
print ('Product Highlights: ' + str(highlights))
print ('Product Rating: ' + str(rating))
print ('Reviews Count: ' + str(reviews_count))

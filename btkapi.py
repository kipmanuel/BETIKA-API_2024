import requests
import pandas as pd

# Define the URLs for the API requests
urls = [
    "https://api.betika.com/v1/uo/matches?page=1&limit=20&tab=upcoming&sub_type_id=1%2C186%2C340&sport_id=14&tag_id=&competition_id=14482&sort_id=2&period_id=9&esports=false",
    "https://api.betika.com/v1/uo/matches?page=1&limit=20&tab=upcoming&sub_type_id=1%2C186%2C340&sport_id=14&tag_id=&competition_id=214&sort_id=2&period_id=9&esports=false",
    "https://api.betika.com/v1/uo/matches?page=1&limit=20&tab=upcoming&sub_type_id=1,186,340&sport_id=14&tag_id=&competition_id=209&sort_id=2&period_id=9&esports=false",
    "https://api.betika.com/v1/uo/matches?page=1&limit=20&tab=upcoming&sub_type_id=1,186,340&sport_id=14&tag_id&competition_id=222&sort_id=2&period_id=9&esports=false",
    "https://api.betika.com/v1/uo/matches?page=1&limit=20&tab=upcoming&sub_type_id=1,186,340&sport_id=14&tag_id=&competition_id=182&sort_id=2&period_id=9&esports=false"
]

# Define common headers for all requests
headers = {
    'cookie': "__cf_bm=w8ud.1gXqMar.l245f9mF0n8srQwSBVnYwsNhx4j9z0-1711281581-1.0.1.1-w25at5S8UbXzD3eDiwPoYGtf7scbIqwAnOM_jMbybqkaAc7jd41J5bwpTH33F1ZUGpAan_fHCuoT1fUe_iw3jQ",
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://www.betika.com/',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"'
}

# Create an empty list to store data from all requests
all_data = []

# Perform GET requests for each URL and append data to the list
for url in urls:
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        all_data.extend(data['data'])
    else:
        print(f"Failed to fetch data from URL: {url}")

# Create a DataFrame from the accumulated data
df = pd.DataFrame(all_data)

# Save the DataFrame to a CSV file
df.to_csv('upcoming.csv', index=False)


import requests
import json
import pprint

trip_start_month = '05'
trip_start_day = '05'
trip_start_year = '2019'
trip_start_date = "{}-{}-{}".format(trip_start_year, trip_start_month, trip_start_day)
trip_end_month = '05'
trip_end_day = '09'
trip_end_year = '2019'
trip_end_date = "{}-{}-{}".format(trip_end_year , trip_end_month, trip_end_day)
trip_start_location = input('Airport code for your city: ')

#TRIPS PORTION
response = requests.get("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/{}/anywhere/{}?inboundpartialdate={}".format(trip_start_location, trip_start_date, trip_end_date),
  headers={
    "X-RapidAPI-Key": "85c2cae2d1msh4f45b5e5f5f7ffep19de73jsnf513195c7a59"})
response_text = response.text
response_data = json.loads(response_text)
routes = response_data['Routes']
routes_with_lowest_price = []
for route in routes:
    if 'QuoteIds' in route:
        routes_with_lowest_price.append(route)
cheapest_sort = sorted(routes_with_lowest_price, key=lambda i: i['Price'])
pprint.pprint(cheapest_sort)
InputPlaceName = input('Enter Place Name')

place_name = [response_data['Places']]

#PLACES LIST API
places = requests.get("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/?query={}".format(InputPlaceName),
  headers={
    "X-RapidAPI-Key": "85c2cae2d1msh4f45b5e5f5f7ffep19de73jsnf513195c7a59"
  }
)
response_text2 = places.text
response_data2 = json.loads(response_text2)
pprint.pprint(response_data2)




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
quotes = response_data['Quotes']
places = response_data['Places']
carriers = response_data['Carriers']
currencies = response_data['Currencies']
# pprint.pprint(quotes)

routes_with_lowest_price = []
for route in routes:
    if 'QuoteIds' in route:
        routes_with_lowest_price.append(route)
cheapest_sort = sorted(routes_with_lowest_price, key=lambda i: i['Price'])
# pprint.pprint(cheapest_sort)

# pprint.pprint(cheapest_sort[0])




# Example: if you just want the destination info of the cheapest quote

cheapest_routeids = cheapest_sort[0]['QuoteIds'] # this is a list of QuoteIds, the first one is not necessarily the cheapest

cheapest_price = cheapest_sort[0]['Price']




cheapest_route_info = {}
for q in quotes:
    if q['QuoteId'] in cheapest_routeids and q['MinPrice'] == cheapest_price:
        cheapest_route_info = q

# pprint.pprint(cheapest_route_info)


cheapest_route_dest_info = {}
for p in places:
    if cheapest_route_info['OutboundLeg']['DestinationId'] == p['PlaceId']:
        cheapest_route_dest_info = p

pprint.pprint(cheapest_route_dest_info)














# InputPlaceName = input('Enter Place Name')
#
# place_name = [response_data['Places']]

# #PLACES LIST API
# places = requests.get("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/?query={}".format(InputPlaceName),
#   headers={
#     "X-RapidAPI-Key": "85c2cae2d1msh4f45b5e5f5f7ffep19de73jsnf513195c7a59"
#   }
# )
# response_text2 = places.text
# response_data2 = json.loads(response_text2)
# pprint.pprint(response_data2)




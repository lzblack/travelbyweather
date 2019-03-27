import requests
import json
import pprint
import decimal

#CODE WITH INPUTS
# trip_start_month = input('What month would you like to start your journey? ')
# trip_start_day = input('What day sounds good? ')
# trip_start_year = input('Year? ')
# trip_start_date = "{}-{}-{}".format(trip_start_year, trip_start_month, trip_start_day)
# trip_end_month = input('What month are you coming back ')
# trip_end_day = input('What day sounds good? ')
# trip_end_year = input('Year? ')
# trip_end_date = "{}-{}-{}".format(trip_end_year , trip_end_month, trip_end_day)
# trip_start_location = input('Airport code for your city: ')

#CODE WITHOUT INPUTS
trip_start_month = '05'
trip_start_day = '05'
trip_start_year = '2019'
trip_start_date = "{}-{}-{}".format(trip_start_year, trip_start_month, trip_start_day)
trip_end_month = '05'
trip_end_day = '09'
trip_end_year = '2019'
trip_end_date = "{}-{}-{}".format(trip_end_year , trip_end_month, trip_end_day)
trip_start_location = input('Airport code for your city: ')

response = requests.get("https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browseroutes/v1.0/US/USD/en-US/{}/anywhere/{}?inboundpartialdate={}".format(trip_start_location, trip_start_date, trip_end_date),
  headers={
    "X-RapidAPI-Key": "85c2cae2d1msh4f45b5e5f5f7ffep19de73jsnf513195c7a59"
  }
)
sum=0
def_price = 'Could Not Find'
response_text = response.text
response_data = json.loads(response_text)
Routes = (response_data['Routes'])
Deals = (Routes[1])
for i in range(1,100):
    if "Price" in Deals:
        print("yay")
        sum=sum+1
    else:
        i=i+1
        print(def_price)
print(sum)


# Price = (Deals['Price'])
# pprint.pprint(Deals)
list=[]
# pprint.pprint(price)
    # print(PriceOfDeal)
# print(response[4]["price"])
# for i in range(1,100):
#     if not response["price"]
#         print(response['Routes'][i]["price"])
# sum=0
# for i in range(1,100):
#     if (Routes[i]["Price"]):
#         print()
#     else:
#         sum=sum+1
# print(sum)

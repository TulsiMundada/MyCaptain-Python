import requests
from bs4 import BeautifulSoup
import pandas

'''
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--page_num_max", help="Enter the number of pages to parse")
args = parser.parse_args()
max_pg_no = args.page_num_max

'''

headers = {
   'user-agent': 'Mozilla/70.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}


hotels_info = []

city = input("Enter name of the city: ").casefold()

oyo_baseurl="https://www.oyorooms.com/hotels-in-" + city + "/?page="

max_pg_no = eval(input("Enter the number of pages to scrape: "))

for pg_no in range(1 , max_pg_no + 1):
  oyo_url = oyo_baseurl + str(pg_no)
  print(oyo_url)
  req = requests.get(oyo_url, verify=True, headers=headers)

  content = req.content

  soup = BeautifulSoup(content, "html.parser")

  all_hotels = soup.find_all("div", {"class": "hotelCardListing"})
  
  

  for hotel in all_hotels:
    
    hotels_dict = {}

    try:
      hotels_dict["Name"] = hotel.find("h3",{"class": "listingHotelDescription__hotelName d-textEllipsis"}).text

      hotels_dict["Location"] = hotel.find("span",{"itemprop":"streetAddress"}).text

      hotels_dict["Rating"] = hotel.find("div",{"itemprop":"aggregateRating"}).text

      hotels_dict["Slashed Price"] = hotel.find("span",{"class":"listingPrice__slashedPrice"}).text

      hotels_dict["Current Price"] = hotel.find("span",{"class":"listingPrice__finalPrice"}).text

    except:
      pass

    hotels_info.append(hotels_dict)
    
   
dataFrame = pandas.DataFrame(hotels_info)
dataFrame.to_csv("OYO.csv")

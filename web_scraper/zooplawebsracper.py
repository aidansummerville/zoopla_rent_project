import requests
import csv
from bs4 import BeautifulSoup

pg = list(range(1,101))
# fo(r num in ascii_lowercase:
x = ("?page=")


zoopla = "https://www.zoopla.co.uk"

home_file = open('week03MyHome.csv', mode='a')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
baseurl = requests.get("https://www.zoopla.co.uk/to-rent/property/london/?identifier=london&include_shared_accommodation=false&page_size=100&q=London&search_source=home&radius=0&price_frequency=per_month&pn=")
for n in range(len(pg)):
        page = f'{baseurl.text}{pg[n]}'
        # print(page)

        soup = BeautifulSoup(page, 'html.parser')
        
        






   

        listings = soup.findAll("div", class_="listing-results-wrapper" )
        for listing in listings:

            entryList = []

            link = listing.find(class_="listing-results-price text-price").get('href')
            entryList.append(zoopla + link)

            image = listing.find(class_= "photo-hover").find('img')
            image2 = image['data-src'] if image else "NULL"
            entryList.append(image2)
            alt = image['alt'] if image else "NULL"
            entryList.append(alt)

            # logo = listing.find(class_= "agent_logo").find('img')
            # logo2 = logo['data-src'] if logo else "NULL"
            # entryList.append(logo2)
            # alt2 = logo['alt'] if logo else "NULL"
            # entryList.append(alt2)


            price = listing.find(class_="listing-results-price text-price").text
            entryList.append(price)

            address = listing.find(class_="listing-results-address").text
            entryList.append(address)

            beds = listing.find(class_= "listing-results-attr").find(class_= "num-icon num-beds")
            bbeds = beds.getText() if beds else "NULL"
            entryList.append(bbeds)

            baths = listing.find(class_= "listing-results-attr").find(class_= "num-icon num-baths")
            baths2 = baths.getText() if baths else "NULL"
            entryList.append(baths2)

            recp = listing.find(class_= "listing-results-attr").find(class_= "num-icon num-reception")
            recp2 = recp.getText() if recp else "NULL"
            entryList.append(recp2)

            available = listing.find(class_= "available-from")
            avail = available.getText() if available else "NULL"
            entryList.append(avail)
            
            added = listing.find(class_= "listing-results-just-added")
            add = added.getText() if added else "NULL"
            entryList.append(add)

            station1 = listing.find_all("span",{"class":"nearby_stations_schools_name"})[0]
            station1a = station1.getText() if station1 else "NULL"
            entryList.append(station1a)

            stationd1 = listing.find_all("li",{"class":"clearfix"})[0]
            stationd1a = stationd1.getText() if stationd1 else "NULL"
            entryList.append(stationd1a)

            station2 = listing.find_all("span",{"class":"nearby_stations_schools_name"})[1]
            station2a = station2.getText() if station2 else "NULL"
            entryList.append(station2a)

            stationd2 = listing.find_all("li",{"class":"clearfix"})[1]
            stationd2a = stationd2.getText() if stationd2 else "NULL"
            entryList.append(stationd2a)

            listed = listing.find(class_= "top-half listing-results-marketed")
            listed2 = listed.getText() if listed else "NULL"
            entryList.append(listed2)

            contact = listing.find(class_= "agent_phone")
            contact2 = contact.getText() if contact else "NULL"
            entryList.append(contact2)

            home_writer.writerow(entryList)
        
home_file.close()
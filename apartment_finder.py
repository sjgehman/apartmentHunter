#Set desired price range and number of bedrooms below
priceLimit = 4100
bedroomMatch = 1

#Creates a string "x bedroom(s)" to check for matches in the html output
bedroomCheck = str(bedroomMatch) + " Bedroom"

#Finds apartments that match the price and bedroom limit
def find_apartments(soup):
    units = []
    for apt_container in soup.select('.apts-container__apt'):
        bedrooms_info = apt_container.select_one('.apt-property__row span')
        if bedrooms_info and bedroomCheck in bedrooms_info.text:
            price_text = apt_container.select_one('.unit-price').text.strip()
            price = float(price_text.replace('Starting at $', '').replace(',', ''))
            if price < priceLimit:  # Adjusted price limit
                link_element = apt_container.select_one('.unit-link a')  # Example selector for <a> tag
                link = link_element['href'] if link_element else 'No link available'
                units.append({
                    'name': apt_container.select_one('h3').text.strip(),
                    'bedrooms': bedroomMatch,
                    'price': int(price),
                    'link': link
                })
    return units
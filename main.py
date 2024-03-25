from requests_and_parsing import fetch_apartments
from apartment_finder import find_apartments
from email_notifications import send_email

def main():
    url = "https://chicagorentals.com/apartment/the-scholar/"
    soup = fetch_apartments(url)
    units = find_apartments(soup)
    if units:
        send_email(units)

if __name__ == "__main__":
    main()
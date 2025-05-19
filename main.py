from datetime import datetime
import requests
from bs4 import BeautifulSoup



def send_push_notification():
    message = "Einburgurungstest Termin avaliable at " + url
    response = requests.post(
        "https://ntfy.sh/d637c33b-f998-4145-9773-2145bbc1cdac",
        data=message.encode('utf-8')
    )
    print("Push notification sent!" if response.status_code == 200 else "Failed to send push.")


def main():
    # Make a request to the website
    response = requests.get(url)

        # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # The text we're looking for
        search_text = "Leider sind aktuell keine Termine für ihre Auswahl verfügbar."

        # Check if the text exists in the page
        if search_text in soup.get_text():
            print("No Appointments available")
        else:
            print("Appointments available... Sending push notification")
            send_push_notification()
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://service.berlin.de/terminvereinbarung/termin/all/351180/"
    hour = datetime.now().hour
    if hour <= 5 or hour > 20:
        print("Not running at this time")
    else:
        main()
        

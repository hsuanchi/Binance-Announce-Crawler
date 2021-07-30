# for Crawler
import requests
from bs4 import BeautifulSoup

# for Firebase
from firebase_admin import initialize_app
from firebase_admin import credentials
from firebase_admin import firestore
from google.api_core.exceptions import AlreadyExists

"""
pip3 install bs4,requests,firebase_admin
or
pip3 install -r requirements.txt 
"""

cred = credentials.Certificate("firebase-adminsdk.json")
initialize_app(cred)
db = firestore.client()


def main():
    line_notify_token = "put your line notify token here"
    line_headers = {
        "Authorization": "Bearer " + line_notify_token,
        "Content-Type": "application/x-www-form-urlencoded",
    }
    crawler_headers = {
        "user-agent": "Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
    }
    url = "https://www.binance.com/en/support/announcement/c-48?navId=48"

    try:
        # Crawler for Binance Announcement
        r = requests.get(url, headers=crawler_headers)
        soup = BeautifulSoup(r.text, "html.parser")
        crawl_title = soup.select(".css-1ej4hfo")[0].text

        # Save To Firestore
        db.collection("crawler_Binance").document(crawl_title).create(
            {"date_time": firestore.SERVER_TIMESTAMP}
        )

        # Line Notify
        payload = {"message": crawl_title}
        r = requests.post(
            "https://notify-api.line.me/api/notify",
            headers=line_headers,
            params=payload,
        )
    except AlreadyExists as e:
        pass
    except Exception as e:
        db.collection("crawler_Binance").document("000_crawler_log").create(
            {str(e): firestore.SERVER_TIMESTAMP}
        )


main()

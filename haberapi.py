import requests
import json
from bs4 import BeautifulSoup
import json

try:
    # Haber sitesinden veri çekme
    response = requests.get("https://www.haberturk.com/gundem/")
    response.raise_for_status()  # Check for any HTTP errors

    data = response.text

    # Verileri çıkarma
    soup = BeautifulSoup(data, "html.parser")
    title_tag = soup.find("h1", class_="ht-title")
    description_tag = soup.find("p", class_="ht-description")

    title = title_tag.text if title_tag else "Title not found"
    description = description_tag.text if description_tag else "Description not found"

    # Discord webhook URL'si
    webhook_url = "https://discord.com/api/webhooks/1199755923321802764/-c3jfIB0-SiEjOKhEHM-UUb5QWpRFknHZrGjPphhPoAkkPZZ_327j15kCcHZhpD5PsBs"

    # Verileri Discord'a gönderme
    payload = {
        "content": "Yeni haberler:",
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": 16711680
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    response.raise_for_status()  # Check for any HTTP errors

    if response.status_code == 204:
        print("Veriler başarıyla Discord'a gönderildi.")
    else:
        print("Verileri Discord'a gönderirken bir hata oluştu.")

except requests.exceptions.RequestException as e:
    print("HTTP hatası oluştu:", e)

except (AttributeError, KeyError, ValueError) as e:
    print("Verileri çıkarmada bir hata oluştu:", e)

except Exception as e:
    print("Bir hata oluştu:", e)

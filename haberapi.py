import requests
import json
from bs4 import BeautifulSoup

try:
    # Haber sitesinden veri çekme
    response = requests.get("https://www.ntv.com.tr/galeri/teknoloji/bir-ilki-basardi-playstation-5in-tablet-surumu-gelistirildi,_hgscsgymUGWKz-tIH019g")
    response.raise_for_status() 

    data = response.text

    # Verileri çıkarma
    soup = BeautifulSoup(data, "html.parser")
    title_tag = soup.find("h1", class_="ht-title")
    description_tag = soup.find("p", class_="ht-description")

    if title_tag and description_tag:
        title = title_tag.text.strip()
        description = description_tag.text.strip()
    else:
        raise ValueError("Title or description not found")

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

import json
from requests import get
from bs4 import BeautifulSoup as bs


base_url = "https://hedibert.org/wp-content/uploads"
headers = {
    'accept': '*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}


all_media: list[str] = []

for year in range(2013, 2024):
    for month in range(1, 13):
        if month >= 10:
            year_month = f"{year}/{month}/"
        else:
            year_month = f"{year}/0{month}/"

        url = f"{base_url}/{year_month}"
        res = get(url, headers=headers)
        print(f"{res.ok} - {url}")
        if res.ok:
            soup = bs(res.text, "html.parser")
            table_rows = soup.find_all("tr")[3:-1]
            for row in table_rows:
                all_media.append(f"{year_month}{row.find("a")["href"]}")


with open("urls.json", 'w+', encoding="utf-8") as f:
    print(json.dumps({"urls": all_media}, indent=2), file=f)

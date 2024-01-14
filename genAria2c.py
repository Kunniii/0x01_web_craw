
import json
import os

base_url = "https://hedibert.org/wp-content/uploads"
headers = {
    'accept': '*',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

data = {}
with open("urls.json", 'r') as f:
    data = json.load(f)
urls: list[str] = data.get("urls", [])


def getFolderFileName(url: str) -> tuple[str, str]:
    parts = url.split("/")
    file_name = parts[-1]
    folder = f"{parts[0]}/{parts[1]}"
    return (folder, file_name)


"""
http://server/file.iso http://mirror/file.iso
  dir=/iso_images
  out=file.img
"""

with open("aria2c.txt", 'w+', encoding="utf-8") as f:
    for url in urls:
        folder, name = getFolderFileName(url)
        out_dir = os.path.abspath(f"./downloads/{folder}/")
        f.write(f"{base_url}/{url}\n")
        f.write(f"\tdir={out_dir}\n")
        f.write(f"\tout={name}\n")

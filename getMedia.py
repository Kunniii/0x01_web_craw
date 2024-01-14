
import json
import os
from threading import Thread

from requests import get

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


def run():
    global urls
    while urls:
        url = urls.pop(0)
        print(f" [+] Getting {url}")
        folder, name = getFolderFileName(url)

        out_dir = os.path.abspath(f"./out/{folder}/")

        if os.path.exists(f"{out_dir}/{name}"):
            print(f"[!] {name} exists! Continue...")
            continue

        res = get(f"{base_url}/{url}", headers=headers)

        if not os.path.isdir(out_dir):
            print(f"[!] Dir not found: {out_dir}")
            os.makedirs(out_dir)

        with open(f"{out_dir}/{name}", "wb") as f:
            f.write(res.content)


worker_no = 10
workers: list[Thread] = []

for i in range(worker_no):
    print(f" [+] Init worker {i}")
    workers.append(Thread(target=run))

for worker in workers:
    worker.run()

for worker in workers:
    worker.join()

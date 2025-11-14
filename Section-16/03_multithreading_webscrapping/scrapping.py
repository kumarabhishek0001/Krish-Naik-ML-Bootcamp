import threading
import requests
import sys
from bs4 import BeautifulSoup

# Fix terminal encoding issue
sys.stdout.reconfigure(encoding='utf-8')

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/'
]

def fetch_contents(site):
    response = requests.get(
        site,
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    soup = BeautifulSoup(response.content, 'html.parser')
    data = soup.text

    # Append instead of overwrite
    with open('output.txt', 'a', encoding='utf-8') as file:
        file.write(f"URL: {site}\n")
        file.write(data)
        file.write("\n----------------END----------------\n")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_contents, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('All URLs fetched')

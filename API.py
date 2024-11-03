import requests
from urllib.parse import urlencode
import yadisk

base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?'
public_key = 'https://yadi.sk/d/UJ8VMK2Y6bJH7A'

final_url = base_url + urlencode(dict(public_key=public_key))
response = requests.get(final_url)
download_url = response.json()['href']


download_response = requests.get(download_url)
with open('downloaded_file.txt', 'wb') as f:
    f.write(download_response.content)



y = yadisk.YaDisk(token="токен")
y.upload("files/resolt_wideo.txt", "/test/file1.txt")
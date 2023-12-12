import requests
from PIL import Image
from io import BytesIO

api_url = "http://placekitten.com/200/300"
response = requests.get(api_url)

if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    image.show()
else:
    print("Hata kodu:", response.status_code)


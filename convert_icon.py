import requests
from PIL import Image
from io import BytesIO

url = "https://raw.githubusercontent.com/ferrumc-rs/ferrumc/refs/heads/master/assets/data/icon.png"
response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.save("favicon.ico", format='ICO')
print("Favicon saved.")
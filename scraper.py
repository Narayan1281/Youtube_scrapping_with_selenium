import requests
from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

# Does not execute Javascript
response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code: ', response.status_code)

# print(response.text[:1000])
with open('trending.html', 'w') as f:
    f.write(response.text)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title: ', doc.title.text)

# Find all the video divs
video_divs = doc.find_all('div', class_= 'ytd-video-renderer')

print(f'Found {len(video_divs)} videos') 
# Initial html just have the blank page and the javascript code that the browser
# executes in order to fetch the page content.
# the browser executes javascript code which makes another network request and which
# fetches the information and then adds it to the page.
# ###
# ##
# That's what happens in dynamic or client side rendered pages!
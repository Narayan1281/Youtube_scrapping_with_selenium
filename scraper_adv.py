from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = "https://www.youtube.com/feed/trending"

def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    # chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def get_videos(driver):
    VIDEO_DIV_TAG = 'ytd-video-renderer'
    # print('Fetching the page...')
    # print('Page title: ', driver.title)
    driver.get(YOUTUBE_TRENDING_URL)
    videos = driver.find_elements(By.TAG_NAME, VIDEO_DIV_TAG)
    return videos

if __name__ == "__main__":
    print('Creating driver')
    driver = get_driver()
    
    print('Fetching trending videos')
    videos = get_videos(driver)

    print (f'Found {len(videos)} videos')
    

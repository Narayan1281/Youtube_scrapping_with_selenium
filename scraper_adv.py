from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

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

def parse_video(video):
    # title, url, thumbnail_url, channel, views, uploaded time, description

    title_tag = video.find_element(By.ID, 'video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')
    
    thumbnail_tag = video.find_element(By.TAG_NAME, 'img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    channel_div = video.find_element(By.CLASS_NAME, 'ytd-channel-name')
    channel_name = channel_div.text

    description = video.find_element(By.ID, 'description-text').text

    metadata_line = video.find_element(By.ID, 'metadata-line')
    metadata_tags = metadata_line.find_elements(By.TAG_NAME, 'span')
    views = metadata_tags[0].text
    uploaded_time = metadata_tags[1].text
    video_info = {
        'title': title,
        'url': url,
        'thumbnail_url': thumbnail_url,
        'channel': channel_name,
        'views': views,
        'uploaded': uploaded_time,
        'description': description
    }
    return video_info

if __name__ == "__main__":
    print('Creating driver')
    driver = get_driver()
    
    print('Fetching trending videos')
    videos = get_videos(driver)

    print (f'Found {len(videos)} videos')
    
    print('Parsing top 10 video')
    videos_data = [parse_video(video) for video in videos[:10]]
    
    print('Save the data to a CSV')
    videos_df = pd.DataFrame(videos_data)
    print(videos_df)
    videos_df.to_csv('trending.csv')
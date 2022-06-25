# NOTE:
# 1. pip install selenium
# 2. selenium driver can be chrome or firefox

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

#url = "https://twitter.com/DisneyPlusNL/status/1427605982524461082?s=20"
# https://twitter.com/running1277/status/1394138156254076935?s=20&t=p0Ehy0dvpxV8DBv9058KLA
dark_url = "https://platform.twitter.com/embed/Tweet.html?id=463440424141459456&theme=dark&hideThread=false&lang=en&embedId=twitter-widget-0&features=eyJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2hvcml6b25fdHdlZXRfZW1iZWRfOTU1NSI6eyJidWNrZXQiOiJodGUiLCJ2ZXJzaW9uIjpudWxsfX0%3D&frame=false&hideCard=false&sessionId=4ee57c34a8bc3f4118cee97a9904f889f35e29b4&widgetsVersion=82e1070%3A1619632193066"
url = "https://platform.twitter.com/embed/Tweet.html?id=1394138156254076935&theme=light&hideThread=false&lang=en&embedId=twitter-widget-2&features=eyJ0ZndfZXhwZXJpbWVudHNfY29va2llX2V4cGlyYXRpb24iOnsiYnVja2V0IjoxMjA5NjAwLCJ2ZXJzaW9uIjpudWxsfSwidGZ3X2hvcml6b25fdHdlZXRfZW1iZWRfOTU1NSI6eyJidWNrZXQiOiJodGUiLCJ2ZXJzaW9uIjpudWxsfX0%3D&frame=false&hideCard=false&sessionId=4ee57c34a8bc3f4118cee97a9904f889f35e29b4&widgetsVersion=82e1070%3A1619632193066"
# Configure Firefox to work headlessly (no window popping up)
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)

# To make sure no other visual elements overlap the Tweet.
driver.set_window_position(0, 0)
driver.set_window_size(2000, 2000)

# Fetch the Tweet URL
driver.get(url)

# Just to make sure all elements load first
time.sleep(10)

#xpath = '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div'
xpath = '/html/body/div[1]/div/div/div/article'

# Sometimes we need to click onto the tweet first, be we also sometimes don't.
# //*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[1]/article/div/div/div
# try:
#     b = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))
#     driver.find_element(By.XPATH, xpath).click()
# except:
#     pass

# Screenshot the Tweet
img = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath))).screenshot_as_png
#driver.find_element(By.XPATH, xpath).click()
#img = driver.find_element(By.XPATH, xpath).screenshot_as_png

# Write the image data to a file
with open("tweet.png", "wb") as file:
    file.write(img)

# Close the headless browser
driver.close()

# send notification to whats app
# Buy sell
# read write to .csv?

import yaml
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


with open('config.yml', 'r') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    username = data.get("username")
    password = data.get("password")
    website = data.get("website")
    drive = data.get("drive")

# Start up google chrome
driver = webdriver.Chrome(drive)
driver.get(website)
driver.maximize_window()
time.sleep(2)

# Checks current url and sees if logged in
print(driver.current_url)

# Login Path
login_btn = driver.find_element_by_xpath("//*[text()='LOG IN']") 
login_btn.click()
time.sleep(2)

username_field = driver.find_element_by_xpath("//input[@placeholder='Email Address']") 
username_field.send_keys(username)

password_field = driver.find_element_by_xpath("//input[@placeholder='Password']") 
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(4)

# Exit Chrome
time.sleep(10)
driver.close()
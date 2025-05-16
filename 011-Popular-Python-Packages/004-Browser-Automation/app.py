from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://github.com")


signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

username_box = browser.find_element(By.ID, "login_field")
username_box.send_keys("MYEMAIL")

password_box = browser.find_element(By.ID, "password")
password_box.send_keys("MYPASSWORD")

password_box.submit()

assert "MY-USER-NAME" in browser.page_source

profile_link = browser.find_element(By.CLASS_NAME, "user-profile-link")
link_label = profile_link.get_attribute("innerHTML")
assert "MY-USER-NAME" in link_label

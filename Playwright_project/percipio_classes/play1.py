import time

from playwright.sync_api import sync_playwright

# here we are starting the playwright with start() method
play_obj = sync_playwright().start()

browser = play_obj.chromium.launch(headless=False)
cont_page = browser.new_context()
page = cont_page.new_page()
page.goto("https://automationexercise.com/")
time.sleep(4)

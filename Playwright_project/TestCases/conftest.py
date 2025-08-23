import time

import pytest
from playwright.sync_api import sync_playwright
import pyautogui

screen_width, screen_height = pyautogui.size()


@pytest.fixture(scope="session")
def user_credential(request):
    return request.param


@pytest.fixture(scope="session")
def get_details(request):
    return request.param


@pytest.fixture(scope="class")
def setup():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, slow_mo=1200, args=["--start-maximized"])

        context_obj = browser.new_context(no_viewport=True, record_video_dir=r"C:\Users\HP\Documents\Playwright_project"
                                                                             r"\Recorded_videos",
                                          record_video_size={"width": screen_width, "height": screen_height})

        page = context_obj.new_page()

        yield page

        context_obj.close()
        browser.close()






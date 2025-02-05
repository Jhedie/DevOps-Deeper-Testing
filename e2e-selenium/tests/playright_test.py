import os
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

@pytest.fixture(scope="module")
def driver():
    load_dotenv()
    browser = os.getenv("BROWSER", "chrome")
    if browser == "chrome":
        opt = webdriver.ChromeOptions()
        opt.add_argument("--headless=new")
        with webdriver.Chrome(options=opt) as driver:
            yield driver
    elif browser == "firefox":
        with webdriver.Firefox() as driver:
            yield driver
    elif browser == "safari":
        with webdriver.Safari() as driver:
            yield driver
    else:
        raise Exception(f"Browser {browser} is not supported. Please select one of chrome, firefox or safari")

def test_chrome_open_google(driver):


    driver.get("https://demo.playwright.dev/todomvc/#/")
    todoBox = driver.find_element(By.CLASS_NAME, 'new-todo')
    todoBox.send_keys("Start selenium")
    todoBox.send_keys(Keys.RETURN)
    todoBox.send_keys("Check selenium")
    todoBox.send_keys(Keys.RETURN)

    driver.save_screenshot('playrightphoto.png')


    sleep(1)

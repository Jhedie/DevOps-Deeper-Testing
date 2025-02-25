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

    driver.get("https://www.selenium.dev/")

    # handle cookie pop up
    try:
        element = driver.find_element(By.XPATH, '//div[text()="Reject all"]')
        element.click()
    except:
        # continue onwards
        pass
    #Tax screenshot

    element = driver.find_element(By.CSS_SELECTOR, '#main_navbar > ul > li:nth-child(3) > a > span')
    element.click()
    search_button = driver.find_element(By.CLASS_NAME, 'DocSearch-Button-Placeholder')
    search_button.click()

    search_box = driver.find_element(By.CLASS_NAME, 'DocSearch-Input')
    search_box.send_keys("Select")
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "docsearch-item-0"))
    )
    driver.save_screenshot('photo.png')
    element = driver.find_element(By.ID, 'docsearch-item-0')
    element.click()
    # Leave the screen up for a few seconds
    # just while we're watching the tests directly
    sleep(1)

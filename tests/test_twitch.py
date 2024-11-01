import time

from selenium.common import NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_twitch_wap(chrome_browser):
    """
    Test using the Mobile emulator from Google Chrome
    to check basic Twitch site functions
    """

    # Step 1: Open the target site
    chrome_browser.get("https://m.twitch.tv/")
    assert chrome_browser.title == "Twitch"

    # Step 2: Click on the search icon
    # Find the search box element.
    search_icon = WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div[1]/div[1]/nav/div[3]/a"))
    )
    search_icon.click()

    # Wait until the search bax is present
    search_box = WebDriverWait(chrome_browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='page-main-content-wrapper']/nav/div/div/div[2]/div/div/input")))
    # Enter a search query and submit.
    search_box.send_keys("StarCraft II" + Keys.RETURN)
    time.sleep(3)

    # Step 3: scroll 2 times
    for _ in range(2):
        ActionChains(chrome_browser).send_keys(Keys.END).perform()

    # Step 4: click on first streamer
    first_streamer = WebDriverWait(chrome_browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='page-main-content-wrapper']/div/div/section[2]/div[2]/div[1]/a/article/div[2]")))
    first_streamer.click()
    try:
        chrome_browser.switch_to.alert.accept()
    except NoAlertPresentException:
        print("No Alerts")

    # Step 5: Make a screenshot
    time.sleep(5)  # Ensure all elements have loaded
    chrome_browser.get_screenshot_as_file("last_step.png")

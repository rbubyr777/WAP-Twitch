import pytest

from selenium.webdriver.chrome.options import Options
from selenium import webdriver



@pytest.fixture(scope="function")
def chrome_browser():
    driver = config_driver()
    yield driver
    driver.quit()

def config_driver():
    options = Options()
    options.add_argument(
       '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    return driver

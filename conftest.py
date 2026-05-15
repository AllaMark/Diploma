import pytest
from selenium import webdriver




# Фикстура для драйвера Chrome
@pytest.fixture()
def driver():
   driver = webdriver.Chrome()
   yield driver
   driver.quit()


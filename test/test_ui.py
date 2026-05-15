from page.main_page import Main_page
import time

def test1(driver):
    main=Main_page(driver)
    main.open()
    time.sleep(3)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Main_page:
   """Класс главной страницы Кинопоиск"""
   URL="https://www.kinopoisk.ru"
   TICKET=(By.XPATH, "//a[@href='/lists/movies/movies-in-cinema/']")
   TICKET_PAGE=(By.XPATH, "//h1[text()='Билеты в кино']")


   def __init__(self, driver) -> None:
       """Метод инициализации класса"""
       self.driver = driver
       self.wait = WebDriverWait(driver, 30)

   def open(self):
       self.driver.get(self.URL)

   #//a[@href="/lists/movies/movies-in-cinema/"]
   def click_to_tickets(self):
      button=self.wait.until(EC.presence_of_element_located(self.TICKET))
      button.click()
   def 




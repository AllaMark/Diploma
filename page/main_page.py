from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Main_page:
    """Класс главной страницы Кинопоиск"""

    URL = "https://www.kinopoisk.ru"
    TICKET = (By.XPATH, "//a[@href='/lists/movies/movies-in-cinema/']")
    TICKET_PAGE = (By.XPATH, "//h1[text()='Билеты в кино']")

    def __init__(self, driver) -> None:
        """Метод инициализации класса"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def open(self):
        self.driver.get(self.URL)

    def search_by_phrase(self, phrase):
        """ввод фразы в строке поиска"""
        search_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="text"]'))
        )
        search_input.clear()
        search_input.send_keys(phrase)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def get_top_search_results(self, name):
        """возвращает название фильма, первого в поиске"""
        result = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//div[@data-test-id="movie-list-item"][1]//div[@class="base-movie-main-info_mainInfo__8Yzaj"]',
                )
            )
        )
        return result.text

    def go_to_movie_tickets(self):
        """Метод для перехода на вкладку «Билеты в кино» на Кинопоиске"""

        # Поиск по тексту ссылки
        tickets_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Билеты в кино')]")
            )
        )
        tickets_link.click()
        return self.driver.title

    def go_to_movie_films(self):
        """Метод для перехода на вкладку «Фильмы» на Кинопоиске"""

        # Поиск по тексту ссылки
        films_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@href="/lists/categories/movies/1/"]')
            )
        )

        films_link.click()
        return self.driver.title

    def go_to_serial(self):
        """Метод для перехода на вкладку «Сериалы» на Кинопоиске"""

        #  # переход к разделу меню Сериалы
        serial_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//a[@href="/lists/categories/movies/3/"]')
            )
        )

        serial_link.click()
        return self.driver.title

from page.main_page import Main_page
import allure
import pytest

@pytest.mark.ui
@allure.title("Поиск фильма на русском языке")
@allure.story("Поиск")
def test_search_film(driver):
    film_name = "Гладиатор"
    with allure.step("Переходна главную страницу"):
        main_page = Main_page(driver)
        main_page.open()
    with allure.step("Выполняем поиск фильма"):
        main_page.search_by_phrase(film_name)
    with allure.step("Выполняем проверку, что фильм первый в списке"):
        assert main_page.get_top_search_results(film_name) == film_name

@pytest.mark.api
@allure.title("Переход на вкладку «Билеты в кино»")
@allure.story("Переход")
def test_go_to_movie_tickets(driver):
    """Тест для проверки перехода на вкладку «Билеты в кино» на Кинопоиске"""
    with allure.step("Переходна главную страницу"):
        main_page = Main_page(driver)
        main_page.open()
    with allure.step("Выполняем переход на вкладку «Билеты в кино»"):
        response = main_page.go_to_movie_tickets()
    with allure.step("Выполняем проверку, что перешли на страницу"):
        assert "Билеты в кино" in response

@pytest.mark.api
@allure.title("Переход на вкладку «Фильмы»")
@allure.story("Переход")
def test_go_to_movie_films(driver):
    """Тест для проверки перехода на вкладку «Фильмы» на Кинопоиске"""
    with allure.step("Переходна главную страницу"):
        main_page = Main_page(driver)
        main_page.open()
    with allure.step("Выполняем переход на вкладку «Фильмы»"):
        response = main_page.go_to_movie_films()
    with allure.step("Выполняем проверку, что перешли на страницу"):
        assert "Фильмы" in response

@pytest.mark.api
@allure.title("Переход на вкладку «Сериалы»")
@allure.story("Переход")
def test_go_to_serial(driver):
    """Тест для проверки перехода на вкладку «Сериалы» на Кинопоиске"""
    with allure.step("Переходна главную страницу"):
        main_page = Main_page(driver)
        main_page.open()
    with allure.step("Выполняем переход на вкладку «Сериалы»"):
        response = main_page.go_to_serial()
    with allure.step("Выполняем проверку, что перешли на страницу"):
        assert "Сериалы" in response
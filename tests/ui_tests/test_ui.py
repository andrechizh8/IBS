import pytest
from model.ui.pages.main_page import MainPage
from model.api.versions.reqres_users import UserApi
import allure


@pytest.fixture(scope="function")
def main_page(driver):
    """
    Fixture for initializing the MainPage and opening it.
    Driver get from conftest.py
    """
    main = MainPage(driver, "https://reqres.in/")
    main.open()
    return main


@allure.tag('UI')
@allure.description('UI tests')
@allure.label('owner', 'andrechizh8')
class TestUi:
    user_api = UserApi()

    def test_check_logo(self, main_page):
        """
        Check the logo on the main page
        """
        assert main_page.get_logo()

    def test_correct_tagline_text(self, main_page):
        """
        Check correct text of tagline on main page
        """

        assert main_page.get_tagline_text() == "A hosted REST-API ready to respond to your AJAX requests."

    @pytest.mark.parametrize("value", [50, 100, 10])
    def test_donate_support(self, main_page, value):
        """
        Check user`s donate
        """
        main_page.support_donate(value)
        assert main_page.get_donate_text()

    def test_correct_redirect_to_authors_page(self, main_page):
        """
        Check correct creator page redirect
        """
        assert main_page.redirect_to_creator().get_creators_name()

    def test_correct_response_status_code(self, main_page):
        """
        Check correct
        """
        assert main_page.get_response_status_code() == 200

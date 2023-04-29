import pytest
from model.api.versions.reqres_users import UserApi
from model.ui.pages.main_page import MainPage
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


@pytest.fixture(scope="function")
def reqres_api():
    api = UserApi()
    return api


@allure.tag('Combined')
@allure.description('Combined UI and API test')
@allure.label('owner', 'andrechizh8')
class TestCombine:

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_api_ui_same_code(self, main_page, user_id, reqres_api):
        """
        Checking the status code using the UI is the same as  using the API
        """
        ui_status_code = main_page.get_response_status_code()
        api_status_code = reqres_api.get_single_user(user_id).status_code
        assert ui_status_code == api_status_code

    def test_api_ui_same_body(self, main_page, reqres_api):
        """
        Checking the response body using the UI is the same as  using the API
        """
        ui_body = main_page.get_response_body()
        api_body = reqres_api.get_single_user_body(2)
        assert ui_body == api_body

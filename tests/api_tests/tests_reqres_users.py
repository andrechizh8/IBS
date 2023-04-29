import pytest
from requests import Response
from model.api.schemas import schema
from pytest_voluptuous import S
from model.api.versions.reqres_users import UserApi
import allure


@pytest.fixture()
def user_api():
    user_api = UserApi()
    return user_api


@allure.tag('API')
@allure.description('API test users')
@allure.label('owner', 'andrechizh8')
class TestUsersApi:

    @pytest.mark.parametrize("name, job", [("Andrew", "QA"), ("Alex", "Doctor"), ("Masha", "HR")])
    def test_create_user_successful(self, name, job, user_api):
        """
        Test creating a new user with correct data and check correct name
        """

        response: Response = user_api.create_new_user(name, job)
        assert response.status_code == 201
        assert response.json()["name"] == name

    @pytest.mark.shema
    def test_check_created_user_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """

        response: Response = user_api.create_new_user("Andrew", "QA")
        assert S(schema.create_single_user) == response.json()

    @pytest.mark.xfail(reason="API creates a user with incorrect data")
    @pytest.mark.negative
    @pytest.mark.parametrize(
        "name, job",
        [
            ("", 123),
            (321, ""),
            ("", ""),
            (123514, 1451235)
        ]
    )
    def test_create_user_invalid_data(self, name, job, user_api):
        """
        Test creating a new user with invalid data
        """

        response: Response = user_api.create_new_user(name, job)
        assert response.status_code != 201

    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_get_single_user(self, user_id, user_api):
        """
        Test get user by correct id and check status code
        """

        response: Response = user_api.get_single_user(user_id)
        assert response.status_code == 200

    @pytest.mark.shema
    def test_check_user_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """

        response: Response = user_api.get_single_user(2)
        assert S(schema.get_single_user) == response.json()

    @pytest.mark.negative
    @pytest.mark.parametrize("incorrect_id", [202, 301, 500, 1090])
    def test_get_user_with_incorrect_id(self, incorrect_id, user_api):
        """
        Test check that user with incorrect id is not exist
        """

        response: Response = user_api.get_single_user(incorrect_id)
        print(response.status_code)
        assert response.status_code == 404

    @pytest.mark.parametrize("page", [1, 2])
    def test_get_users_list(self, page, user_api):
        """
        Test get list of users and check status code
        """

        response: Response = user_api.get_users_list(page)
        assert response.status_code == 200

    @pytest.mark.shema
    def test_check_users_list_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """

        response: Response = user_api.get_users_list(2)
        assert S(schema.get_list_users) == response.json()

    @pytest.mark.xfail(reason="API validate incorrect input type parameter ")
    @pytest.mark.negative
    @pytest.mark.parametrize("page", ["asuhdahsld", 20.0, 000000])
    def test_get_list_with_incorrect_id(self, page, user_api):
        """
        Test retrieving list of users with invalid input type parameter
        """

        response: Response = user_api.get_users_list(page)
        assert response.status_code == 400

    @pytest.mark.slow
    @pytest.mark.parametrize("delay", [3, 4, 5])
    def test_delayed_response(self, delay, user_api):
        """
        Test get delayed response and check status code
        """

        response: Response = user_api.get_delayed_users_list(delay)
        assert response.status_code == 200

    @pytest.mark.schema
    def test_check_schema_delayed_response(self, user_api):
        """
        Test that the response schema matches the expected schema
        """

        response: Response = user_api.get_delayed_users_list(5)
        assert S(schema.get_delayed_response) == response.json()

    @pytest.mark.parametrize("delay", [3, 4, 5])
    def test_check_delayed_time(self, delay, user_api):
        """
        Test delayed response time
        """

        response: Response = user_api.get_delayed_users_list(delay)
        assert response.elapsed.total_seconds() > delay

    @pytest.mark.schema
    def test_check_delayed_response_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """

        response: Response = user_api.get_delayed_users_list(3)
        assert S(schema.get_delayed_response) == response.json()

    @pytest.mark.parametrize("user_id", [23, 50, 123])
    def test_get_non_exist_user(self, user_id, user_api):
        """
        Test trying to get non exist user and check status code
        """

        response: Response = user_api.get_single_user(user_id)
        assert response.status_code == 404

    def test_check_content_type_non_exist_user(self, user_api):
        """
        Test checking correct  headers content type
        """

        response: Response = user_api.get_single_user(23)
        content_type = response.headers["Content-Type"]
        format_type = content_type.split(";")[0]
        assert format_type
        "application/json"

    @pytest.mark.parametrize("user_id, name, job", [(2, "Alex", "doctor"), (3, "Masha", "QA"), (4, "Vladimir", "Dev")])
    def test_update_user(self, user_id, name, job, user_api):
        """
        Test update user by using put method and check status code
        """

        response: Response = user_api.update_user(user_id, name, job)
        assert response.status_code == 200

    def test_check_updated_user_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """

        response: Response = user_api.update_user(2, "Alex", "doctor")
        assert S(schema.update_user) == response.json()

    @pytest.mark.negative
    @pytest.mark.xfail(reason="API validate incorrect user id type")
    @pytest.mark.parametrize("user_id, name, job",
                             [("фывфывфыв", "Alex", "doctor"), (201.5, "Masha", "QA"), ("!#@!#", "Vladimir", "Dev")])
    def test_check_update_user_with_incorrect_id_type(self, user_id, name, job, user_api):
        """
        Test update user by using put method and check status code
        """

        response: Response = user_api.update_user(user_id, name, job)
        assert response.status_code != 200

    @pytest.mark.parametrize("user_id, name, job", [(2, "Alex", "doctor"), (3, "Masha", "QA"), (4, "Vladimir", "Dev")])
    def test_partially_update_user(self, user_id, name, job, user_api):
        """
        Test  partially update user by patch method and check status code
        """
        response: Response = user_api.partially_update_user(user_id, name, job)
        assert response.status_code == 200

    def test_check_partially_updated_user_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """
        response: Response = user_api.partially_update_user(5, "Irina", "cooker")
        assert S(schema.partially_update_user) == response.json()

    @pytest.mark.negative
    @pytest.mark.xfail(reason="API validate incorrect user id type")
    @pytest.mark.parametrize("user_id, name, job",
                             [("фывфывфыв", "Alex", "doctor"), (201.5, "Masha", "QA"), ("!#@!#", "Vladimir", "Dev")])
    def test_partially_update_user_incorrect_id(self, user_id, name, job, user_api):
        """
        Test check that response data type is correct
        """
        response: Response = user_api.partially_update_user(user_id, name, job)
        assert response.status_code != 200

    @pytest.mark.parametrize("user_id", [1, 2, 3])
    def test_delete_user(self, user_id, user_api):
        """
        Test delete user by correct id and check status code
        """
        response: Response = user_api.delete_user(user_id)
        assert response.status_code == 204

    def test_delete_user_response_body(self, user_api):
        """
        Test delete user response has no body
        """
        response: Response = user_api.delete_user(2)
        assert not response.content

    @pytest.mark.negative
    @pytest.mark.xfail(reason="API validate incorrect user id type")
    @pytest.mark.parametrize("user_id", ["uashdhald", "20.1213", 123123.0])
    def test_delete_user_with_incorrect_id(self, user_id, user_api):
        """
        Test check delete user by incorrect id
        """
        response: Response = user_api.delete_user(user_id)
        assert response.status_code != 204

    def test_successful_register_user(self, user_api):
        """
        Test register user successful and check token type
        """
        response: Response = user_api.register_user("eve.holt@reqres.in", "pistol")
        assert type(response.json()["token"]) == str

    def test_successful_register_user_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """
        response: Response = user_api.register_user("eve.holt@reqres.in", "pistol")
        assert S(schema.successful_register_user) == response.json()

    @pytest.mark.negative
    @pytest.mark.parametrize("email", [1231421, "1892y3", 103.123])
    def test_register_user_with_incorrect_email_type(self, email, user_api):
        """
        Test check register user using int type instead str type in email
        """
        response: Response = user_api.register_user(email, "pistol")
        assert response.status_code == 400

    def test_unsuccessful_register_user_by_password(self, user_api):
        """
        Test register user unsuccessful by missing password and check status code
        """
        response: Response = user_api.register_user("sydney@fife", password=None)
        assert response.status_code == 400
        assert response.json()["error"] == "Missing password"

    def test_unsuccessful_register_user(self, user_api):
        """
        Test register user unsuccessful by missing email and password and check error message
        """
        response: Response = user_api.register_user(email=None, password=None)
        assert response.json()["error"] == "Missing email or username"

    def test_successful_login_user(self, user_api):
        """
        Test login user successful and check status_code
        """
        response: Response = user_api.login_user("eve.holt@reqres.in", "cityslicka")
        assert response.status_code == 200

    def test_successful_login_token(self, user_api):
        """
        Test user token is not empty
        """
        response: Response = user_api.login_user("eve.holt@reqres.in", "cityslicka")
        assert len(response.json()["token"]) != 0

    def test_successful_login_user_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """
        response: Response = user_api.login_user("eve.holt@reqres.in", "cityslicka")
        assert S(schema.successful_login_user) == response.json()

    @pytest.mark.negative
    @pytest.mark.parametrize("email", [1231421, "1892y3", 103.123])
    def test_login_user_with_incorrect_email_type(self, email, user_api):
        """
        Test check login user using int type instead str type in email
        """
        response: Response = user_api.register_user(email, "pistol")
        assert response.status_code == 400

    def test_unsuccessful_login_user(self, user_api):
        """
        Test login user unsuccessful by missing password and check status code
        """
        response: Response = user_api.login_user("peter@klaven", password=None)
        assert response.status_code == 400

    def test_unsuccessful_login_message(self, user_api):
        """
        Test login user unsuccessful by missing password and check message
        """
        response: Response = user_api.login_user("peter@klaven", password=None)
        assert response.json()["error"] == "Missing password"

    def test_unsuccessful_login_schema(self, user_api):
        """
        Test that the response schema matches the expected schema
        """
        response: Response = user_api.login_user("peter@klaven", password=None)
        assert S(schema.unsuccessful_login_user) == response.json()

import pytest
from requests import Response
from model.api.schemas import schema
from pytest_voluptuous import S
from model.api.versions.reqres_resources import ResourceApi
import allure


@pytest.fixture(scope="function")
def api():
    resource_api = ResourceApi()
    return resource_api


@allure.tag('API')
@allure.description('API test resource')
@allure.label('owner', 'andrechizh8')
class TestResourceApi:
    resource_api = ResourceApi()

    def test_get_resource_list(self, api):
        """
        Test get resource list and check status code
        """
        response: Response = api.get_resource_list()
        assert response.status_code == 200

    def test_resource_list_schema(self, api):
        """
        Test that the response schema matches the expected schema
        """
        response: Response = api.get_resource_list()
        assert S(schema.get_list_resource) == response.json()

    @pytest.mark.parametrize("resource_id", [1, 2, 3])
    def test_single_resource(self, resource_id, api):
        """
        Test get resource list and check status code
        """
        response: Response = api.get_single_resource(resource_id)
        assert response.status_code == 200

    def test_single_resource_schema(self, api):
        """
        Test that the response schema matches the expected schema
        """
        response: Response = api.get_single_resource(2)
        assert S(schema.get_single_resource) == response.json()

    @pytest.mark.parametrize("resource_id", [1111, 2222, 3333])
    def test_resource_not_found(self, resource_id, api):
        """
        Test get resource by incorrect id and check status code
        """
        response: Response = api.get_single_resource(resource_id)
        assert response.status_code == 404

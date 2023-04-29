from model.api.versions.base_api import BaseApi


class ResourceApi(BaseApi):
    """
    Methods for resources
    """

    base_url = "https://reqres.in/api/unknown/"

    def get_resource_list(self):
        response = self.get(self.base_url)

        return response

    def get_single_resource(self, resource_id):
        path = f"{self.base_url}{resource_id}"

        response = self.get(path)

        return response

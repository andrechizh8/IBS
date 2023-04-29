from model.api.versions.base_api import BaseApi


class UserApi(BaseApi):
    """
    Methods for users
    """

    base_url = "https://reqres.in/"

    def create_new_user(self, name, job):
        path = "api/users"
        body = {
            "name": name,
            "job": job
        }

        post_result = self.post(self.base_url + path, body)

        return post_result

    def get_single_user(self, user_id):
        path = f"api/users/{user_id}"

        get_result = self.get(self.base_url + path)

        return get_result

    def get_single_user_body(self, user_id):
        path = f"api/users/{user_id}"

        get_result = self.get(self.base_url + path)

        return get_result.text.replace(' ', '')

    def get_users_list(self, value):
        path = f"api/users?page={value}"

        get_result = self.get(self.base_url + path)

        return get_result

    def get_delayed_users_list(self, value):
        path = f"api/users?delay={value}"

        get_result = self.get(self.base_url + path)

        return get_result

    def update_user(self, user_id, name, job):
        path = f"api/users/{user_id}"
        body = {
            "name": name,
            "job": job
        }

        set_update = self.put(self.base_url + path, body)

        return set_update

    def partially_update_user(self, user_id, name, job):
        path = f"api/users/{user_id}"
        body = {
            "name": name,
            "job": job
        }

        set_update = self.patch(self.base_url + path, body)

        return set_update

    def delete_user(self, user_id):
        path = f"api/users/{user_id}"

        deleted_user = self.delete(self.base_url + path)

        return deleted_user

    def register_user(self, email, password):
        path = "api/register"
        body = {
            "email": email,
            "password": password
        }

        post_result = self.post(self.base_url + path, body)

        return post_result

    def login_user(self, email, password):
        path = "api/login"
        body = {
            "email": email,
            "password": password
        }

        post_result = self.post(self.base_url + path, body)

        return post_result

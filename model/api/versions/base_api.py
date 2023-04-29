import requests
from requests import Response


class BaseApi:
    """Base class for API using staticmethod"""

    @staticmethod
    def get(path):
        response = requests.get(path)
        return response

    @staticmethod
    def post(path, body):
        response = requests.post(path, json=body)
        return response

    @staticmethod
    def put(path, body):
        response = requests.put(path, json=body)
        return response

    @staticmethod
    def patch(path, body):
        response = requests.patch(path, json=body)
        return response

    @staticmethod
    def delete(path):
        response = requests.delete(path)
        return response

from app import create_app
import json


def get(url, headers):
    """
    GET function for tests
    :param str url: the relative URL to post to.
    :param dict headers: the header of the GET request.
    """
    response = app.test_client().get(url, headers=headers)
    data = json.loads(response.get_data(as_text=True)) \
        if response.data else None
    return response.status_code, data


def put(url, data, headers=None):
    """
    PUT function for tests
    :param str url: the relative URL to post to.
    :param dict data: the payload data.
    :param dict headers: the header of the POST request.
    """
    headers = {**{'content-type': 'application/json'}, **(headers or {})}
    response = app.test_client().put(
        url, data=json.dumps(data), headers=headers)
    data = json.loads(response.get_data(
        as_text=True)) if response.data else None
    return response.status_code, data


app = create_app()

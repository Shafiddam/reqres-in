import pytest
import requests

from settings import *


@pytest.fixture  # 1
def get_list_users():
    response = requests.get(base_url_get_list_users)
    return response


@pytest.fixture  # 2
def get_single_user():
    response = requests.get(base_url_get_single_user)
    return response


@pytest.fixture  # 3
def get_single_user_not_found():
    response = requests.get(base_url_get_single_user_not_found)
    return response


@pytest.fixture  # 4
def get_list_resource():
    response = requests.get(base_url_get_list_resource)
    return response


@pytest.fixture  # 5
def get_single_resource():
    response = requests.get(base_url_get_single_resource)
    return response


@pytest.fixture  # 6
def get_single_resource_not_found():
    response = requests.get(base_url_get_single_resource_not_found)
    return response


@pytest.fixture  # 7
def get_delayed_response():
    response = requests.get(base_url_get_delayed_response)
    return response


@pytest.fixture  # 8
def post_create():
    response = requests.post(base_url_post_create)
    return response


@pytest.fixture  # 9
def post_register_successful():
    response = requests.post(base_url_post_register_successful)
    return response


@pytest.fixture  # 10
def post_register_unsuccessful():
    response = requests.post(base_url_post_register_unsuccessful)
    return response


@pytest.fixture  # 11
def post_login_successful():
    response = requests.post(base_url_post_login_successful)
    return response


@pytest.fixture  # 12
def post_login_unsuccessful():
    response = requests.post(base_url_post_login_unsuccessful)
    return response


@pytest.fixture  # 13
def put_update():
    response = requests.put(base_url_put_update)
    return response


@pytest.fixture  # 14
def patch_update():
    response = requests.patch(base_url_patch_update)
    return response


@pytest.fixture  # 15
def delete_delete():
    response = requests.delete(base_url_delete_delete)
    return response

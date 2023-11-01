import pytest
import requests

from settings import *


@pytest.fixture
def get_list_users():
    response = requests.get(base_url_get_list_users)
    return response


@pytest.fixture
def get_single_user():
    response = requests.get(base_url_get_single_user)
    return response


@pytest.fixture
def get_single_user_not_found():
    response = requests.get(base_url_get_single_user_not_found)
    return response


@pytest.fixture
def get_list_resource():
    response = requests.get(base_url_get_list_resource)
    return response


@pytest.fixture
def get_single_resource():
    response = requests.get(base_url_get_single_resource)
    return response


@pytest.fixture
def get_single_resource_not_found():
    response = requests.get(base_url_get_single_resource_not_found)
    return response


@pytest.fixture
def get_delayed_response():
    response = requests.get(base_url_get_delayed_response)
    return response


@pytest.fixture
def post_create():
    response = requests.get(base_url_post_create)
    return response


@pytest.fixture
def post_register_successful():
    response = requests.get(base_url_post_register_successful)
    return response


@pytest.fixture
def post_register_unsuccessful():
    response = requests.get(base_url_post_register_unsuccessful)
    return response


@pytest.fixture
def post_login_successful():
    response = requests.get(base_url_post_login_successful)
    return response


@pytest.fixture
def post_login_unsuccessful():
    response = requests.get(base_url_post_login_unsuccessful)
    return response


@pytest.fixture
def put_update():
    response = requests.get(base_url_put_update)
    return response


@pytest.fixture
def patch_update():
    response = requests.get(base_url_patch_update)
    return response


@pytest.fixture
def delete_delete():
    response = requests.get(base_url_delete_delete)
    return response

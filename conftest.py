import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from settings.settings import *


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
def post_create(data):
    response = requests.post(base_url_post_create, data)
    return response


@pytest.fixture
def post_register_successful(data):
    response = requests.post(base_url_post_register_successful, data)
    return response


@pytest.fixture
def post_register_unsuccessful(data):
    response = requests.post(base_url_post_register_unsuccessful, data)
    return response


@pytest.fixture
def post_login_successful(data):
    response = requests.post(base_url_post_login_successful, data)
    return response


@pytest.fixture
def post_login_unsuccessful(data):
    response = requests.post(base_url_post_login_unsuccessful, data)
    return response


@pytest.fixture
def put_update(data):
    response = requests.put(base_url_put_update, data)
    return response


@pytest.fixture
def patch_update(data):
    response = requests.patch(base_url_patch_update, data)
    return response


@pytest.fixture
def delete_delete():
    response = requests.delete(base_url_delete_delete)
    return response


@pytest.fixture
def browser():
    chrome_options = Options()
    # chrome_options.add_argument("--lang=en-US")
    driver_path = "c:\\Chromedriver\\chromedriver.exe"
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.maximize_window()
    yield driver
    return driver

import pytest
import requests

from settings import *


@pytest.mark.positive
@pytest.mark.parametrize("page_number, expected_status", [(2, 200)])
def test_list_users_status_code(get_list_users, page_number, expected_status):
    assert get_list_users.status_code == expected_status, "Ошибка: ожидаемый результат не соответствует фактическому!"


@pytest.mark.positive
@pytest.mark.parametrize("page_number, expected_data_length", [(2, 6)])
def test_list_users_count(get_list_users, page_number, expected_data_length):
    data = get_list_users.json()
    assert len(data["data"]) == expected_data_length, \
        "Ошибка: ожидаемое количество пользователей не соответствует фактическому!"


@pytest.mark.positive
def test_users_have_ids(get_list_users):
    data = get_list_users.json()
    for user in data["data"]:
        assert "id" in user, "Ошибка: пользователь не имеет идентификатора (id)"


@pytest.mark.positive
def test_users_have_emails(get_list_users):
    """ Проверка, что все пользователи имеют адреса электронной почты (email)"""
    data = get_list_users.json()
    for user in data["data"]:
        assert "email" in user, "Ошибка: пользователь не имеет адреса электронной почты (email)"


@pytest.mark.positive
def test_response_contains_support_info(get_list_users):
    """ Проверка, что ответ содержит информацию о поддержке """
    data = get_list_users.json()
    assert "support" in data, "Ошибка: ответ не содержит информацию о поддержке"


@pytest.mark.negative
@pytest.mark.parametrize("page_number, expected_statuses", [(2, [400, 401, 403])])
def test_list_users_wrong_status_code(get_list_users, page_number, expected_statuses):
    assert not get_list_users.status_code in expected_statuses, "Ошибка: ожидаемый результат равен фактическому!"


@pytest.mark.negative
@pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
def test_list_users_wrong_method(method):
    if method == 'post':
        response = requests.post(base_url_get_list_users)
        assert response.status_code == 201, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'delete':
        response = requests.delete(base_url_get_list_users)
        assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'put':
        response = requests.put(base_url_get_list_users)
        assert response.status_code == 404, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'patch':
        response = requests.patch(base_url_get_list_users)
        assert response.status_code == 404, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'options':
        response = requests.options(base_url_get_list_users)
        assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"

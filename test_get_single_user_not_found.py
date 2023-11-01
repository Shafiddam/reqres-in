from conftest import *


@pytest.mark.positive
@pytest.mark.parametrize('expected_status', [404])
def test_get_single_user_not_found_status_code(get_single_user_not_found, expected_status):
    assert get_single_user_not_found.status_code == expected_status, "Ошибка: ожидаемый результат не соответствует фактическому!"


@pytest.mark.positive
def test_get_single_user_not_found_empty_response(get_single_user_not_found):
    """ Позитивный тест для проверки, что ответ содержит пустой объект """
    data = get_single_user_not_found.json()
    assert data == {}, "Ошибка: ожидается пустой объект в ответе."


@pytest.mark.negative
@pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
def test_get_single_user_wrong_method(method):
    if method == 'post':
        response = requests.post(base_url_get_single_user_not_found)
        assert response.status_code == 201, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'delete':
        response = requests.delete(base_url_get_single_user_not_found)
        assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'put':
        response = requests.put(base_url_get_single_user_not_found)
        assert response.status_code == 200, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'patch':
        response = requests.patch(base_url_get_single_user_not_found)
        assert response.status_code == 200, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'options':
        response = requests.options(base_url_get_single_user_not_found)
        assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"

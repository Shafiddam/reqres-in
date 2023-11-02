from conftest import *


@pytest.mark.positive
@pytest.mark.parametrize('expected_status', [200])
def test_get_single_resource_status_code(get_single_resource, expected_status):
    assert get_single_resource.status_code == expected_status, "Ошибка: ожидаемый результат не равен фактическому!"


@pytest.mark.positive
def test_get_single_resource(get_single_resource):
    expected_data = {
        "data": {
            "id": 2,
            "name": "fuchsia rose",
            "year": 2001,
            "color": "#C74375",
            "pantone_value": "17-2031"
        },
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    response_data = get_single_resource.json()
    assert response_data == expected_data, "Ошибка: ожидаемый результат не равен фактическому!"


@pytest.mark.negative
def test_get_single_resource_not_empty_response(get_single_resource):
    """ Проверка что ответ не содержит пустой объект """
    data = get_single_resource.json()
    assert data != {}, "Ошибка: ожидается не пустой объект в ответе"


@pytest.mark.negative
def test_get_single_resource_status_code(get_single_resource):
    """ Попытка получить несуществующего пользователя """
    wrong_url = "https://reqres.in/api/unknown/24444"
    response = requests.get(wrong_url)
    data = response.json()
    assert response.status_code == 404, "Ошибка: ожидается статус код 404"
    assert data == {}, "Ошибка: ожидается пустой объект в ответе"


@pytest.mark.negative
@pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
def test_get_single_resource_wrong_method(method):
    if method == 'post':
        response = requests.post(base_url_get_single_resource)
        assert response.status_code == 201, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'delete':
        response = requests.delete(base_url_get_single_resource)
        assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'put':
        response = requests.put(base_url_get_single_resource)
        assert response.status_code == 200, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'patch':
        response = requests.patch(base_url_get_single_resource)
        assert response.status_code == 200, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'options':
        response = requests.options(base_url_get_single_resource)
        assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"

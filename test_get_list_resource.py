from conftest import *


@pytest.mark.positive
@pytest.mark.parametrize('expected_status', [200])
def test_get_list_resource_status_code(get_list_resource, expected_status):
    assert get_list_resource.status_code == expected_status, "Ошибка: ожидаемый результат не равен фактическому!"


@pytest.mark.positive
def test_get_list_resource_data(get_list_resource):
    expected_data = {
        "page": 1,
        "per_page": 6,
        "total": 12,
        "total_pages": 2,
        "data": [
            {"id": 1, "name": "cerulean", "year": 2000, "color": "#98B2D1", "pantone_value": "15-4020"},
            {"id": 2, "name": "fuchsia rose", "year": 2001, "color": "#C74375", "pantone_value": "17-2031"},
            {"id": 3, "name": "true red", "year": 2002, "color": "#BF1932", "pantone_value": "19-1664"},
            {"id": 4, "name": "aqua sky", "year": 2003, "color": "#7BC4C4", "pantone_value": "14-4811"},
            {"id": 5, "name": "tigerlily", "year": 2004, "color": "#E2583E", "pantone_value": "17-1456"},
            {"id": 6, "name": "blue turquoise", "year": 2005, "color": "#53B0AE", "pantone_value": "15-5217"}
        ],
        "support": {
            "url": "https://reqres.in/#support-heading",
            "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
        }
    }
    response_data = get_list_resource.json()
    assert response_data == expected_data, "Ошибка: ожидаемый результат не равен фактическому!"
    # Проверяем, что все поля присутствуют
    assert 'page' in response_data, "page отсутствует в ответе"
    assert 'per_page' in response_data, "per_page отсутствует в ответе"
    assert 'total' in response_data, "total отсутствует в ответе"
    assert 'total_pages' in response_data, "total_pages отсутствует в ответе"
    assert 'data' in response_data, "data отсутствует в ответе"
    assert 'support' in response_data, "support отсутствует в ответе"


@pytest.mark.negative
def test_get_list_resource_not_empty_response(get_list_resource):
    """ Проверка что ответ не содержит пустой объект """
    data = get_list_resource.json()
    assert data != {}, "Ошибка: ожидается не пустой объект в ответе"


@pytest.mark.negative
@pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
def test_get_list_resource_wrong_method(method):
    if method == 'post':
        response = requests.post(base_url_get_list_resource)
        assert response.status_code == 201, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'delete':
        response = requests.delete(base_url_get_list_resource)
        assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'put':
        response = requests.put(base_url_get_list_resource)
        assert response.status_code == 404, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'patch':
        response = requests.patch(base_url_get_list_resource)
        assert response.status_code == 404, f"Ошибка: статус код для метода {method} неверный!"
    elif method == 'options':
        response = requests.options(base_url_get_list_resource)
        assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"

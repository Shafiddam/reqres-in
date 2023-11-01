from conftest import *


@pytest.mark.positive
@pytest.mark.parametrize('expected_status', [200])
def test_get_single_user_status_code(get_single_user, expected_status):
    assert get_single_user.status_code == expected_status, "Ошибка: ожидаемый результат не соответствует фактическому!"


@pytest.mark.positive
def test_get_single_user_required_fields(get_single_user):
    data = get_single_user.json()["data"]
    assert "id" in data, "Ошибка: поле 'id' отсутствует в ответе."
    assert "email" in data, "Ошибка: поле 'email' отсутствует в ответе."
    assert "first_name" in data, "Ошибка: поле 'first_name' отсутствует в ответе."
    assert "last_name" in data, "Ошибка: поле 'last_name' отсутствует в ответе."


@pytest.mark.positive
def test_get_single_user_first_name(get_single_user):
    data = get_single_user.json()["data"]
    expected_first_name = "Janet"
    assert data["first_name"] == expected_first_name, f"Ошибка: ожидается '{expected_first_name}' для 'first_name'."


@pytest.mark.positive
def test_get_single_user_support_link(get_single_user):
    support = get_single_user.json()["support"]
    assert "url" in support, "Ошибка: поле 'url' для поддержки отсутствует в ответе"


@pytest.mark.negative
def test_get_single_user_not_found_status_code():
    """ Попытка получить несуществующего пользователя """
    response = requests.get("https://reqres.in/api/users/999")
    assert response.status_code == 404, "Ошибка: ожидается статус код 404."


@pytest.mark.negative
@pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
def test_get_single_user_wrong_method(method):
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

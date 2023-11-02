from conftest import *


class TestGetListUsers:
    @pytest.mark.positive
    @pytest.mark.parametrize("page_number, expected_status", [(2, 200)])
    def test_list_users_status_code(self, get_list_users, page_number, expected_status):
        assert get_list_users.status_code == expected_status, "Ошибка: ожидаемый результат не соответствует фактическому!"

    @pytest.mark.positive
    @pytest.mark.parametrize("page_number, expected_data_length", [(2, 6)])
    def test_list_users_count(self, get_list_users, page_number, expected_data_length):
        data = get_list_users.json()
        assert len(data["data"]) == expected_data_length, \
            "Ошибка: ожидаемое количество пользователей не соответствует фактическому!"

    @pytest.mark.positive
    def test_users_have_ids(self, get_list_users):
        data = get_list_users.json()
        for user in data["data"]:
            assert "id" in user, "Ошибка: пользователь не имеет идентификатора (id)"

    @pytest.mark.positive
    def test_users_have_emails(self, get_list_users):
        """ Проверка, что все пользователи имеют адреса электронной почты (email)"""
        data = get_list_users.json()
        for user in data["data"]:
            assert "email" in user, "Ошибка: пользователь не имеет адреса электронной почты (email)"

    @pytest.mark.positive
    def test_response_contains_support_info(self, get_list_users):
        """ Проверка, что ответ содержит информацию о поддержке """
        data = get_list_users.json()
        assert "support" in data, "Ошибка: ответ не содержит информацию о поддержке"

    @pytest.mark.negative
    @pytest.mark.parametrize("page_number, expected_statuses", [(2, [400, 401, 403])])
    def test_list_users_wrong_status_code(self, get_list_users, page_number, expected_statuses):
        assert not get_list_users.status_code in expected_statuses, "Ошибка: ожидаемый результат равен фактическому!"

    @pytest.mark.negative
    @pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
    def test_list_users_wrong_method(self, method):
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


class TestGetSingleUser:
    @pytest.mark.positive
    @pytest.mark.parametrize('expected_status', [200])
    def test_get_single_user_status_code(self, get_single_user, expected_status):
        assert get_single_user.status_code == expected_status, "Ошибка: ожидаемый результат не соответствует фактическому!"

    @pytest.mark.positive
    def test_get_single_user_required_fields(self, get_single_user):
        data = get_single_user.json()["data"]
        assert "id" in data, "Ошибка: поле 'id' отсутствует в ответе."
        assert "email" in data, "Ошибка: поле 'email' отсутствует в ответе."
        assert "first_name" in data, "Ошибка: поле 'first_name' отсутствует в ответе."
        assert "last_name" in data, "Ошибка: поле 'last_name' отсутствует в ответе."

    @pytest.mark.positive
    def test_get_single_user_first_name(self, get_single_user):
        data = get_single_user.json()["data"]
        expected_first_name = "Janet"
        assert data["first_name"] == expected_first_name, f"Ошибка: ожидается '{expected_first_name}' для 'first_name'."

    @pytest.mark.positive
    def test_get_single_user_support_link(self, get_single_user):
        support = get_single_user.json()["support"]
        assert "url" in support, "Ошибка: поле 'url' для поддержки отсутствует в ответе"

    @pytest.mark.negative
    def test_get_single_user_not_found_status_code(self):
        """ Попытка получить несуществующего пользователя """
        response = requests.get("https://reqres.in/api/users/999")
        assert response.status_code == 404, "Ошибка: ожидается статус код 404."

    @pytest.mark.negative
    @pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
    def test_get_single_user_wrong_method(self, method):
        if method == 'post':
            response = requests.post(base_url_get_single_user)
            assert response.status_code == 201, f"Ошибка: статус код для метода {method} неверный!"
        elif method == 'delete':
            response = requests.delete(base_url_get_single_user)
            assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"
        elif method == 'put':
            response = requests.put(base_url_get_single_user)
            assert response.status_code == 200, f"Ошибка: статус код для метода {method} неверный!"
        elif method == 'patch':
            response = requests.patch(base_url_get_single_user)
            assert response.status_code == 200, f"Ошибка: статус код для метода {method} неверный!"
        elif method == 'options':
            response = requests.options(base_url_get_single_user)
            assert response.status_code == 204, f"Ошибка: статус код для метода {method} неверный!"


class TestGetSingleUserNotFound:
    @pytest.mark.positive
    @pytest.mark.parametrize('expected_status', [404])
    def test_get_single_user_not_found_status_code(self, get_single_user_not_found, expected_status):
        assert get_single_user_not_found.status_code == expected_status, "Ошибка: ожидаемый результат не соответствует фактическому!"


    @pytest.mark.positive
    def test_get_single_user_not_found_empty_response(self, get_single_user_not_found):
        """ Позитивный тест для проверки, что ответ содержит пустой объект """
        data = get_single_user_not_found.json()
        assert data == {}, "Ошибка: ожидается пустой объект в ответе."


    @pytest.mark.negative
    @pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
    def test_get_single_user_wrong_method(self, method):
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


class TestGetListResource:
    @pytest.mark.positive
    @pytest.mark.parametrize('expected_status', [200])
    def test_get_list_resource_status_code(self, get_list_resource, expected_status):
        assert get_list_resource.status_code == expected_status, "Ошибка: ожидаемый результат не равен фактическому!"

    @pytest.mark.positive
    def test_get_list_resource_data(self, get_list_resource):
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
    def test_get_list_resource_not_empty_response(self, get_list_resource):
        """ Проверка что ответ не содержит пустой объект """
        data = get_list_resource.json()
        assert data != {}, "Ошибка: ожидается не пустой объект в ответе"

    @pytest.mark.negative
    @pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
    def test_get_list_resource_wrong_method(self, method):
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


class TestGetSingleResource:
    @pytest.mark.positive
    @pytest.mark.parametrize('expected_status', [200])
    def test_get_single_resource_status_code(get_single_resource, expected_status):
        assert get_single_resource.status_code == expected_status, "Ошибка: ожидаемый результат не равен фактическому!"

    @pytest.mark.positive
    def test_get_single_resource(self, get_single_resource):
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
    def test_get_single_resource_not_empty_response(self, get_single_resource):
        """ Проверка что ответ не содержит пустой объект """
        data = get_single_resource.json()
        assert data != {}, "Ошибка: ожидается не пустой объект в ответе"

    @pytest.mark.negative
    def test_get_single_resource_status_code(self, get_single_resource):
        """ Попытка получить несуществующего пользователя """
        wrong_url = "https://reqres.in/api/unknown/24444"
        response = requests.get(wrong_url)
        data = response.json()
        assert response.status_code == 404, "Ошибка: ожидается статус код 404"
        assert data == {}, "Ошибка: ожидается пустой объект в ответе"

    @pytest.mark.negative
    @pytest.mark.parametrize('method', ['post', 'delete', 'put', 'patch', 'options'])
    def test_get_single_resource_wrong_method(self, method):
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




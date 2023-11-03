import json
from time import sleep

from conftest import *
from pages.base_page import BasePage

error_status_code = "Ошибка: response_code на странице не соответствует получаемому по апи!"
error_output_response = "Ошибка: тело ответа на странице не соответствует получаемому по апи!"


def test_get_list_users(browser, get_list_users):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_get_list_users()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = get_list_users.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = get_list_users.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


def test_get_single_user(browser, get_single_user):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_get_single_user()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = get_single_user.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = get_single_user.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


def test_get_single_user_not_found(browser, get_single_user_not_found):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_get_single_user_not_found()
        sleep(3)

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = get_single_user_not_found.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = get_single_user_not_found.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


def test_get_list_resource(browser, get_list_resource):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_get_list_resource()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = get_list_resource.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = get_list_resource.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


def test_get_single_resource(browser, get_single_resource):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_get_single_resource()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = get_single_resource.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = get_single_resource.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


def test_get_single_resource_not_found(browser, get_single_resource_not_found):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_get_single_resource_not_found()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = get_single_resource_not_found.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = get_single_resource_not_found.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


@pytest.mark.parametrize('data', [{"name": "morpheus", "job": "leader"}])
def test_post_create(browser, post_create, data):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_post_create()
        sleep(3)

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = post_create.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = post_create.json()

        # проверяем только два поля, а не весь ответ, так как поля "сreatedAt" и 'id' динамические:
        assert data["name"] == output_response["name"], f"{error_output_response}"
        assert data["job"] == output_response["job"], f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


@pytest.mark.parametrize('data', [{"name": "morpheus", "job": "zion resident"}])
def test_put_update(browser, put_update, data):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_put_update()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = put_update.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = put_update.json()

        # проверяем только два поля, а не весь ответ, так как поле "сreatedAt" динамическое:
        assert data["name"] == output_response["name"], f"{error_output_response}"
        assert data["job"] == output_response["job"], f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


@pytest.mark.parametrize('data', [{"name": "morpheus", "job": "zion resident"}])
def test_patch_update(browser, patch_update, data):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_patch_update()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = patch_update.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = patch_update.json()

        # проверяем только два поля, а не весь ответ, так как поле "сreatedAt" динамическое:
        assert data["name"] == output_response["name"], f"{error_output_response}"
        assert data["job"] == output_response["job"], f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


def test_delete_delete(browser, delete_delete):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_delete_delete()
        sleep(3)

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = delete_delete.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_empty_output_response_from_site()

        try:
            data = delete_delete.json()
        except json.JSONDecodeError:
            data = ''

        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


@pytest.mark.parametrize('data', [{"email": "eve.holt@reqres.in", "password": "pistol"}])
def test_post_register_successful(browser, post_register_successful, data):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_post_register_successful()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = post_register_successful.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = post_register_successful.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


@pytest.mark.parametrize('data', [{"email": "sydney@fife"}])
def test_post_register_unsuccessful(browser, post_register_unsuccessful, data):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_post_register_unsuccessful()
        sleep(3)

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = post_register_unsuccessful.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = post_register_unsuccessful.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


@pytest.mark.parametrize('data', [{"email": "eve.holt@reqres.in", "password": "cityslicka"}])
def test_post_login_successful(browser, post_login_successful, data):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_post_login_successful()

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = post_login_successful.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = post_login_successful.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


@pytest.mark.parametrize('data', [{"email": "peter@klaven"}])
def test_post_login_unsuccessful(browser, post_login_unsuccessful, data):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_post_login_unsuccessful()
        sleep(3)

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = post_login_unsuccessful.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = post_login_unsuccessful.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()


def test_get_delayed_response(browser, get_delayed_response):
    base_page = BasePage(browser)

    try:
        base_page.open()
        base_page.click_btn_get_delayed_response()
        sleep(4)

        response_code_from_site = base_page.get_response_code_from_site()
        expected_code_from_api = get_delayed_response.status_code
        assert response_code_from_site == expected_code_from_api, f"{error_status_code}"

        output_response = base_page.get_output_response_from_site()
        data = get_delayed_response.json()
        assert data == output_response, f"{error_output_response}"

    except Exception as e:
        pytest.fail(f"ERROR: {str(e)}")
    finally:
        browser.quit()
import json

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup


class BasePage:
    class Locators:
        BASE_URL = 'https://reqres.in/'
        BTN_GET_LIST_USERS = (By.CSS_SELECTOR, 'li[data-id="users"]')
        BTN_GET_SINGLE_USER = (By.CSS_SELECTOR, 'li[data-id="users-single"]')
        BTN_GET_SINGLE_USER_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="users-single-not-found"]')
        BTN_GET_LIST_RESOURCE = (By.CSS_SELECTOR, 'li[data-id="unknown"][data-key="endpoint"]')
        BTN_GET_SINGLE_RESOURCE = (By.CSS_SELECTOR, 'li[data-id="unknown-single"][data-key="endpoint"]')
        BTN_GET_SINGLE_RESOURCE_NOT_FOUND = (By.CSS_SELECTOR, 'li[data-id="unknown-single-not-found"]')
        BTN_POST_CREATE = (By.CSS_SELECTOR, 'li[data-id="post"][data-key="endpoint"]')
        BTN_PUT_UPDATE = (By.CSS_SELECTOR, 'li[data-id="put"][data-key="endpoint"]')
        BTN_PATCH_UPDATE = (By.CSS_SELECTOR, 'li[data-id="patch"][data-key="endpoint"]')
        BTN_DELETE_DELETE = (By.CSS_SELECTOR, 'li[data-id="delete"][data-key="endpoint"]')
        BTN_POST_REGISTER_SUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="register-successful"][data-key="endpoint"]')
        BTN_POST_REGISTER_UNSUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="register-unsuccessful"][data-key="endpoint"]')
        BTN_POST_LOGIN_SUCCESSFUL = (By.CSS_SELECTOR, 'li[data-id="login-successful"][data-key="endpoint"]')

        RESPONSE_CODE = (By.CSS_SELECTOR, 'span[class*="response-code"]')
        OUTPUT_RESPONSE_FROM_SITE = (By.CSS_SELECTOR, 'pre[data-key="output-response"]')

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.timeout = timeout

    def open(self):
        self.driver.get(self.Locators.BASE_URL)

    def click_btn_get_list_users(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GET_LIST_USERS)).click()

    def click_btn_get_single_user(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GET_SINGLE_USER)).click()

    def click_btn_get_single_user_not_found(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GET_SINGLE_USER_NOT_FOUND)).click()

    def click_btn_get_list_resource(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GET_LIST_RESOURCE)).click()

    def click_btn_get_single_resource(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GET_SINGLE_RESOURCE)).click()

    def click_btn_get_single_resource_not_found(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_GET_SINGLE_RESOURCE_NOT_FOUND)).click()

    def click_btn_post_create(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_POST_CREATE)).click()

    def click_btn_put_update(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PUT_UPDATE)).click()

    def click_btn_patch_update(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_PATCH_UPDATE)).click()

    def click_btn_delete_delete(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_DELETE_DELETE)).click()

    def click_btn_post_register_successful(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_POST_REGISTER_SUCCESSFUL)).click()

    def click_btn_post_register_unsuccessful(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_POST_REGISTER_UNSUCCESSFUL)).click()

    def click_btn_post_login_successful(self):
        self.wait.until(EC.visibility_of_element_located(self.Locators.BTN_POST_LOGIN_SUCCESSFUL)).click()











    def get_response_code_from_site(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.RESPONSE_CODE))
        response_code = int(element.text)
        return response_code

    def get_output_response_from_site(self):
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.OUTPUT_RESPONSE_FROM_SITE))
        html_text = element.get_attribute('innerHTML')
        soup = BeautifulSoup(html_text, 'html.parser')
        json_text = soup.get_text()
        json_data = json.loads(json_text)
        return json_data

    def get_empty_output_response_from_site(self):
        """ должен вернуть пустую строку """
        element = self.wait.until(EC.visibility_of_element_located(self.Locators.OUTPUT_RESPONSE_FROM_SITE))
        element_text = element.text
        return element_text

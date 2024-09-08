import allure
import requests
from api.api_url import ApiUrl
from helper.generate_random_courier import create_login_courier_random, create_pass_courier_random, \
    create_name_courier_random
from helper.text_answer import TextAnswer


class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера')
    def test_courier_login_passed(self):
        data = {'login': create_login_courier_random(),
                'password': create_pass_courier_random(),
                'first_name': create_name_courier_random()}
        requests.post(ApiUrl.CREATE_COURIER_API_URL, data=data)
        response = requests.post(ApiUrl.LOGIN_COURIER_API_URL, data=data)
        assert response.status_code == 200
        assert 'id' in response.text

    @allure.title('Проверка попытки авторизации курьера без заполнения поля login')
    def test_not_required_field_login_courier(self):
        data = {'login': None,
                'password': create_pass_courier_random(),
                'name': create_name_courier_random()}
        response = requests.post(ApiUrl.LOGIN_COURIER_API_URL, data=data)
        assert response.status_code == 400
        assert response.json()['message'] == TextAnswer.not_login_courier

    @allure.title('Проверка попытки авторизации курьера без заполнения поля password')
    def test_not_required_field_password_courier(self):
        data = {'login': create_login_courier_random(),
                'password': None,
                'name': create_name_courier_random()}
        response = requests.post(ApiUrl.LOGIN_COURIER_API_URL, data=data)
        assert response.status_code == 400
        assert response.json()['message'] == TextAnswer.not_login_courier

    @allure.title('Проверка авторизации несуществующим курьером')
    def test_no_such_username_and_password(self):
        data = {'login': create_login_courier_random(),
                'password': create_pass_courier_random(),
                'first_name': create_name_courier_random()}
        response = requests.post(ApiUrl.LOGIN_COURIER_API_URL, data=data)
        assert response.status_code == 404
        assert response.json()['message'] == TextAnswer.no_such_username_and_password

    def test_authorization_incorrect_login(self):
        data = {'login': 'inanimateness',
                'password': '1234',
                'first_name': 'Ниндзя'}
        response = requests.post(ApiUrl.LOGIN_COURIER_API_URL, data=data)
        assert response.status_code == 404
        assert response.json()['message'] == TextAnswer.no_such_username_and_password

    def test_authorization_incorrect_password(self):
        data = {'login': 'nina',
                'password': '123456789',
                'first_name': 'Ниндзя'}
        response = requests.post(ApiUrl.LOGIN_COURIER_API_URL, data=data)
        assert response.status_code == 404
        assert response.json()['message'] == TextAnswer.no_such_username_and_password

import allure
import pytest
import requests
from api.api_url import ApiUrl
from helper.generate_random_courier import create_login_courier_random, create_pass_courier_random, create_name_courier_random
from helper.text_answer import TextAnswer


class TestCreateCourier:
    @allure.title('Проверка создания аккаунта курьера')
    def test_create_courier(self):
        data = {'login': create_login_courier_random(),
                'password': create_pass_courier_random(),
                'name': create_name_courier_random()}
        response = requests.post(ApiUrl.CREATE_COURIER_API_URL, data=data)
        assert response.status_code == 201, response.json == TextAnswer.create_courier

    @allure.title('Проверка невозможности создания двух одинаковых аккаунтов курьеров')
    def test_duplicate_courier(self):
        data = {'login': 'nina',
                'password': create_pass_courier_random(),
                'name': create_name_courier_random()}
        requests.post(ApiUrl.CREATE_COURIER_API_URL, data=data)
        response = requests.post(ApiUrl.CREATE_COURIER_API_URL, data=data)
        assert response.status_code == 409, response.json()['message'] == TextAnswer.duplicate_courier

    @allure.title('Проверка невозможности регистрации курьера без одного обязательного поля')
    @pytest.mark.parametrize('login, password, first_name', [
        (None, create_pass_courier_random(), create_name_courier_random()),
        (create_login_courier_random(), None, create_name_courier_random())])
    def test_not_once_required_field(self, login, password, first_name):
        data = {'login': login, 'password': password, 'first_name': first_name}
        response = requests.post(ApiUrl.CREATE_COURIER_API_URL, data=data)
        assert response.status_code == 400 and response.json()['message'] == TextAnswer.not_once_required_field

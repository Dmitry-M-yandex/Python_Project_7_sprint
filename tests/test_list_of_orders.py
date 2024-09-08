import allure
import random
import requests
from api.api_url import ApiUrl


class TestOrderList:

    @allure.title("Тест проверяет, что метод возвращает список заказов")
    def test_get_order_list(self):
        params = {'limit': random.randint(1, 3)}
        response = requests.get(ApiUrl.LIST_OF_ORDERS, params=params, timeout=(10, 30))
        assert response.status_code == 200
        assert response.json()["orders"] != []

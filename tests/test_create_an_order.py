import allure
import pytest
import requests
from api.api_url import ApiUrl


class TestOrderCreation:

    @pytest.mark.parametrize("color",
                             ["BLACK",
                              "GREY",
                              ("BLACK", "GREY"),
                              None])
    @allure.title("Тест проверяет создание заказа с разными цветами")
    def test_order_creation_success(self, creating_an_order, color):
        data = {
            "firstName": creating_an_order.get('first_name'),
            "lastName": creating_an_order.get('last_name'),
            "address": creating_an_order.get('address'),
            "metroStation": creating_an_order.get('metro_station'),
            "phone": creating_an_order.get('phone'),
            "rentTime": creating_an_order.get('rent_time'),
            "deliveryDate": creating_an_order.get('delivery_date'),
            "comment": creating_an_order.get('comment'),
            "color": color}
        response = requests.post(ApiUrl.CREATING_AN_ORDER, data=data)
        assert response.status_code == 201
        assert 'track' in response.text

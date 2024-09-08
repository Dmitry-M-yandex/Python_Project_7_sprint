# Python_Project_7_sprint
<h1>API тесты для сервиса «Яндекс.Самокат»</h1>

# <h3>test_not_required_field_password_courier</h3>
При авторизации курьера без заполнения поля password, статус код 504 вместо 400

# <h3>test_order_creation_success</h3>
При создании заказа с одним цветом, статус код 500 вместо 201

<h2>Отчеты Allure</h2>

Для просмотра отчетов Allure вам необходимо после запуска тестов выполнить команду <code>allure serve
allure_results</code>.

<h2>Запуск тестов</h2>

Чтобы запустить тесты, нужно выполнить команду <code>pytest tests --alluredir=allure_results</code>.

<h2>Установить зависимости</h2>
Чтобы установить зависимости, нужно выполнить команду <code>pip install -r requirements.txt</code>.


import pytest


@pytest.fixture
def set_up():
    print("Вход в систему выполнен(использование фикстуры)")
    yield
    print("Выход из системы(операция, "
          "выполненная после завершения тестов)")

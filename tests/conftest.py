import pytest


# выполнение для каждой функции(по умолчанию)
@pytest.fixture(scope="function")
def set_up_function():
    print("Вход в систему выполнен(операция, "
          "выполненная до начала тестов)")
    yield
    print("Выход из системы(операция, "
          "выполненная после завершения тестов)")


# выполнение до начала теста первой функции
# и завершение после теста последней функции в модуле
@pytest.fixture(scope="module")
def set_up_module():
    print("Вход в систему выполнен(операция, "
          "выполненная до начала тестов)")
    yield
    print("Выход из системы(операция, "
          "выполненная после завершения тестов)")

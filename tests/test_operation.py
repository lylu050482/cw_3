from src.models import Operation


def test_operation_convert_date():
    """
    Тест для проверки метода класса преобразования даты в нужный вид
    """
    operation = Operation(pk=123421,
                          state="EXECUTED",
                          date="2019-07-03T18:35:29.512364",
                          operation_amount={
                              "amount": "8221.37",
                              "currency": {
                                  "name": "USD",
                                  "code": "USD"
                              }
                          },
                          description="Перевод организации",
                          from_="Visa Classic 6831982476737658",
                          to="Счет 38976430693692818358"
                          )
    assert operation.convert_date("2019-07-03T18:35:29.512364") == "03.07.2019"


def test_operation_convert_info_payment():
    """
    Тест для проверки метода вывода информации о платеже в нужном виде
    """
    operation = Operation(pk=123421,
                          state="EXECUTED",
                          date="2019-07-03T18:35:29.512364",
                          operation_amount={
                              "amount": "8221.37",
                              "currency": {
                                  "name": "USD",
                                  "code": "USD"
                              }
                          },
                          description="Перевод организации",
                          from_="Visa Classic 6831982476737658",
                          to="Счет 38976430693692818358")
    assert operation.convert_info_payment("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert operation.convert_info_payment("Счет 38976430693692818358") == "Счет **8358"
    assert operation.convert_info_payment("") == "Данные отправителя отсутствуют"

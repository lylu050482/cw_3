import pytest

from src.models import Operation


@pytest.fixture
def operation_instance():
    """
    Данные для test_get_executed_operations
    и test_sort_operations_by_date
    """
    instance_oper = Operation(
        pk=123421,
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
        to="Счет 38976430693692815332"
    )
    instance_oper_2 = Operation(
        pk=128765321,
        state="CANCELED",
        date="2018-11-23T17:47:33.127140",
        operation_amount={
            "amount": "8221.37",
            "currency": {
                "name": "руб.",
                "code": "USD"
            }
        },
        description="Перевод организации",
        from_="Visa Classic 6831982476737658",
        to="Счет 38976430693692818358"
    )
    return [instance_oper, instance_oper_2]


@pytest.fixture
def operation_dict():
    """
    Данные для test_get_instances_class
    """
    return [
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        },
        {},
        {
            "id": 407169720,
            "state": "EXECUTED",
            "date": "2018-02-03T14:52:08.093722",
            "operationAmount": {
                "amount": "67011.26",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "MasterCard 4047671689373225",
            "to": "Maestro 3806652527413662"
        }
    ]
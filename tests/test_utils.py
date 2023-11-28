from datetime import datetime

from src.models import Operation
from src.utils import get_instances, get_executed, sort_operations_by_date


def test_get_instances_class(operation_dict):
    """
    Тест для проверки функции получения одного экземпляра
    """
    operations = get_instances(operation_dict)
    assert operations[1].pk == 407169720
    assert isinstance(operations, list)
    assert operations[1].operation_amount["amount"] == "67011.26"
    assert isinstance(operations[0], Operation)
    assert len(operations) == 2


def test_get_executed_operations(operation_instance):
    """
    Тест для проверки функции получения списка экземпляров с выполненными операциями
    """
    executed_operation = get_executed(operation_instance)
    assert len(executed_operation) == 1
    assert executed_operation[0].state == "EXECUTED"
    assert isinstance(executed_operation, list)
    assert isinstance(executed_operation[0], Operation)
    assert executed_operation[0].to == "Счет **5332"


def test_sort_operations_by_date(operation_instance):
    """
    Тест для проверки функции сортировки выполненных операций, начинающихся с последней выполненной операции
    """
    sort_date = sort_operations_by_date(operation_instance)
    assert len(sort_date) == 2
    assert isinstance(sort_date, list)
    assert isinstance(sort_date[0], Operation)
    assert datetime.strptime(sort_date[0].date, "%d.%m.%Y") > datetime.strptime(sort_date[1].date, "%d.%m.%Y")
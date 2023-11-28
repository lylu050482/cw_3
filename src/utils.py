import json
from datetime import datetime

from src.models import Operation


def load_operations(path: str) -> list[dict]:
    """
    Чтение операций из файла
    :param path: путь к файлу
    :return: json с операциями
    """
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_instances(operations: list[dict]) -> list[Operation]:
    """

    :param operations:
    :return:
    """
    operation_instances = []
    for operation in operations:
        if operation:
            operation_instances.append(Operation(
                pk=operation["id"],
                state=operation["state"],
                date=operation["date"],
                operation_amount=operation["operationAmount"],
                description=operation["description"],
                from_=operation.get("from", ""),
                to=operation["to"],
            ))
    return operation_instances


def get_executed(operations: list[Operation]) -> list[Operation]:
    """

    :param operations:
    :return:
    """
    executed_operation = []
    for operation in operations:
        if operation.state == "EXECUTED":
            executed_operation.append(operation)
    return executed_operation


def sort_operations_by_date(operations: list[Operation]) -> list[Operation]:
    """

    :param operations:
    :return:
    """
    return sorted(operations, key=lambda operation: datetime.strptime(operation.date, "%d.%m.%Y"), reverse=True)

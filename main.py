from config import OPERATIONS_PATH
from src.utils import load_operations, get_instances, get_executed, sort_operations_by_date


def main():
    operations = load_operations(OPERATIONS_PATH)
    instances = get_instances(operations)
    executed_operations = get_executed(instances)
    sorted_operations = sort_operations_by_date(executed_operations)
    for operation in sorted_operations[:5]:
        print(operation)


if __name__ == '__main__':
    main()

from src.funcs import load_operations, change_date, mask_from, mask_to, filter_sorted_operations

operations = load_operations()
operations = filter_sorted_operations(operations)
for operation in operations[:5]:
    print(f"{change_date(operation['date'])} {operation['description']}")
    if operation.get("from") and "Счет" not in operation.get("from"):
        print(f'{mask_from(operation["from"])} -> {mask_to(operation["to"])}')
    elif operation.get("from") and "Счет" in operation.get("from"):
        print(f'{mask_to(operation["from"])} -> {mask_to(operation["to"])}')
    else:
        print(f'{" "} -> {mask_to(operation["to"])}')
    print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
    print()

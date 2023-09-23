from src.funcs import load_operations, change_date, mask_from, mask_to, filter_sorted_operations

operations = load_operations()
operations = filter_sorted_operations(operations)
for operation in operations[:5]:
    print(f"{change_date(operation['date'])} {operation['description']}")
    print(f"{mask_from(operation['from']) if operation.get('from') else None} -> {mask_to(operation['to'])}")
    print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}")
    print()

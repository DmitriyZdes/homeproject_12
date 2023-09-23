import json


def load_operations():
    """Выводит на экран список из 5 последних выполненных операций"""

    with open("operations.json", "r", encoding="utf-8") as file:
        return json.load(file)

def change_date(date):
    """Принимает и форматирует дату"""

    date = date.split("T")[0].split("-")
    return f"{date[2]}.{date[1]}.{date[0]}"

def mask_from(card_number):
    """Маскирует номер отправителя"""

    card_number = card_number.split(" ")
    type_card = card_number[:-1]
    masked_number = f"{card_number[-1][:4]} {card_number[-1][4:6]}** **** {card_number[-1][12:16]}"
    return f'{" ".join(type_card)} {masked_number}'

def mask_to(card_number):
    """Маскирует номер получателя"""

    card_number = card_number.split(" ")
    type_card = card_number[:-1]
    masked_number = f"**{card_number[-1][-4:]}"
    return f'{" ".join(type_card)} {masked_number}'

def filter_sorted_operations(operations):
    """Сортирует список выполненных операций"""

    operations = [operation for operation in operations if operation.get("state") == "EXECUTED"]
    operations = sorted(operations, key= lambda x: x["date"], reverse=True)
    return operations
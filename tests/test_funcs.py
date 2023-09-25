from src.funcs import change_date, mask_from, mask_to

def test_change_date():
    date = "2019-07-03T18:35:29.512364"
    expected_date = '03.07.2019'
    assert change_date(date) == expected_date

def test_mask_from():
    input_number = "MasterCard 7158300734726758"
    expected_number = 'MasterCard 7158 30** **** 6758'
    assert mask_from(input_number) == expected_number

def test_mask_to():
    input_number = "Счет 35383033474447895560"
    expected_number = 'Счет **5560'
    assert mask_to(input_number) == expected_number

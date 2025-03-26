import unittest
import datetime
from main import read_product_data, get_last_two_prices, price_change

def test_read_product_data():
    test_data = "Apple, 2025-02-20, 1.5\nApple, 2025-03-10, 2.0\nBanana, 2025-02-10, 1.0\n"
    
    with open("test_data.txt", "w") as f:
        f.write(test_data)
    
    result = read_product_data("test_data.txt")
    
    expected_result = [
        ('Apple', datetime.date(2025, 2, 20), 1.5),
        ('Apple', datetime.date(2025, 3, 10), 2.0),
        ('Banana', datetime.date(2025, 2, 10), 1.0)
    ]
    
    assert result == expected_result


def test_get_last_two_prices():
    test_data = [
        ('Apple', datetime.date(2025, 2, 20), 1.5),
        ('Apple', datetime.date(2025, 3, 10), 2.0),
        ('Banana', datetime.date(2025, 2, 10), 1.0)
    ]
    
    result = get_last_two_prices(test_data, "Apple")
    
    expected_result = [
        ('Apple', datetime.date(2025, 2, 20), 1.5),
        ('Apple', datetime.date(2025, 3, 10), 2.0)
    ]
    
    assert result == expected_result


def test_price_change():
    test_data = [
        ('Apple', datetime.date(2025, 2, 20), 1.5),
        ('Apple', datetime.date(2025, 3, 10), 2.0),
        ('Banana', datetime.date(2025, 2, 10), 1.0)
    ]
    
    result = price_change(test_data, "Apple")
    
    expected_result = 0.5
    
    assert result == expected_result


def test_price_change_not_enough_data():
    test_data = [
        ('Apple', datetime.date(2025, 2, 20), 1.5)
    ]
    
    result = price_change(test_data, "Apple")
    
    assert result is None

import pytest
from src.transaction_processor import validate_item, calculate_total, process_refund

def test_validate_item_valid():
    """Test a valid item name."""
    # Arrange
    item = "Laptop"

    # Act
    result = validate_item(item)

    # Assert
    assert result == True

def test_calculate_total_type_error():
    """TEST THE TYPE ERROR"""
    with pytest.raises(TypeError):
        calculate_total("123","111")

def test_calculate_total_value_error():
    """TEST THE TYPE ERROR"""
    with pytest.raises(ValueError):
        calculate_total(10,-20)


def test_validate_item_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        validate_item(123)

def test_validate_item_value_error():
    """TEST THAT THE VALUE ERROR IS OK"""
    with pytest.raises(ValueError):
        validate_item("a")


def test_calculate_total_basic():
    """Test a normal calculation under the discount threshold."""
    # Arrange
    price = 100
    quantity = 2

    # Act
    result = calculate_total(price, quantity)

    # Assert
    assert result == 200.0


def test_calculate_total_discount():
    """Test that a total strictly over 500 gets a 10% discount."""
    # Arrange
    price = 300
    quantity = 2

    # Act
    result = calculate_total(price, quantity)

    # Assert
    assert result == 540.0

def test_process_refund_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        process_refund("abcd")

def test_process_refund_value_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(ValueError):
        process_refund(-1000)

def test_process_refund_basic():
    result = process_refund(123)
    assert result == "Refunded #123"


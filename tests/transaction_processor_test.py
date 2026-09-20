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


def test_validate_item_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        validate_item(123)


def test_calculate_total_basic():
    """Test a normal calculation under the discount threshold."""
    # Arrange
    price = 100
    quantity = 2

    # Act
    result = calculate_total(price, quantity)

    # Assert
    assert result == 200.0


# def test_calculate_total_discount():
#     """Test that a total strictly over 500 gets a 10% discount."""
#     # Arrange
#     price = 300
#     quantity = 2
#
#     # Act
#     result = calculate_total(price, quantity)
#
#     # Assert
#     assert result == 550.0
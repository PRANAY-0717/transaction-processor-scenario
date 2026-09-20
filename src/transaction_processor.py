def validate_item(item_name):
    """Return True if the item name is valid."""
    if not isinstance(item_name, str):
        raise TypeError("Item name must be a string")
    if len(item_name) < 3:
        raise ValueError("Item name too short")
    return True


def calculate_total(price, quantity):
    """Calculate total price, applying a 10% discount if the total is strictly over 500."""
    if not isinstance(price, (int, float)) or not isinstance(quantity, int):
        raise TypeError("Invalid types for price or quantity")
    if price < 0 or quantity < 1:
        raise ValueError("Price must be positive and quantity at least 1")

    total = price * quantity
    
    if total > 500:
        return total * 0.9  # 10% discount applied
    return float(total)


def process_refund(transaction_id):
    """Process a refund. Assumes ID is valid."""
    if not isinstance(transaction_id, int):
        raise TypeError("Transaction ID must be an integer")
    if transaction_id <= 0:
        raise ValueError("Invalid transaction ID")
    return f"Refunded #{transaction_id}"
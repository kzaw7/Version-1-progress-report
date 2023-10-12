def calculate_total_price(cart):
    """
    Calculate the total price of items in the shopping cart.
    Args:
        cart (list): List of dictionaries representing items in the cart.
            Each dictionary should have 'price' and 'quantity' keys.
    Returns:
        float: Total price of items in the cart.
    """
    total_price = 0
    for item in cart:
        total_price += item['price'] * item['quantity']
    return total_price

def format_price(price):
    """
    Format the price to display with two decimal places and a currency symbol.
    Args:
        price (float): Price to be formatted.
    Returns:
        str: Formatted price as a string.
    """
    formatted_price = "${:.2f}".format(price)
    return formatted_price

def generate_order_number(user_id):
    """
    Generate a unique order number based on the user's ID.
    Args:
        user_id (int): User's ID.
    Returns:
        str: Unique order number.
    """
    order_number = "ORD-{}".format(user_id)
    return order_number
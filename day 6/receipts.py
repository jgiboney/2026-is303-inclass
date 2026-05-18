def calculate_tax(amount, tax_rate=0.0825):
    """Calculate tax for a given amount."""
    return amount * tax_rate

def print_receipt(quantities, items, subtotal, membership, discount, total):
    """Print a formatted receipt."""
    print("\n" + "="*30)
    print("FRESHCART RECEIPT")
    print("="*30)
    for qty, item in zip(quantities, items):
        print(f"{qty} x {item['name']} @ ${item['price']:.2f}")
    print("-"*30)
    print(f"Subtotal: ${subtotal:.2f}")
    if membership:
        print(f"Membership Discount: -${discount:.2f}")
    print(f"Tax: ${calculate_tax(subtotal - discount):.2f}")
    print(f"Total (incl. tax): ${total:.2f}")
    print("="*30)
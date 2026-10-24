def food_listing_is_valid(name, quantity, pickup_location):
    return bool(name.strip()) and quantity > 0 and bool(pickup_location.strip())

def available_quantity(initial_quantity, reserved_quantity):
    if reserved_quantity < 0 or initial_quantity < 0:
        raise ValueError("Quantities cannot be negative")
    if reserved_quantity > initial_quantity:
        raise ValueError("Reservation exceeds available quantity")
    return initial_quantity - reserved_quantity

import pytest
from app import food_listing_is_valid, available_quantity

def test_valid_listing():
    assert food_listing_is_valid("Bread", 10, "Dombivli")

def test_empty_name_invalid():
    assert not food_listing_is_valid(" ", 10, "Dombivli")

def test_zero_quantity_invalid():
    assert not food_listing_is_valid("Bread", 0, "Dombivli")

def test_remaining_quantity():
    assert available_quantity(10, 4) == 6

def test_reservation_over_stock_fails():
    with pytest.raises(ValueError):
        available_quantity(5, 8)

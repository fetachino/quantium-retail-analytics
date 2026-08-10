"""Unit tests for the reusable Task 1 transformations."""

import pytest

from quantium_task1_analysis import clean_brand, money


@pytest.mark.parametrize(
    ("product_name", "expected"),
    [
        ("Red Rock Deli Lime 165g", "RRD"),
        ("Dorito Corn Chips 150g", "DORITOS"),
        ("Smith Crinkle Cut 170g", "SMITHS"),
        ("Kettle Sea Salt 175g", "KETTLE"),
    ],
)
def test_clean_brand_normalizes_known_names(product_name, expected):
    assert clean_brand(product_name) == expected


def test_money_formats_currency_for_reporting():
    assert money(1234.5) == "$1,234.50"

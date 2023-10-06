import pytest
from main.db import get_db
from main.menu import *

def test_validate_form_data():
    form = {
            'category': 'Drinks',
            'code': 'D01',
            'dish': '',
            'price': '5.00'
            }

    result = validate_form_data(form)
    assert result == 'Dish is required.'

    form = {
            'category': 'Drinks',
            'code': '',
            'dish': 'Tea',
            'price': '5.00'
            }

    result = validate_form_data(form)
    assert result == 'Code is required.'

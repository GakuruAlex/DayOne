import pytest

from band_name_generator import band_name_gen

@pytest.mark.parametrize("city, pet, band_name", [
    ("Nakuru", "George", "Nakuru George"),
    ("nairobi", "tokyo", "nairobi tokyo"),
    ("Nairobi", "Tokyo", "Nairobi Tokyo"),
    ("Nairobi", "tokyo", "Nairobi tokyo"),
    ("nairobi", "Tokyo", "nairobi Tokyo")
])

def test_band_name_generator(city, pet , band_name):
    assert band_name_gen(city, pet) == band_name
    
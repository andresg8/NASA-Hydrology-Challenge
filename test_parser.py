from angle_csv_parses.py import *

def test_fetch_data():
    assert type(fetch_data()) == bytes

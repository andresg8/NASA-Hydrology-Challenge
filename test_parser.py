from angles_csv_parser import *

def test_fetch_data():
    assert type(fetch_data()) == bytes

def test_print_data():
    print_data(fetch_data())

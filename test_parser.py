from angles_csv_parser import *

def test_fetch_data():
    assert type(fetch_data()) == bytes

def test_parse_data():
    data = fetch_data().decode('utf-8')
    lines = data.split('\r\n')
    values = parse_data(lines)
    for value in values:
        assert len(value) == 2
        try:
            float(value[0])
            float(value[1])
        except ValueError:
            raise AssertionError()

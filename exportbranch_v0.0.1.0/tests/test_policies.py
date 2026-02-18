from core.policies import normalize_filename

def test_invalid_chars_removed():
    assert normalize_filename("a<b>c.txt") == "abc.txt"

def test_reserved_name():
    assert normalize_filename("CON.txt") == "_CON.txt"

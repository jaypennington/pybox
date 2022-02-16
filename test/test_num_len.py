import pybox.src.num_len.num_len as nl

def test_num_len():
    assert nl.num_len(1) == 1
    assert nl.num_len(12) == 2
    assert nl.num_len(997) == 3
    assert nl.num_len(12324) == 5
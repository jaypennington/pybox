import pybox.src.tallest_skyscraper.tallest_skyscraper as ts


def test_tallest_skyscraper():
    assert ts.tallest_skyscraper([
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]]) == 3

    assert ts.tallest_skyscraper([
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 1, 0],
        [1, 1, 1, 1]]) == 4

    assert ts.tallest_skyscraper([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [1, 1, 1, 1]]) == 2
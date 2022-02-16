import pybox.src.unlucky.unlucky as ul

def test_unlucky():
    arr0 = []
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 13]
    arr3 = [1, 2, 13, 3]
    arr4 = [1, 2, 13, 3, 4]
    arr5 = [1, 2, 13, 13, 3, 4]

    assert ul.unlucky(arr0) == 0
    assert ul.unlucky(arr1) == 6
    assert ul.unlucky(arr2) == 3
    assert ul.unlucky(arr3) == 3
    assert ul.unlucky(arr4) == 7
    assert ul.unlucky(arr5) == 7

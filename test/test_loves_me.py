import pybox.src.loves_me.loves_me as lm


def test_loves_me():
    assert lm.loves_me(0) == "NO ONE LOVES YOU!"
    assert lm.loves_me(1) == "LOVES ME!"
    assert lm.loves_me(3) == "Loves me, Loves me not, LOVES ME!"
    assert lm.loves_me(6) == "Loves me, Loves me not, Loves me, Loves me not, Loves me, LOVES ME NOT!"
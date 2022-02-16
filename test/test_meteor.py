import pybox.src.meteor.meteor as meteor

def test_will_hit():
    assert meteor.will_hit("y = 2x - 5", (0, 0)) == False
    assert meteor.will_hit("y = -4x + 6", (1, 2)) == True
    assert meteor.will_hit("y = 2x + 6", (3, 2)) == False
from .model import energy


def test_energy():
    assert energy([1,2,3]) == 8
    """Optional description for nose reporting."""
def test_energy_zeros():
    assert energy([0,0,0]) == 0
def test_energy_negative():
    assert energy([-1,-2,-3]) == 0
def test_energy_long():
    assert energy([2,2,2,2,2,2,2,2]) == 16   
    # Test something

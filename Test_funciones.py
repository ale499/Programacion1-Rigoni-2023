import pytest
from funciones import *

@pytest.mark.parametrize("a, res",[
    (24,6),
    (46,10),
    (51,6),
    (34,7),
    (98,17),
])
def test_suma_digitos(a, res):
    assert suma_digitos(a) == res

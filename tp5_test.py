import pytest
import math

from Trabajo_practico_5 import module_vector
def test_module_vector():
    assert module_vector(2,3) ==  10
@pytest.mark.parametrize(
    [(2,3,10),(3,5,16),(4,2,12)])
def test_module_vecto_multi(x,y,modulo):
    assert module_vector(x,y) ==  modulo
    
from Trabajo_practico_5 import even_or_odd
def test_numero_par():
    assert even_or_odd(2) == True
    assert even_or_odd(0) == True
    assert even_or_odd(7) == False
    assert even_or_odd(-3) == False


from Trabajo_practico_5 import funcion_radio
def test_valor_positivo():
    radio = 5
    perimetro = 2 * math.pi * radio
    area = math.pi * (radio * radio)
    assert funcion_radio(radio) == (perimetro,area)

def test_valor_cero():
    radio = 0
    perimetro = 0
    area = 0
    assert funcion_radio(radio) == (perimetro, area)

import pytest
from parcial_2 import is_mutant

# Pruebas para la función is_mutant
def test_is_mutant_vertical():
    dna = ['GCTTGA', 'CTGCAG', 'TGTATT', 'GGAAGA', 'ACTACC', 'GGCTAC']
    assert is_mutant(dna) is True

def test_is_mutant_horizontal():
    dna = ['GCTTGA', 'CTGCAG', 'TTTTGG', 'GGAAGA', 'CCCCCA', 'GGCTAC']
    assert is_mutant(dna) is True

import calculator
import pytest
def main():
   test_negative_modulo()
   test_positive_modulo()
   test_zero_modulo()
   test_str()

def test_negative_modulo():
   assert calculator.modulo(-4) == 4
   assert calculator.modulo(-10) == 10

def test_positive_modulo():
   assert calculator.modulo(5)== 5
   assert calculator.modulo(3) == 3

def test_zero_modulo():
   assert calculator.modulo(-0) == 0
def test_str():
    with pytest.raises(TypeError):
      calculator.modulo("Cat")
      



main()        

 
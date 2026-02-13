import pytest
import saying

def test_default():
  assert saying.hello() == "Hello , World"

def test_argument():
  for name in ["Gukshan " , "prakshsn" , "tarim"]:  
    assert saying.hello(name) == f"Hello , {name}"
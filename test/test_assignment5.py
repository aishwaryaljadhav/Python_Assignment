from src.assignment5.util import merge_the_tools

def test_basic_case():
    s = "AABCAAADA"
    k = 3
    
    result = merge_the_tools(s, k)
    
    assert result == ["AB", "CA", "AD"]


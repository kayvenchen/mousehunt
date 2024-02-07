from shop import buy_cheese
from io import StringIO
import sys
from unittest import mock


std_out = sys.stdout
capture_out = StringIO()
sys.stdout = capture_out

def test_function():
    expected_output = (50, (0, 1, 0))

    with mock.patch('builtins.input', side_effect=["marble 1", "back"]):
        output = buy_cheese(125)
        actual = capture_out.getvalue().strip("\n")
        expected_print = "You have 125 gold to spend.\nSuccessfully purchase 1 marble.\nYou have 75 gold to spend."
        assert actual == expected_print, "statements don't look the same"
        print("Print statements look good.")
    
    assert output == expected_output, "return values don't look too good"
    print("Return value looks good.")
    

test_function()

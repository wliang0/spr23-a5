#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
# Checks division 10 / 5 = 2
assert run("10 / 5").output == "2"
# Checks subtraction 3 - 1 = 2
assert run("3 - 1").output == "2"


###

print("All tests passed!")
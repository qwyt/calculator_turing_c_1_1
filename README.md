# Calculator Package

___
This implements a simple calculator module.

# Features

___
This package supports simple operations such as:

- Addition / Subtraction
- Multiplication / Division
- Square and nth root

# How to install it

___

```
pip install  calculator_turing_c_1_1
```

# How to use it:

___

```
# Initialize a calculator object

calc = Calculator()

# The state/current value is stored internally
# and operations have to be performed one at a time
# e.g:

calc.add(5)
# 5

calc.mult(3)
#15

# The calculator object can be reset and reused
# this set it's value to 0
calc.clear()

# The currently stored (read-only) value can be queried at any time:
print(calc.value)
```

# License:

___
[GNU AGPL](https://github.com/qwyt/calculator_turing_c_1_1/blob/master/LICENSE)

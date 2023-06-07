# Calculator Package
___
This implements a simple calculator module.

# How to install it
___
```
pip install
```

# Features
___
This package supports simple operations such as:
- Addition / Subtraction
- Multiplication / Division
- Square and nth root

# How to use:
___
```
# Initialize initialize a calculator object

calc = Calculator()

# The state/current value is stored internally
# and operations have to be performed one at a time
# e.g:

calc.add(5)
# 5

calc.mult(3)
#15

# The calculator object can be cleared and reused
calc.clear()

# The currently stored (read-only) value can be queried at any time:
print(calc.value)
```


#License
___
[GNU AGPL](https://github.com/qwyt/m1s1_turring_calc_module/blob/master/LICENSE).

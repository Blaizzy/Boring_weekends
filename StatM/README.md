
This is a simple package. You just pass in the formula as an string and the initial approximation(A and B).

Default args:

- iter = 8, 
- dec_places=4

---------------Sample Code------------------------

import Module
from statistics.helper import Bisection

s = nasm.secant("x * math.exp(x) - 1")
s()
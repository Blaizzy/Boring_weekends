# Statistics: Iterative Algorithms
This is a simple package to implements 3 key Numerical Analysis iterative algorithms:
-Bisection 
-Regula-Falsi
-Secant.

You just pass in the formula as an string and the initial approximation(A and B) and it will create an Excel sheet in your current directory.
![alt text](https://github.com/Blaizzy/Boring_weekends/edit/master/StatM/Screenshot from 2019-05-13 18-44-15.png.png)

Default args:

- iter = 8, 
- dec_places=4

---------------Sample Code------------------------

import Module
from statistics.helper import Bisection

s = nasm.secant("x * math.exp(x) - 1")
s()

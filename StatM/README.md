# Statistics: Iterative Algorithms
This is a simple package to implements 3 key Numerical Analysis iterative algorithms:
-Bisection 
-Regula-Falsi
-Secant.

You can install this package in your python env. by using **pip install StatM**.


**Disclaimer**: this github repo is just to show what's under the package. Feel free to fork it and improve upon it, but don't forget to cite this repo.

You just pass in the formula as an string and the initial approximation(A and B) and it will create an Excel sheet in your current directory.


![alt text](https://github.com/Blaizzy/Boring_weekends/blob/master/StatM/Screenshot%20from%202019-05-13%2018-44-15.png)

Default args:

- iter = 8, 
- dec_places=4

**---------------Sample Code------------------------**

<code>
import Module
from statistics.helper import Bisection

s = nasm.secant("x * math.exp(x) - 1")
s()
</code>

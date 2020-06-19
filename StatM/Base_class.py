import math
import pandas as pd
import os
from abc import ABC, abstractclassmethod


class Base(ABC):
    '''Abstract class'''

    def __init__(self, formula, iter = 8, dec_places=4):
        self.formula = lambda x: eval(formula)
        self.a = int(input('Value of A = '))
        self.b = int(input('Value of B = '))
        self.path = os.getcwd()
        self.iter = iter
        self.dec_places = dec_places
        self.i = 0
        self.df = pd.DataFrame()


    def F(self, x):
        return round(self.formula(x), self.dec_places)

    def C(self, a, b, fa, fb):
        return round((a * fb - b * fa)/(fb-fa), self.dec_places)

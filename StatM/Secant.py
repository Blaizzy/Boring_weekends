from StatM.Base_class import Base

class Secant(Base):
    '''This class implements the statistical algorithm (secant method) to the root value between a and b
    S'''

    def __init__(self,formula):
        super().__init__(formula)

    def C(self, a, b, fa, fb):
        return (a * fb - b * fa) / (fb - fa)

    def __call__(self):

        fa = self.F(self.a)
        fb = self.F(self.b)

        while self.i < self.iter:

            c = self.C(self.a, self.b, fa, fb)
            fc = self.F(c)

            temp = {'a': self.a, 'b': self.b, 'c': c, 'fa': fa, 'fb': fb, 'fc': fc}

            self.df = self.df.append(temp, ignore_index=True)

            # shift all left
            self.a, self.b = self.b, c
            fa, fb = fb, fc

            self.i += 1
        else:
            self.df.to_csv(self.path + '/secant.csv')
            print('CSV file Successfully saved to = ', self.path)

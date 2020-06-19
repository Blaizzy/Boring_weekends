from StatM.Base_class import Base

class Bisection(Base):
    '''This class implements the statistical algorithm (bisection method) to the root value between a and b
        S'''

    def __init__(self, formula):
        super().__init__(formula)

    def C(self, a, b):
        return round(((a+b)/2), self.dec_places)

    def __call__(self):



        fa = self.F(self.a)
        fb = self.F(self.b)

        while self.i < self.iter:
            c = self.C(self.a,self.b)
            fc = self.F(c)

            temp = {'a': self.a, 'b': self.b, 'c': c, 'fa': fa, 'fb': fb, 'fc': fc}
            self.df = self.df.append(temp, ignore_index=True)

            # shift left conditions
            if fc < 0:
                self.a, fa = c, fc
            else:
                self.b, fb = c, fc

            self.i += 1

        else:
            self.df.to_csv(self.path + '/Bisection.csv')
            print('CSV succefully saved to = ', self.path)

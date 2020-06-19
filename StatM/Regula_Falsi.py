from StatM.Base_class import Base

class Regula_Falsi(Base):

    def __init__(self, formula):
        super().__init__(formula)

    def __call__(self):

        fa = self.F(self.a)
        fb = self.F(self.b)

        while self.i < self.iter:

            c = self.C(self.a, self.b, fa, fb)
            fc = self.F(c)

            temp = {'a': self.a, 'b': self.b, 'c': c, 'fa': fa, 'fb': fb, 'fc': fc}
            self.df = self.df.append(temp, ignore_index=True)

            if fc < 0:
                self.a, fa = c, fc
            else:
                self.b, fb = c, fc

            self.i += 1

        else:
            self.df.to_csv(self.path +'/RegulaFalsi.csv')
            print('CSV succefully saved to = ', self.path)


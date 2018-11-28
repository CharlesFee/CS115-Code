from cs115 import *
from math import *
class QuadraticEquation:
    def __init__(self, a, b, c):
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        else:
            self.a = float(a)
            self.b = float(b)
            self.c = float(c)

    def discriminant(self):
        return ((self.b)**2)-(4*self.a*self.c)
    
    def root1(self): 
        d = self.discriminant()
        if d < 0:
            return None
        else:
            return (-self.b+sqrt(d))/(2*self.a)
        
    def root2(self):
        d = self.discriminant()
        if d < 0:
            return None
        else:
            return (-self.b-sqrt(d))/(2*self.a)

    def __str__(self):
        if self.a == 1:
            if self.b == 1:
                if self.c > 0:
                    return 'x^2 + x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return 'x^2 + x'+' = 0'
                else:
                    return 'x^2 + x - '+str(abs(self.c))
            elif self.b == -1:
                if self.c > 0:
                    return 'x^2 - x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return 'x^2 -x'+' = 0'
                else:
                    return 'x^2 - x - '+str(abs(self.c))+' = 0'
            elif self.b > 0:
                if self.c > 0:
                    return 'x^2 + '+str(self.b)+'x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return 'x^2 + '+str(self.b)+'x'+' = 0'
                else:
                    return 'x^2 + '+str(self.b)+'x - '+str(abs(self.c))+' = 0'
            elif self.b < 0:
                if self.c > 0:
                    return 'x^2 - '+str(abs(self.b))+'x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return 'x^2 - '+str(abs(self.b))+'x'+' = 0'
                else:
                    return 'x^2 - '+str(abs(self.b))+'x - '+str(abs(self.c))+' = 0'
            elif self.b == 0:
                if self.c > 0:
                    return 'x^2 + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return 'x^2'+' = 0'
                else:
                    return 'x^2 - '+str(abs(self.c))+' = 0'
                
        elif self.a == -1:
            if self.b == 1:
                if self.c > 0:
                    return '-x^2 + x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return '-x^2 + x'+' = 0'
                else:
                    return '-x^2 + x - '+str(abs(self.c))+' = 0'
            elif self.b == -1:
                if self.c > 0:
                    return '-x^2 - x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return 'x^2 -x'+' = 0'
                else:
                    return '-x^2 - x - '+str(abs(self.c))+' = 0'
            elif self.b > 0:
                if self.c > 0:
                    return '-x^2 + '+str(self.b)+'x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return '-x^2 + '+str(self.b)+'x'+' = 0'
                else:
                    return '-x^2 + '+str(self.b)+'x - '+str(abs(self.c))+' = 0'
            elif self.b < 0:
                if self.c > 0:
                    return '-x^2 - '+str(abs(self.b))+'x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return '-x^2 - '+str(abs(self.b))+'x'+' = 0'
                else:
                    return '-x^2 - '+str(abs(self.b))+'x - '+str(abs(self.c))+' = 0'
            elif self.b == 0:
                if self.c > 0:
                    return '-x^2 + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return '-x^2'+' = 0'
                else:
                    return '-x^2 - '+str(abs(self.c))+' = 0'
        elif self.b == 1:
            if self.a == 0:
                if self.c > 0:
                    return 'x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return 'x'+' = 0'
                else:
                    return 'x - '+str(abs(self.c))+' = 0'
            else:
                if self.c > 0:
                    return str(self.a)+'x^2 + x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return str(self.a)+'x^2 + x'+' = 0'
                else:
                    return str(self.a)+'x^2 + x - '+str(abs(self.c))+' = 0'
        elif self.b == -1:
            if self.a == 0:
                if self.c > 0:
                    return '-x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return '-x'+' = 0'
                else:
                    return '-x - '+str(abs(self.c))+' = 0'
            else:
                if self.c > 0:
                    return str(self.a)+'x^2 - x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return str(self.a)+'x^2 - x'+' = 0'
                else:
                    return str(self.a)+'x^2 - x - '+str(abs(self.c))+' = 0'
        else:
            if self.b > 0:
                if self.c > 0:
                    return str(self.a)+'x^2 + '+str(self.b)+'x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return str(self.a)+'x^2 + '+str(self.b)+'x'+' = 0'
                else:
                    return str(self.a)+'x^2 + '+str(self.b)+'x - '+str(abs(self.c))+' = 0'
            elif self.b == 0:
                if self.c > 0:
                    return str(self.a)+'x^2 + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return str(self.a)+'x^2'
                else:
                    return str(self.a)+'x^2 - '+str(abs(self.c))
            else:
                if self.c > 0:
                    return str(self.a)+'x^2 - '+str(abs(self.b))+'x + '+str(self.c)+' = 0'
                elif self.c == 0:
                    return str(self.a)+'x^2 - '+str(abs(self.b))+'x'+' = 0'
                else:
                    return str(self.a)+'x^2 - '+str(abs(self.b))+'x - '+str(abs(self.c))+' = 0'
                



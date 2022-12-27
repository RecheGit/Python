# Calcular area de poligonos

class Poligono():

    def __init__(self,base,altura):
        self.base=base
        self.altura=altura


class Rectangulo(Poligono):
    def area(self):
        return self.base*self.altura


class Triangulo(Poligono):
    def area(self):
        return  (self.base*self.altura)/2

trian=Triangulo(10,20)
rectan = Rectangulo(10,20)
print(trian.area())
print(rectan.area())


class Backend:

    def __init__(self):
        self.potencia = 0
        self.direccion = 1

    def actualizar_potencia(self):
        if self.potencia == 5:
            self.direccion = -1
        elif self.potencia == 0:
            self.direccion = 1

        if self.direccion == 1:
            self.potencia += 1
        else:
            self.potencia -= 1

        return self.potencia

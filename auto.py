class Coche:
    def __init__(self, marca,modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
    def acelerar(self, cantidad):
        self.velocidad += cantidad
        print(f"El {self.marca} {self.modelo} va a {self.velocidad} km/h")
    def frenar(self):
        self.velocidad=0
        print(f"El {self.marca} {self.modelo} se ha detenido ")
auto = Coche("Toyota", "Corolla")
auto.acelerar(40)
auto.frenar()

#modificar o agregar
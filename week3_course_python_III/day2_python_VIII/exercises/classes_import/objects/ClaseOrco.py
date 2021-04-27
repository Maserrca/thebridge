class Orco:
    def __init__(self, nombre, armadura, nivel, ataque, ojos=2,piernas=2, dientes=32, salud=100):
        self.ojos = 2
        self.piernas = 2
        self.dientes = 56
        self.nombre = nombre
        self.armadura = armadura
        self.ataque = ataque
        self.salud = 100
    def atacar(self, humano):
        from ClaseHumano import 
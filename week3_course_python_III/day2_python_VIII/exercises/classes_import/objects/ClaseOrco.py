
class orco:
    def __init__(self, nombre, armadura, nivel, ataque, ojos=2,piernas=2, dientes=32, salud=100):
        self.ojos = 2
        self.piernas = 2
        self.dientes = 56
        self.nombre = nombre
        self.armadura = armadura
        self.ataque = ataque
        self.salud = 100
    def atacar(self, humano):
        humano.salud = humano.salud - (self.ataque - humano.armadura)
        print(humano.salud)
        return humano.salud
    def no_vivo(self):
        if self.salud <= 0:
            return True
        else:
            return False
    def mostrar(self):
        print("Nombre", self.nombre, "|", "Armadura:", self.armadura ,"|", "Nivel:", self.nivel ,"|", "Ataque:", self.ataque,"|", "Ojos:", self.ojos,"|", "Piernas:", self.piernas, "|", "Dientes:", self.dientes, "|","Salud:", self.salud)


        
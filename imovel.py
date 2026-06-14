class Imovel:

    def __init__(self, tipo, quartos, garagem, criancas):
        self.tipo = tipo
        self.quartos = quartos
        self.garagem = garagem
        self.criancas = criancas

    def calcular_aluguel(self):

        valor = 0

        if self.tipo == "apartamento":
            valor = 700

            if self.quartos == 2:
                valor += 200

            if self.garagem:
                valor += 300

            if not self.criancas:
                valor *= 0.95

        elif self.tipo == "casa":
            valor = 900

            if self.quartos == 2:
                valor += 250

            if self.garagem:
                valor += 300

        elif self.tipo == "estudio":
            valor = 1200

        return valor
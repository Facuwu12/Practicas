class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def calcularSuma(self):
        resultado = self.num1 + self.num2
        print("El resultado es: ", resultado)
    def calcularResta(self):
        resultado = self.num1 - self.num2
        print("El resultado es: ", resultado)
    def calcularMultiplicacion(self):
        resultado = self.num1 * self.num2
        print("El resultado es: ", resultado)
    def calcularDivision(self):
        resultado = self.num1 / self.num2
        print("El resultado es: ", resultado)

calculadora = Calculadora(1, 2)
calculadora.calcularSuma()
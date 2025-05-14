"""
Jesús Pérez Hernández
Clasificación inteligente de datos

Hands-on 2: Simple Linear Regression
"""

class SimpleLinearRegression:
    def __init__(self, dataset):
        self.dataset = dataset
        self.n = len(dataset)
        self.b0 = 0
        self.b1 = 0
        self._calculate_coefficients()

    def _sum_x(self):
        return sum(item[0] for item in self.dataset)

    def _sum_y(self):
        return sum(item[1] for item in self.dataset)

    def _sum_xy(self):
        return sum(item[0] * item[1] for item in self.dataset)

    def _sum_x_squared(self):
        return sum(item[0]**2 for item in self.dataset)

    def _calculate_coefficients(self):
        sum_x = self._sum_x()
        sum_y = self._sum_y()
        sum_xy = self._sum_xy()
        sum_x_squared = self._sum_x_squared()

        denominator = (self.n * sum_x_squared) - (sum_x ** 2)
        self.b0 = ((sum_x_squared * sum_y) - (sum_x * sum_xy)) / denominator
        self.b1 = ((self.n * sum_xy) - (sum_x * sum_y)) / denominator

    def predict(self, x):
        return self.b0 + self.b1 * x

    def show_equation(self):
        print("Ecuación de regresión: y = {:.3f} + {:.3f} * x".format(self.b0, self.b1))

    def predict_and_display(self, values):
        print("\nPredicciones usando la fórmula de regresión:")
        for x in values:
            y = self.predict(x)
            print(f"Advertising={x} --> Sales={y:.3f}")


# Declaración del dataset
dataset = [
    [23, 651],
    [26, 762],
    [30, 856],
    [34, 1063],
    [43, 1190],
    [48, 1298],
    [52, 1421],
    [57, 1440],
    [58, 1518],
]

# Valores no conocidos
valores_no_conocidos = [21, 25, 45, 54, 60]

# Uso de la clase
modelo = SimpleLinearRegression(dataset)
modelo.show_equation()
modelo.predict_and_display(valores_no_conocidos)

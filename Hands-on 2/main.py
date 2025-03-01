"""
Jesús Pérez Hernández
Clasificación inteligente de datos

Hands-on 2: Simple Linear Regression
"""
## Declaración del dataset
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

## Valores no conocidos
valoresNoConocidos = [21, 25, 45, 54, 60]

## Sumatoria de X
def sumX():
    return sum(item[0] for item in dataset)

## Sumatoria de Y
def sumY():
    return sum(item[1] for item in dataset)

## Sumatoria de xy
def sumXY():
    return sum(item[0] * item[1] for item in dataset)

## Sumatoria de x^2
def sumXSquared():
    return sum(item[0]**2 for item in dataset)

n = len(dataset)
b0 = ((sumXSquared() * sumY()) - (sumX() * sumXY())) / ((n * sumXSquared()) - (sumX() ** 2))
b1 = ((n * sumXY()) - (sumX() * sumY())) / ((n * sumXSquared()) - (sumX()**2))

print("Ecuacion de regresion = {:.3f} + {:.3f} * x1\n".format(b0, b1))

print("Predicciones usando la fórmula de regresión:")

for i in valoresNoConocidos:
    valorCalculado = b0 + (b1 * i)
    print("Advertising={} --> Sales={:.3f}".format(i, valorCalculado))
from scipy.optimize import linprog

obj = [-20, -12, -40, -25]

lhs_ineq = [[1, 1, 1, 1],  # Manpower
        [3, 2, 1, 0],  # Material A
        [0, 1, 2, 3]]  # Material B

rhs_ineq = [50,  # Manpower
            100,  # Material A
            90]  # Material B

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="revised simplex")

print(opt)

# la salida con : es la igualdad de la restriccion residual
# la salida fun: es el valor optimo de la funcion objetivo
# la salida message: es el status de la funcion objetivo
# la salida nit: es el numero de iteraciones necesarias para terminar el calculo
# la salida slack: son los valores de las variables de holgura o las diferencias entre los valores de los lados izquierdo y derecho de las restricciones.
# la salida status: su salida son valores entre 0 y 4, si es 0 es porque entrego la solucion optima
# la salida success: es un boolean que muestra si la solucion fue encontrada.
# la salida x: es una matriz NumPy que contiene los valores óptimos de las variables de decisión.
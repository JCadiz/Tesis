from scipy.optimize import linprog

obj = [-1, -2]
#      ─┬  ─┬
#       │   └┤ Coefficient for y
#       └────┤ Coefficient for x

#Restricciones
lhs_ineq = [[ 2,  1],  # Red constraint left side
             [-4,  5],  # Blue constraint left side
             [ 1, -2]]  # Yellow constraint left side

rhs_ineq = [20,  # Red constraint right side
             10,  # Blue constraint right side
              2]  # Yellow constraint right side

#Restriccion con igualdad
lhs_eq = [[-1, 5]]  # Green constraint left side
rhs_eq = [15]       # Green constraint right side

#Restricciones para que las variables no sean menores a zero
bnd = [(0, float("inf")),  # Bounds of x
        (0, float("inf"))]  # Bounds of y

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, A_eq=lhs_eq, b_eq=rhs_eq, bounds=bnd, method="revised simplex")

print(opt)

# la salida con : es la igualdad de la restriccion residual
# la salida fun: es el valor optimo de la funcion objetivo
# la salida message: es el status de la funcion objetivo
# la salida nit: es el numero de iteraciones necesarias para terminar el calculo
# la salida slack: son los valores de las variables de holgura o las diferencias entre los valores de los lados izquierdo y derecho de las restricciones.
# la salida status: su salida son valores entre 0 y 4, si es 0 es porque entrego la solucion optima
# la salida success: es un boolean que muestra si la solucion fue encontrada.
# la salida x: es una matriz NumPy que contiene los valores óptimos de las variables de decisión.
# primero, se importa PuLP
import pulp

# luego, se realiza la declaración inicial del problema

modelo1 = pulp.LpProblem("Modelo1_MinSum",pulp.LpMinimize)

# definimos las variables 

x11 = pulp.LpVariable( name="x11" , lowBound=0 )
x12 = pulp.LpVariable( name="x12" , lowBound=0 )
x13 = pulp.LpVariable( name="x13" , lowBound=0 )
x14 = pulp.LpVariable( name="x14" , lowBound=0 )
x15 = pulp.LpVariable( name="x15" , lowBound=0 )
x21 = pulp.LpVariable( name="x21" , lowBound=0 )
x22 = pulp.LpVariable( name="x22" , lowBound=0 )
x23 = pulp.LpVariable( name="x23" , lowBound=0 )
x24 = pulp.LpVariable( name="x24" , lowBound=0 )
x25 = pulp.LpVariable( name="x25" , lowBound=0 )
x31 = pulp.LpVariable( name="x31" , lowBound=0 )
x32 = pulp.LpVariable( name="x32" , lowBound=0 )
x33 = pulp.LpVariable( name="x33" , lowBound=0 )
x34 = pulp.LpVariable( name="x34" , lowBound=0 )
x35 = pulp.LpVariable( name="x35" , lowBound=0 )
x41 = pulp.LpVariable( name="x41" , lowBound=0 )
x42 = pulp.LpVariable( name="x42" , lowBound=0 )
x43 = pulp.LpVariable( name="x43" , lowBound=0 )
x44 = pulp.LpVariable( name="x44" , lowBound=0 )
x45 = pulp.LpVariable( name="x45" , lowBound=0 )
x51 = pulp.LpVariable( name="x51" , lowBound=0 )
x52 = pulp.LpVariable( name="x52" , lowBound=0 )
x53 = pulp.LpVariable( name="x53" , lowBound=0 )
x54 = pulp.LpVariable( name="x54" , lowBound=0 )
x55 = pulp.LpVariable( name="x55" , lowBound=0 )

# Se define la funcion objetivo

modelo1 += 10* x11 +75* x12 + 85 * x13 + 65 * x14 + 14 * x15 + 90 * x21 + 50 * x22 + 20 * x23 + 78 * x24 + 36 * x25 + 60 * x31 + 35 * x32 + 12 * x33 + 32 * x34 + 85 * x35 + 15 * x41 + 96 * x42 + 70 * x43 + 25 * x44 + 14 * x45 + 80 * x51 + 14 * x52 + 55 * x53 + 45 * x54 + 25 * x55

# Se definen restricciones del problema

modelo1 += (x11 + x21 + x31 + x41 + x51 == 1,"Restriccion1")
modelo1 += (x12 + x22 + x32 + x42 + x52 == 1,"Restriccion2")
modelo1 += (x13 + x23 + x33 + x43 + x53 == 1,"Restriccion3")
modelo1 += (x14 + x24 + x34 + x44 + x54 == 1,"Restriccion4")
modelo1 += (x15 + x25 + x35 + x45 + x55 == 1,"Restriccion5")
modelo1 += (x11 + x12 + x13 + x14 + x15 == 1,"Restriccion6")
modelo1 += (x21 + x22 + x23 + x24 + x25 == 1,"Restriccion7")
modelo1 += (x31 + x32 + x33 + x34 + x35 == 1,"Restriccion8")
modelo1 += (x41 + x42 + x43 + x44 + x45 == 1,"Restriccion9")
modelo1 += (x51 + x52 + x53 + x54 + x55 == 1,"Restriccion10")

# Se resuelve utilizando el solucionador 

solution = modelo1.solve()

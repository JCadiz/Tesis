# primero, se importa PuLP
import pulp

# luego, se realiza la declaración inicial del problema

modelo2 = pulp.LpProblem("modelo2 MinMax",pulp.LpMinimize)

# definimos las variables 

x11 = pulp.LpVariable( name="x11" , lowBound = 0 )
x12 = pulp.LpVariable( name="x12" , lowBound = 0 )
x13 = pulp.LpVariable( name="x13" , lowBound = 0 )
x14 = pulp.LpVariable( name="x14" , lowBound = 0 )
x15 = pulp.LpVariable( name="x15" , lowBound = 0 )
x21 = pulp.LpVariable( name="x21" , lowBound = 0 )
x22 = pulp.LpVariable( name="x22" , lowBound = 0 )
x23 = pulp.LpVariable( name="x23" , lowBound = 0 )
x24 = pulp.LpVariable( name="x24" , lowBound = 0 )
x25 = pulp.LpVariable( name="x25" , lowBound = 0 )
x31 = pulp.LpVariable( name="x31" , lowBound = 0 )
x32 = pulp.LpVariable( name="x32" , lowBound = 0 )
x33 = pulp.LpVariable( name="x33" , lowBound = 0 )
x34 = pulp.LpVariable( name="x34" , lowBound = 0 )
x35 = pulp.LpVariable( name="x35" , lowBound = 0 )
x41 = pulp.LpVariable( name="x41" , lowBound = 0 )
x42 = pulp.LpVariable( name="x42" , lowBound = 0 )
x43 = pulp.LpVariable( name="x43" , lowBound = 0 )
x44 = pulp.LpVariable( name="x44" , lowBound = 0 )
x45 = pulp.LpVariable( name="x45" , lowBound = 0 )
x51 = pulp.LpVariable( name="x51" , lowBound = 0 )
x52 = pulp.LpVariable( name="x52" , lowBound = 0 )
x53 = pulp.LpVariable( name="x53" , lowBound = 0 )
x54 = pulp.LpVariable( name="x54" , lowBound = 0 )
x55 = pulp.LpVariable( name="x55" , lowBound = 0 )
z = pulp.LpVariable( name = "z", lowBound = 0 )

# Se define la funcion objetivo

modelo2 += z

# Se definen restricciones del problema

modelo2 += (x11 + x21 + x31 + x41 + x51 == 1,"Restriccion1")
modelo2 += (x12 + x22 + x32 + x42 + x52 == 1,"Restriccion2")
modelo2 += (x13 + x23 + x33 + x43 + x53 == 1,"Restriccion3")
modelo2 += (x14 + x24 + x34 + x44 + x54 == 1,"Restriccion4")
modelo2 += (x15 + x25 + x35 + x45 + x55 == 1,"Restriccion5")
modelo2 += (x11 + x12 + x13 + x14 + x15 == 1,"Restriccion6")
modelo2 += (x21 + x22 + x23 + x24 + x25 == 1,"Restriccion7")
modelo2 += (x31 + x32 + x33 + x34 + x35 == 1,"Restriccion8")
modelo2 += (x41 + x42 + x43 + x44 + x45 == 1,"Restriccion9")
modelo2 += (x51 + x52 + x53 + x54 + x55 == 1,"Restriccion10")
modelo2 += (z >= 10 * x11 , "Restriccion 11")
modelo2 += (z >= 75 * x12 , "Restriccion 12")
modelo2 += (z >= 85 * x13 , "Restriccion 13")
modelo2 += (z >= 65 * x14 , "Restriccion 14")
modelo2 += (z >= 14 * x15 , "Restriccion 15")
modelo2 += (z >= 90 * x21 , "Restriccion 16")
modelo2 += (z >= 50 * x22 , "Restriccion 17")
modelo2 += (z >= 20 * x23 , "Restriccion 18")
modelo2 += (z >= 78 * x24 , "Restriccion 19")
modelo2 += (z >= 36 * x25 , "Restriccion 20")
modelo2 += (z >= 60 * x31 , "Restriccion 21")
modelo2 += (z >= 35 * x32 , "Restriccion 22")
modelo2 += (z >= 12 * x33 , "Restriccion 23")
modelo2 += (z >= 32 * x34 , "Restriccion 24")
modelo2 += (z >= 85 * x35 , "Restriccion 25")
modelo2 += (z >= 15 * x41 , "Restriccion 26")
modelo2 += (z >= 96 * x42 , "Restriccion 27")
modelo2 += (z >= 70 * x43 , "Restriccion 28")
modelo2 += (z >= 25 * x44 , "Restriccion 29")
modelo2 += (z >= 14 * x45 , "Restriccion 30")
modelo2 += (z >= 80 * x51 , "Restriccion 31")
modelo2 += (z >= 14 * x52 , "Restriccion 32")
modelo2 += (z >= 55 * x53 , "Restriccion 33")
modelo2 += (z >= 45 * x54 , "Restriccion 34")
modelo2 += (z >= 25 * x55 , "Restriccion 35")



# Se resuelve utilizando el solucionador 

solution = modelo2.solve()

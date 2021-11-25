# Elaborado por Pablo Cruz Morales y Xavier Suástegui Rodríguez.
# Julio de 2021.

# Esta función despliega en pantalla la carátula del programa.
def interfaz():
    print("\n                             MÉTODO DE GAUSS-SEIDEL\n")
    print("""La operaciones válidas son las siguientes: +, -, *, /, **. Este método numérico únicamente resuelve sistemas de ecuaciones
lineales compatibles determinados. Se te solicitará que escribas el orden de la matriz A y los elementos de esta; también  el vector b,
que contendrá los resultados de las ecuaciones del sistema. Si el sistema de ecuaciones fuese el siguiente:
                x+10y+9z=7
                2x-7y-10z=-17
                10x+2y+6z=28
el orden de la matriz sería n = 3, los componentes de la matriz A serían los siguientes:
Primer renglón = 1, 0, 10
Segundo renglón = 2, -7, -17
Tercer renglón = 10, 2, 0
y los términos independientes (vector b) serían 7, -17 y 28
NOTA: Los elementos de la matriz A deben de ingresarse por el usuario de manera tal que cumplan la condición necesaria del método de Gauss-Siedel.\n""")

# Este método lee y almacena los coeficientes del sistema de ecuaciones.
def leer_matriz():
    a = []
    b = []
    renglones = []
    n = int(input("Orden de la matriz: "))
    tolerancia = float(input("Tolerancia (en porcentaje): "))
    for i in range(n): # Se le pide al usuario, uno por uno, los coeficientes del sistema de ecuaciones.
        for j in range(n):
            coeficientes = float(input("Coeficiente a[{}][{}]: ".format(i+1,j+1)))
            renglones.append(coeficientes)
        a.append(renglones)
        renglones=[]
    for i in range(n):
        resultados = float(input("Término independiente b[{}]: ".format(i+1)))
        b.append(resultados)

    return a, b, n, tolerancia

# Esta función resuleve el sistema de ecuaciones.
def resuelve_sistema(a,b,n,tolerancia):
    k = 0 # Índice que ayuda a ubicar la iteración en la que nos encontramos.
    x = [] # Matriz con resultados de cada iteración. Los renglones representan las variables y las columnas, las iteraciones.
    e_abs = []
    e=0
    for i in range(n):
        x.append([b[i]/a[i][i]]) # Se crea el primer vector con los valores de las variables.
        e_abs.append([b[i]/a[i][i]])
    while e<n:
        for i in range(n): # Se avanza en cada renglón de la matriz x.
            x_aux=b[i]
            for j in range(n): # Se avanza en cada columna de la matriz x.
                if i == j:
                    continue
                try:
                    x_aux=x_aux-a[i][j]*x[j][k+1] # Ecuaciones de recurrencia.
                except IndexError:
                    x_aux=x_aux-a[i][j]*x[j][k]  
            x[i].append(x_aux/a[i][i]) # Se agrega a la matrix x el vector con los valores de las variables.
            e_abs[i].append(abs(x[i][-1]-x[i][-2])/x[i][-1]*100)
        for error in e_abs:
            if(error[-1]>tolerancia):
                e=0
                continue
            e=1+e
        k += 1 # Aumenta el índice de la iteración.
    return x # Se devuelven los valores más actualizados de las variables.

# Esta función imprime los valores de las variables del sistema.
def imprime_variables(n, x):
    print("\nResultados:")
    for i in range(n):
        print("x%d = %4.5f" % (i+1, x[i][-1]))
    
# Programa principal.
if __name__ == '__main__':
    interfaz()
    a, b, n, tolerancia = leer_matriz()
    x = resuelve_sistema(a,b,n,tolerancia)
    imprime_variables(n, x)

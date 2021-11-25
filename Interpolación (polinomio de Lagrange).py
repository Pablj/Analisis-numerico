# Elaborado por Pablo Cruz Morales y Xavier Suástegui Rodríguez.
# Julio de 2021.

import pandas as pd

# Esta función despliega en pantalla la carátula del programa.
def interfaz():
    print("\n           INTERPOLACIÓN CON INCREMENTOS CONSTANTES O VARIABLES: POLINOMIO DE LAGRANGE\n")
    print("""Este programa utiliza Excel como herramienta, lo cual significa dos cosas: puedes crear una tabla en excel con una columna 'x' y otra
columna 'y' y definir tu propia función tabular; o bien, puedes crear tu archivo desde Pyhton (las indicaciones correspondientes se te darán al
seleccionar esa opción).
    Ahora bien, se te solicitará que escojas entre tres opciones: 'Cargar archivo', 'Crear archivo' o 'Salir'. Si seleccionas la primer opción,
tendrás que escribir el nombre de tu archivo con todo y su extensión, la cual debe ser FORZOZAMENTE 'csv', por ejemplo, 'archivo.csv'. Finalmente,
tienes que elegir entre calcular una 'x' o una 'y'.
NOTA: Es importante que, si decides crear tu propio archivo en Excel, lo guardes en el mismo directorio en el que tengas este programa.""")

# Este método importa la tabla de Excel con extensión 'csv'.
def cargar_tabla():
    while True:
        archivo = input("\nNombre del archivo: ")
        try:
            tabla = pd.read_csv(archivo)
            return tabla
        except FileNotFoundError:
            print("Archivo no encontrado.")

# Esta operación crea el polinomio de Lagrange para calcular una 'y' dada una 'x'.
def lagrange(tabla, x_ev):
    # La variable 'x_ev' es el valor de 'x' para el cual el usuario quiere calcular una 'y'.
    num = 1 # Numerador de cada término del polinomio de Lagrange.
    den = 1 # Denominador de cada término del polinomio de Lagrange.
    polinomio = 0
    for y in range(len(tabla['x'])): 
        for xi in tabla['x']:
            if tabla['x'][y] - xi == 0:
                continue
            num = (x_ev-xi)*num
            den = (tabla['x'][y]-xi)*den
        polinomio = (num/den)*tabla['y'][y] + polinomio
        num = 1
        den = 1
    print("y = %4.5f" % polinomio)

# Esta función crea el polinomio de Lagrange para calcular una 'x' dada una 'y'.
def lagrange_inversa(tabla,x_ev):
    num = 1
    den = 1
    polinomio = 0
    for y in range(len(tabla['x'])):
        for xi in tabla['y']:
            if tabla['y'][y] - xi == 0: # 
                continue
            num = (x_ev - xi)*num
            den = (tabla['y'][y] - xi)*den
        polinomio = (num/den)*tabla['x'][y] + polinomio
        num = 1
        den = 1   
    print("x = %4.5f" % polinomio)

# Esta función desliega el menú en la pantalla.
def menu():
    print("\n¿Qué deseas hacer?")
    print("a) Cargar archivo.\nb) Crear archivo.\nc) Salir.")
    opcion = input("Opción: ")
    if opcion == 'a':
        tabla = cargar_tabla()
        while True:
            print("\n¿Qué quieres calcular?")
            print ("a) Calcular una 'y'.\nb) Calcular una 'x'.")
            opcion2 = input("Opción: ")
            if opcion2 == 'a':
                x = float(input("Cuando 'x' es igual a: "))
                lagrange(tabla, x)
            elif opcion2 == 'b':
                y = float(input("Cuando 'y' es igual a: "))
                lagrange_inversa(tabla, y)
            else:
                print("Valor fuera de rango.")
            c = input("¿Calcular otro valor? (s/n): ")
            if c == 'n':
                break
    elif opcion == 'c':
        return False
        
if __name__ == '__main__':
    interfaz()
    respuesta = True
    while respuesta != False:
        respuesta = menu()
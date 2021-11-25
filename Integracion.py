import pandas as pd
from pandas.core.frame import DataFrame

def cargar_tabla():
    while True:
        archivo=input("Nombre del archivo. example.csv\n=")
        try:
            tabla=pd.read_csv(archivo)
            return tabla
            # nuevaT=pd.DataFrame(tabla)
            # nuevaT.to_csv(archivo)
            print(tabla)
        except(FileNotFoundError):
            print("Archivo no encontrado")

def integral(tabla,intervalo=[1,9],formula):
    
def lagrange_inversa(tabla,x_ev):
    den=1
    nom=1
    polinomio=0
    for y in range(len(tabla['x'])):
        for xs in tabla['y']:
            if tabla['y'][y]-xs==0:
                continue
            nom=(x_ev-xs)*nom
            den=(tabla['y'][y]-xs)*den
        polinomio=nom/den*tabla['x'][y]+polinomio
        nom=1
        den=1   
    print(polinomio)
def menu():
    opcion=input("a)Cargar archivo\nb)Crear archivo\nc)Salir\n=")
    if opcion=='a':
        tabla=cargar_tabla()
        while True:
            a=input("Calcular y\nCalcular x\n=")
            if a=='y':
                x=float(input("Calcular 'y' cuando x:"))
                lagrange(tabla,x)

            elif a=='x':
                y=float(input("Calcular 'x' cuando y:"))
                lagrange_inversa(tabla,y)
            else:
                print("Valor fuera de rango")
            c=input("Quieres continuar?(s/n)")
            if c=='n':
                break
            

        
    elif opcion=='c':
        return 1
if __name__ == '__main__':
    ban=0
    while ban!=1:
        ban=menu()
    



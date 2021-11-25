
def cargar_tabla():
    x=[]
    y=[]
    tabla={}
    with open("final.csv","r") as archivo:
        for linea in archivo:
            linea=linea[:-1]
            linea=linea.split(',')
            try:   
                x.append(int(linea[0])) 
                y.append(float(linea[1])) 
            except ValueError:
                x.append(linea[0]) 
                y.append(linea[1]) 


    tabla[x[0]]=(x[1:])
    tabla[y[0]]=(y[1:])
    return tabla
    

def integral(tabla,intervalo,v=False):
    sum_par=0
    sum_impar=0
    h=1
    
    if v==False:
        indice_a=tabla['x'].index(intervalo[0])#Se corta las listas segun el intervalo del usuario
        indice_b=tabla['x'].index(intervalo[1])
        tabla['x']=tabla['x'][indice_a:indice_b+1]
        tabla['y']=tabla['y'][indice_a:indice_b+1]
    else:
        tabla['x']=tabla['x'][intervalo[0]:intervalo[1]]
        tabla['y']=tabla['y'][intervalo[0]:intervalo[1]]
       
    
    if (len(tabla['x'])-1)%2==0:
        for i in range(len(tabla['x'])):
            if tabla['x'][i]==tabla['x'][0] or tabla['x'][i]==tabla['x'][-1]  :
                continue
            if i%2==0:
                sum_par=tabla['y'][i]+sum_par
            else:
                sum_impar=tabla['y'][i]+sum_impar
        i_fx=(h/3)*(tabla['y'][0]+tabla['y'][-1]+4*sum_impar+2*sum_par)
        
        return i_fx
    elif (len(tabla['x'])-1)%3==0:
        for i in range(len(tabla['x'])):
            if tabla['x'][i]==tabla['x'][0] or tabla['x'][i]==tabla['x'][-1]  :#filtra y_0 y y_n
                continue
            if i%3==0:
                sum_par=tabla['y'][i]+sum_par
            else:
                sum_impar=tabla['y'][i]+sum_impar
        i_fx=(3*h/8)*(tabla['y'][0]+tabla['y'][-1]+2*sum_par+3*sum_impar)
        
        print("3/8",i_fx)
        return i_fx
    elif (len(tabla['x'])==2):
        i_fx=(h/2)*(tabla['y'][0]+tabla['y'][-1])
        return i_fx   
    else:
        a=None
        b=3*int((len(tabla['x'])-1)/3)+1
        print("entre")
        i_fx=integral(tabla.copy(),(a,b),True)+integral(tabla,(b-1,a),True)
        return i_fx    
def agregar_resultado(integral_definida,tabla):
    tabla['Integral_definida']=integral_definida
    with open("puntos.csv","w") as archivo:
        archivo.write('x,y,Integral definida\n')
        for  x in range(len(tabla['x'])):
            if x==0:
                archivo.write(str(tabla['x'][x])+','+str(tabla['y'][x])+','+str(tabla['Integral_definida'])+'\n')
            archivo.write(str(tabla['x'][x])+','+str(tabla['y'][x])+'\n')

if __name__ == '__main__':
    tabla=cargar_tabla()
    intervalo=(1,5)
    integral_definida=round(integral(tabla,intervalo),3)
    print(integral_definida)
    agregar_resultado(integral_definida,tabla)

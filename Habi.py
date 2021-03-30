import pandas as pd
import numpy as np 

filename = 'train_data.csv'
data = pd.read_csv(filename, header=0).fillna(0)
Y = data.get(['tipoinmueble','area','estrato','tiempodeconstruido','banos','latitud','longitud','valorventa'])
Y = np.array(Y)

filename1 = 'test_data.csv'
data1 = pd.read_csv(filename1, header=0).fillna(0)
J = data1.get(['tipoinmueble','area','estrato','tiempodeconstruido','banos','latitud','longitud','valorventa'])
X = np.array(J)

#Datos entrantes en este caso datos de la primera fila de archivo test 
#Se puede generar a través de la petición de datos o a través del cambio de la fila del archivo test
Dato=X[0] 

Final = list()
final = list()

tamaño = (X.shape[1] - 1)
for n in range (0,tamaño):
    x=Dato[n]
    if n == 0:
        for i in range(0,Y.shape[0]):
            Base = Y[i][n]
            if type(x) == float or type(x) == int:
                if x < 0 and Base < 0:
                    x = x*(-1)
                    Base = Base*(-1)
                if Base > (x-1) and Base < (x+1):
                    Relacion = list()
                    a=0
                    for m in range (0, X.shape[1]):
                        Relacion.insert(a, Y[i][m])
                        a = a+1
                    Final.append(Relacion)
            else:
                if Base == x:
                    Relacion = list()
                    a=0
                    for m in range (0,X.shape[1]):
                        Relacion.insert(a, Y[i][m])
                        a = a+1
                    Final.append(Relacion)
    else:
        if len(Final)>15:
            final = Final
            Final = list()
            for i in range (0, len(final)):
                Base = final[i][n]
                if type(x) == float or type(x) == int:
                    if x < 0 and Base < 0:
                        x = x*(-1)
                        Base = Base*(-1)
                    if Base > (x-1) and Base < (x+1):
                        Relacion = list()
                        a = 0
                        for m in range (0, X.shape[1]):
                            Relacion.insert(a, final[i][m])
                            a = a+1
                        Final.append(Relacion)
                else:
                    if Base == x:
                        Relacion = list()
                        a=0
                        for m in range(0, X.shape[1]):
                            Relacion.insert(a, final[i][m])
                            a = a+1
                        Final.append(Relacion)
        else:
            break
Titulos = (['tipoinmueble','area','estrato','tiempodeconstruido','banos','latitud','longitud','valorventa'])
datos = pd.DataFrame(Final, columns=Titulos)
Venta = datos.get(['valorventa'])
Area = datos.get(['area'])
Area = np.array(Area)
Venta = np.array(Venta)
Valor1 = 0
for n in range (0, Venta.shape[0]):
    Valor = Venta[n]
    Valor1 = Valor + Valor1
Valor = int(Valor1/Venta.shape[0])
MetroCua = int(Valor/Area[0])
ValorMed = int(max(Venta)-min(Venta))
ValorR = Dato[7]
Error = int(Valor - ValorR)
Error = abs(Error)/ValorR
Error = round(Error*100,2)
print(f"El valor calculado del costo del inmueble es: {Valor} ")
print(f"El valor calculado del metro cuadrado es: {MetroCua}")
print(f"El valor medio calculado es: {ValorMed}")
print(f"El error calculado del costo del inmueble es: {Error}%")

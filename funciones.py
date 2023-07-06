import numpy as np
import msvcrt
import datetime
import os

fecha=datetime.datetime.now()

concierto=np.zeros((10,10),int)
lista_filas=[1,2,3,4,5,6,7,8,9,10]
lista_columnas=[1,2,3,4,5,6,7,8,9,10]

lista_ruts=[]
lista_nombres=[]
lista_apellidos=[]
lista_usuario_filas=[]
lista_usuario_columna=[]

acumulador_platinum=0
acumulador_gold=0
acumulador_silver=0

platinum=120000
gold=80000
silver=50000


def menu():
    os.system('cls')
    print("""
    MENÚ CONCIERTO

    1. COMPRAR ENTRADAS
    2. MOSTRAR UBICACIONES DISPONIBLES
    3. VER LISTADO DE ASITENTES 
    4. MOSTRAR GANANCIAS TOTALES
    5. SALIR
    """)

def opcion():
    while True:
        try:
            opc = int(input("INGRESE OPCIÓN: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERROR!, OPCION INVÁLIDA, DEBE ESTAR ENTRE: (1,2,3,4,5)")
        except:
            print("ERROR!, SU OPCIÓN DEBE SER NÚMERO ENTERO!")

def validar_rut():
    while True:
        try:
            rut=int(input("INGRESE RUT (SIN GUIÓN, SIN PUNTOS NI DÍGITO VERIFICADOR): "))
            if len(str(rut))>=7 and len(str(rut))<=8:
                return rut
            else:
                print("ERROR!, SU RUT DEBE ESTAR ENTRE 7 Y 8 DÍGITOS!")
        except:
            print("ERROR!, SU RUT DEBE ESTÁR ESCRÍTO EN NÚMEROS ENTEROS!")

def validar_nombre():
    while True:
        nom = input("INGRESE SU NOMBRE: ")
        if len(nom.strip()) >= 3 and nom.isalpha:
            return nom
        else:
            print("ERROR!, SU NOMBRE DEBE ESTÁR ESCRITO EN LETRAS Y DEBE SER IGUAL O MAYOR DE 3 LETRAS!")

def validar_apellido():
    while True:
        apell = input("INGRESE SU APELLIDO: ")
        if len(apell.strip()) >= 3 and apell.isalpha:
            return apell
        else:
            print("ERROR!, SU APELLIDO DEBE ESTÁR ESCRITO EN LETRAS Y DEBE SER IGUAL O MAYOR DE 3 LETRAS!")

def ver_concierto():
    print("VER ASIENTOS CONCIERTO")
    print()
    print("COLUMNA:   1 2 3 4 5 6 7 8 9 10")
    for x in range(10): 
        print(f"FILA:{x+1} -->",end=" ")
        for y in range(10):
            print(concierto[x][y],end=" ")
        print()
    print()
    print("PRESIONE CUALQUIER TECLA PARA CONTINUAR")
    msvcrt.getch()

def validar_fila():
    while True:
        try:
            fila=int(input("INGRESE FILA: "))
            if fila in lista_filas:
                return fila
            else:
                print("ERROR!, FILA INVÁLIDA, DEBE ESTAR ENTRE: (1,2,3,4,5,6,7,8,9,10)")
        except:
            print("ERROR!, SU FILA DEBE SER NÚMERO ENTERO!")

def validar_columna():
    while True:
        try:
            column=int(input("INGRESE COLUMNA: "))
            if column in lista_columnas:
                return column
            else:
                print("ERROR!, COLUMNA INVÁLIDA, DEBE ESTAR ENTRE: (1,2,3,4,5,6,7,8,9,10)")
        except:
            print("ERROR!, SU COLUMNA DEBE SER NÚMERO ENTERO!")

def comprar_entrada():
    if not 0 in concierto:
        print("ERROR, ASIENTOS DEL CONCIERTO OCUPADOS COMPLETAMENTE!")
        print()
        print("PRESIONE CUALQUIER TECLA PARA CONTINUAR")
        msvcrt.getch()
        return

    rut=validar_rut()
    nom=validar_nombre()
    apell=validar_apellido()
    ver_concierto()
    while True:
        fila=validar_fila()
        column=validar_columna()
        if concierto[fila-1][column-1]==0:
            concierto[fila-1][column-1]=1
            lista_usuario_filas.append(fila)
            lista_usuario_columna.append(column)
            break
        else:
            print("ERROR!, EL ASIENTO ELEGIDO YA ESTÁ OCUPADO, ELIGA OTRO!")
    if fila >=1 and fila <=20:
        acumulador_platinum={acumulador_platinum}+1
    elif fila >=21 and fila <=50:
        acumulador_gold={acumulador_gold}+1
    else:
        acumulador_silver={acumulador_silver}+1
    lista_ruts.append(rut)
    lista_nombres.append(nom)
    lista_apellidos.append(apell)
    print("REGISTRO EXITOSO!")
    print()
    print("PRESIONE CUALQUIER TECLA PARA CONTINUAR")
    msvcrt.getch()

def ver_ruts():
    lista_ruts.sort()
    print(lista_ruts)
    print()
    print("PRESIONE CUALQUIER TECLA PARA CONTINUAR")
    msvcrt.getch()

def ganancias_totales():
    pla=comprar_entrada(acumulador_platinum)
   
    print("GANANCIAS TOTALES")
    print()
    print(f"""
         TIPO DE ENTRADA  | CANTIDAD | TOTAL
    PLATINUM = $120000    | {acumulador_platinum}        | ${platinum*acumulador_platinum}
    GOLD     = $80000     | {acumulador_gold}        | ${gold*acumulador_gold}
    SILVER   = $50000     | {acumulador_silver}        | ${silver*acumulador_silver}
    """)
    print()
    print("PRESIONE CUALQUIER TECLA PARA CONTINUAR")
    msvcrt.getch()


def salida():
    nom=validar_nombre()
    apell=validar_apellido()
    print(f"""
    SALIENDO DEL SISTEMA

    HASTA PRONTO {nom} {apell}!  /////  FECHA: {fecha}
          
          """)



import funciones as fn

print("BIENVENIDO A CREATIVOS.CL!")
while True:
    fn.menu()
    opc=fn.opcion()
    if opc == 1:
        fn.comprar_entrada()
    elif opc == 2:
        fn.ver_concierto()
    elif opc == 3:
        fn.ver_ruts()
    elif opc == 4:
        fn.ganancias_totales()
    else:
        fn.salida()
        break

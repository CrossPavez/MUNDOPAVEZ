import os
opcion = ""
precioDescuento = False


#Precio Descuento
descuento = 0.90

#Contador
cont = 0
cont2 = 0
cont3 = 0
cont4 = 0

#Total Recaudado
recaudado = 0

while True:
    print(" Bienvenido a la Heladeria Fan´s Levi live ")
    edad = int(input("Ingrese su edad: "))
    

    if edad < 18:
        precioDescuento = True
        print("Tiene un descuento de un 10%")
        break


    elif edad > 18 and edad <60:
        precioDescuento = False
        print("No tiene descuento")
        break
 
    else:
        precioDescuento = True
        print("Tiene un descuento de un 10%")
        break





while opcion != "5":
    os.system("Pause")
    print("** Heladeria Fan´s Levi live")
    print("1.- Cestrellan $500 ")
    print("2.- Champs $4.000 ")
    print("3.- Meganium $2.500 ")
    print("4.- Donkie $2.000 ")
    print("5.- Salir")
    opcion = input("Ingrese una opción:")

    if opcion not in ("1","2","3","4","5"):
        print("La opción no es válida")

    if opcion == "1":
        precio = 500
        if precioDescuento:
            precioFinal = precio * descuento

        elif precioDescuento:
            precioFinal = precio * descuento

        else:
            precioFinal = precio

        cont+=1
        recaudado += precioFinal
      
    if opcion == "2":
        precio = 4000
        if precioDescuento:
            precioFinal = precio * descuento

        elif precioDescuento:
            precioFinal = precio * descuento

        else:
            precioFinal = precio

        cont2+=1
        recaudado += precioFinal  

    if opcion == "3":
        precio = 2500
        if precioDescuento:
            precioFinal = precio * descuento

        elif precioDescuento:
            precioFinal = precio * descuento

        else:
            precioFinal = precio

        cont3+=1
        recaudado += precioFinal


    if opcion == "4":
        precio = 2000
        if precioDescuento:
            precioFinal = precio * descuento

        elif precioDescuento:
            precioFinal = precio * descuento

        else:
            precioFinal = precio

        cont4+=1
        recaudado += precioFinal




    elif opcion == "5":
        os.system("cls")
        print("Heladeria Fan´s Levi live: ")
        print("Reporte de productos vendidos")
        print("Cestrellant: ", cont)
        print("Champs: ", cont2)
        print("Meganum: ", cont3)
        print("Donkie: ", cont4)
        print("Total ventas: ", recaudado)


## Ejercicio 1

while True:
    NombreCliente = input("Ingrese el nombre del cliente: ")

    if NombreCliente == "":
        print("Error: El nombre no puede estar vacio")

    elif not NombreCliente.isalpha():
        print("Error: El nombre solo puede contener letras")

    else:
        break

while True:
    CantidadProductosC = input("Ingrese la cantidad de producto: ")

    if CantidadProductosC == "":
       print("Error: La cantidad no puede estar vacio")

    elif not CantidadProductosC.isdigit():
        print("Error: solo se admiten numeros enteros positivos")

    else:
        CantidadProductosC = int(CantidadProductosC)

        if CantidadProductosC > 0:
            break

        else:
            print("Error: La cantidad tiene que ser mayor a cero")

TotalSinDescuento = 0
TotalConDescuento = 0

for i in range(CantidadProductosC):
    while True:
        PrecioProducto = input(f"Ingrese el precio del producto {i + 1}: ")

        if PrecioProducto == "":
            print("Error: El precio no puede estar vacio")

        elif not PrecioProducto.isdigit():
            print("Error: Solo se admiten numeros enteros positivos")

        else:
            PrecioProducto = int(PrecioProducto)

            if PrecioProducto > 0:
                break

            else:
                print("Error: El precio tiene que ser mayor a cero")

    TotalSinDescuento = TotalSinDescuento + PrecioProducto      

    while True:
        TieneDescuento = input("¿El cliente posee descuento? (S/N)").upper()

        if TieneDescuento == "S" or TieneDescuento == "N":
            break

        else:

            print("Error debe ingresar S o N")

    if TieneDescuento == "S":

        PrecioConDescuento = PrecioProducto - (PrecioProducto * 0.10)

        TotalConDescuento += PrecioConDescuento

    elif TieneDescuento == "N":

        TotalConDescuento += PrecioProducto
AhorroTotal = TotalSinDescuento - TotalConDescuento
PromedioProducto = TotalConDescuento / CantidadProductosC

print(f"Total sin descuentos: ${TotalSinDescuento}")
print(f"Total con descuentos: ${TotalConDescuento:.2f}")
print(f"Ahorro: ${AhorroTotal:.2f}")
print(f"Promedio por producto: ${PromedioProducto:.2f}")

print("#" * 10)
## Ejercicio 2 

UsuarioCorrecto = "alumno"
ClaveCorrecta = "python123"
cont = 0
AccesoConcedido = False


for i in range(3):
    Usuario = input("Ingrese su usuario: ")
    Clave = input("Ingrese su clave: ")
    cont += 1

    if Usuario == UsuarioCorrecto and Clave == ClaveCorrecta:
        AccesoConcedido = True
        break

    elif Usuario != UsuarioCorrecto:
        print("Error: Usuario incorrecto")

    elif Clave != ClaveCorrecta:
        print("Error: Clave incorrecta")

if AccesoConcedido == False:
    print("Cuenta bloqueada")

else:
    while True:
        print("1) Ver estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mostrar mensaje motivacional")
        print("4) Salir")

        opcion = input("Ingrese su opcion: ")

        if not opcion.isdigit():
            print("Error: debe ingresar un numero")

        else:

            opcion = int(opcion)

            if opcion < 1 or opcion > 4:
                print("Error: Debe ser un numero entre 1 y 4")

            else:
                if opcion == 1:
                    print("Inscripto")

                elif opcion == 2:
                    while True:
                        clave1 = input("Ingrese su nueva clave: ")

                        if len(clave1) < 6:
                            print("Error: La clave tiene que tener minimo 6 caracteres")

                        else:
                            clave2 = input("Ingrese nuevamente su clave: ")

                            if clave1 == clave2:
                                ClaveCorrecta = clave1
                                print("Clave cambiada correctamente")
                                break

                            else:
                                print("Error: Las claves no coinciden")


                elif opcion == 3:
                    print("Cada dia es una oportunidad para mejorar")


                else:
                    break
print("#" * 10)
 ##ejercicio3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    Operador = input("Ingrese el nombre del operador: ")

    if Operador == "":
        print("Error: no puede estar vacío")

    elif not Operador.isalpha():
        print("Error: solo letras")

    else:
        break


while True:

    print("\n1) Reservar turno")
    print("2) Cancelar turno (por nombre)")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Ingrese su opcion: ")

    if not opcion.isdigit():
        print("Error: debe ingresar un numero")

    else:
        opcion = int(opcion)

        if opcion < 1 or opcion > 5:
            print("Error: Debe ser un numero entre 1 y 5")

        else:

            # OPCION 1 
            if opcion == 1:

                while True:
                    Dia = input("Seleccione día (1=Lunes / 2=Martes): ")

                    if not Dia.isdigit():
                        print("Error: debe ingresar un número")

                    else:
                        Dia = int(Dia)

                        if Dia == 1 or Dia == 2:
                            break

                        else:
                            print("Error: seleccione 1 o 2")


                while True:
                    Paciente = input("Ingrese nombre del paciente: ")

                    if Paciente == "":
                        print("Error: el nombre no puede estar vacío")

                    elif not Paciente.isalpha():
                        print("Error: el nombre solo puede contener letras")

                    else:

                        if Dia == 1:

                            if Paciente == lunes1 or Paciente == lunes2 or Paciente == lunes3 or Paciente == lunes4:
                                print("Error: el paciente ya tiene un turno ese día")

                            else:
                                break

                        elif Dia == 2:

                            if Paciente == martes1 or Paciente == martes2 or Paciente == martes3:
                                print("Error: el paciente ya tiene un turno ese día")

                            else:
                                break


                if Dia == 1:

                    if lunes1 == "":
                        lunes1 = Paciente
                        print("Turno reservado correctamente")

                    elif lunes2 == "":
                        lunes2 = Paciente
                        print("Turno reservado correctamente")

                    elif lunes3 == "":
                        lunes3 = Paciente
                        print("Turno reservado correctamente")

                    elif lunes4 == "":
                        lunes4 = Paciente
                        print("Turno reservado correctamente")

                    else:
                        print("No hay turnos disponibles para el lunes")


                elif Dia == 2:

                    if martes1 == "":
                        martes1 = Paciente
                        print("Turno reservado correctamente")

                    elif martes2 == "":
                        martes2 = Paciente
                        print("Turno reservado correctamente")

                    elif martes3 == "":
                        martes3 = Paciente
                        print("Turno reservado correctamente")

                    else:
                        print("No hay turnos disponibles para el martes")


            # OPCION 2 
            elif opcion == 2:

                while True:
                    Dia = input("Seleccione día (1=Lunes / 2=Martes): ")

                    if not Dia.isdigit():
                        print("Error: debe ingresar un número")

                    else:
                        Dia = int(Dia)

                        if Dia == 1 or Dia == 2:
                            break

                        else:
                            print("Error: seleccione 1 o 2")


                while True:
                    PacienteCancelar = input("Ingrese nombre del paciente: ")

                    if PacienteCancelar == "":
                        print("Error: el nombre no puede estar vacío")

                    elif not PacienteCancelar.isalpha():
                        print("Error: el nombre solo puede contener letras")

                    else:
                        break


                if Dia == 1:

                    if PacienteCancelar == lunes1:
                        lunes1 = ""
                        print("Turno cancelado correctamente")

                    elif PacienteCancelar == lunes2:
                        lunes2 = ""
                        print("Turno cancelado correctamente")

                    elif PacienteCancelar == lunes3:
                        lunes3 = ""
                        print("Turno cancelado correctamente")

                    elif PacienteCancelar == lunes4:
                        lunes4 = ""
                        print("Turno cancelado correctamente")

                    else:
                        print("El paciente no tiene turno el lunes")


                elif Dia == 2:

                    if PacienteCancelar == martes1:
                        martes1 = ""
                        print("Turno cancelado correctamente")

                    elif PacienteCancelar == martes2:
                        martes2 = ""
                        print("Turno cancelado correctamente")

                    elif PacienteCancelar == martes3:
                        martes3 = ""
                        print("Turno cancelado correctamente")

                    else:
                        print("El paciente no tiene turno el martes")


            # OPCION 3 
            elif opcion == 3:

                while True:
                    Dia = input("Seleccione día (1=Lunes / 2=Martes): ")

                    if not Dia.isdigit():
                        print("Error: debe ingresar un número")

                    else:
                        Dia = int(Dia)

                        if Dia == 1 or Dia == 2:
                            break

                        else:
                            print("Error: seleccione 1 o 2")


                if Dia == 1:

                    print("\n--- AGENDA DEL LUNES ---")

                    if lunes1 == "":
                        print("Turno 1: (libre)")
                    else:
                        print("Turno 1:", lunes1)

                    if lunes2 == "":
                        print("Turno 2: (libre)")
                    else:
                        print("Turno 2:", lunes2)

                    if lunes3 == "":
                        print("Turno 3: (libre)")
                    else:
                        print("Turno 3:", lunes3)

                    if lunes4 == "":
                        print("Turno 4: (libre)")
                    else:
                        print("Turno 4:", lunes4)


                elif Dia == 2:

                    print("\n--- AGENDA DEL MARTES ---")

                    if martes1 == "":
                        print("Turno 1: (libre)")
                    else:
                        print("Turno 1:", martes1)

                    if martes2 == "":
                        print("Turno 2: (libre)")
                    else:
                        print("Turno 2:", martes2)

                    if martes3 == "":
                        print("Turno 3: (libre)")
                    else:
                        print("Turno 3:", martes3)


            # OPCION 4 
            elif opcion == 4:

                OcupadosLunes = 0
                OcupadosMartes = 0

                if lunes1 != "":
                    OcupadosLunes += 1

                if lunes2 != "":
                    OcupadosLunes += 1

                if lunes3 != "":
                    OcupadosLunes += 1

                if lunes4 != "":
                    OcupadosLunes += 1


                if martes1 != "":
                    OcupadosMartes += 1

                if martes2 != "":
                    OcupadosMartes += 1

                if martes3 != "":
                    OcupadosMartes += 1


                DisponiblesLunes = 4 - OcupadosLunes
                DisponiblesMartes = 3 - OcupadosMartes

                print("\n--- RESUMEN GENERAL ---")

                print("Lunes:")
                print("Turnos ocupados:", OcupadosLunes)
                print("Turnos disponibles:", DisponiblesLunes)

                print("Martes:")
                print("Turnos ocupados:", OcupadosMartes)
                print("Turnos disponibles:", DisponiblesMartes)


                if OcupadosLunes > OcupadosMartes:
                    print("El lunes tiene más turnos ocupados")

                elif OcupadosMartes > OcupadosLunes:
                    print("El martes tiene más turnos ocupados")

                else:
                    print("Lunes y martes tienen la misma cantidad de turnos ocupados")


            # OPCION 5 
            elif opcion == 5:
                print("Sistema cerrado")
                break
print("#" * 10)
    ##ejercicio4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidas = 0
bloqueado = False


while True:
    agente = input("Ingrese nombre del agente: ")

    if agente == "":
        print("Error: el nombre no puede estar vacío")

    elif not agente.isalpha():
        print("Error: solo se permiten letras")

    else:
        break


while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and bloqueado == False:

    print("\n--- ESTADO ---")
    print("Agente:", agente)
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)
    print("Código parcial:", codigo_parcial)

    print("\n1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    while True:
        opcion = input("Ingrese una opción: ")

        if not opcion.isdigit():
            print("Error: debe ingresar un número")

        else:
            opcion = int(opcion)

            if opcion < 1 or opcion > 3:
                print("Error: debe ingresar una opción entre 1 y 3")

            else:
                break


    # OPCION 1 
    if opcion == 1:

        energia -= 20
        tiempo -= 2

        forzar_seguidas += 1

        if forzar_seguidas == 3:

            alarma = True
            print("La cerradura se trabó.")
            print("¡Alarma activada!")

            forzar_seguidas = 0

        else:

            if energia < 40:

                while True:
                    riesgo = input("Ingrese un número del 1 al 3: ")

                    if not riesgo.isdigit():
                        print("Error: debe ingresar un número")

                    else:
                        riesgo = int(riesgo)

                        if riesgo >= 1 and riesgo <= 3:
                            break

                        else:
                            print("Error: debe elegir entre 1 y 3")


                if riesgo == 3:
                    alarma = True
                    print("¡Alarma activada!")


            if alarma == False:

                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

            else:
                print("No se pudo abrir la cerradura.")


    # OPCION 2 
    elif opcion == 2:

        energia -= 10
        tiempo -= 3

        forzar_seguidas = 0

        print("Iniciando hackeo...")

        for i in range(4):

            codigo_parcial += "A"

            print(f"Paso {i + 1}/4")
            print("Código:", codigo_parcial)


        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas += 1
            print("¡El hackeo abrió una cerradura!")


    # OPCION 3 
    elif opcion == 3:

        forzar_seguidas = 0

        energia += 15
        tiempo -= 1

        if energia > 100:
            energia = 100


        if alarma == True:

            energia -= 10
            print("La alarma consume 10 puntos extra de energía.")


    # VERIFICAR BLOQUEO
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:

        bloqueado = True


# RESULTADO FINAL
if cerraduras_abiertas == 3:

    print("\nVICTORIA")
    print("¡Abriste la bóveda!")

elif bloqueado == True:

    print("\nDERROTA")
    print("El sistema se bloqueó por la alarma.")

elif energia <= 0 or tiempo <= 0:

    print("\nDERROTA")
    print("Te quedaste sin energía o sin tiempo.")
    
print("#" * 10)
## EJERCICIO5
while True:
    NombreJugador = input("Nombre del Gladiador: ")

    if NombreJugador == "":
        print("Error: Solo se permiten letras")

    elif not NombreJugador.isalpha():
        print("Error: Solo se permiten letras")

    else:
        break

VidaJugador = 100
VidaEnemigo = 100

Pociones = 3

AtaquePesado = 15
DanioEnemigo = 12

TurnoGladiador = True


print("\n=== INICIO DEL COMBATE ===")


while VidaJugador > 0 and VidaEnemigo > 0:

    # TURNO DEL GLADIADOR
    if TurnoGladiador == True:

        print("\n=== NUEVO TURNO ===")
        print(f"{NombreJugador} (HP: {VidaJugador}) vs Enemigo (HP: {VidaEnemigo}) | Pociones: {Pociones}")

        print("\nElige acción:")
        print("1) Ataque Pesado")
        print("2) Ráfaga Veloz")
        print("3) Curar")


        while True:

            opcion = input("Opción: ")

            if not opcion.isdigit():

                print("Error: Ingrese un número válido.")

            else:

                opcion = int(opcion)

                if opcion < 1 or opcion > 3:

                    print("Error: debe elegir una opción entre 1 y 3")

                else:

                    break


        # ATAQUE PESADO
        if opcion == 1:

            if VidaEnemigo < 20:

                DanioFinal = AtaquePesado * 1.5

                VidaEnemigo -= DanioFinal

                print("¡Golpe Crítico!")
                print(f"¡Atacaste al enemigo por {DanioFinal} puntos de daño!")

            else:

                DanioFinal = AtaquePesado

                VidaEnemigo -= DanioFinal

                print(f"¡Atacaste al enemigo por {DanioFinal} puntos de daño!")


        # RAFAGA VELOZ
        elif opcion == 2:

            print(">> ¡Inicias una ráfaga de golpes!")

            for i in range(3):

                VidaEnemigo -= 5

                print("> Golpe conectado por 5 de daño")


        # CURAR
        elif opcion == 3:

            if Pociones > 0:

                VidaJugador += 30
                Pociones -= 1

                print("¡Usaste una poción!")
                print("Recuperaste 30 puntos de vida.")

            else:

                print("¡No quedan pociones!")


        TurnoGladiador = False


    # TURNO DEL ENEMIGO
    else:

        if VidaEnemigo > 0:

            VidaJugador -= DanioEnemigo

            print(f">> ¡El enemigo contraataca por {DanioEnemigo} puntos!")


        TurnoGladiador = True


# FIN DEL JUEGO
if VidaJugador > 0:

    print(f"\n¡VICTORIA! {NombreJugador} ha ganado la batalla.")

else:

    print("\nDERROTA. Has caído en combate.")
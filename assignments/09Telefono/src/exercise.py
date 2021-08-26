def main():
    # escribe tu código abajo de esta línea
    num_msj = int(input("Dame el número de mensajes: "))
    num_megas = float(input("Dame el número de megas: "))
    num_min = int(input("Dame el número de minutos: "))

    costo_mensual = (num_msj * 0.80) + (num_megas * 0.80) + (num_min * 0.80)

    print("El costo mensual es:", costo_mensual)



if __name__ == '__main__':
    main()

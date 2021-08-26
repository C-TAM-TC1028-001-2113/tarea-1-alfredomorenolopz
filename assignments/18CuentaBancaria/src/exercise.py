def main():
    # escribe tu código abajo de esta línea

saldo_mes_anterior = float(input("Dame el saldo del mes anterior: "))
ingresos = float(input("Dame los ingresos: "))
egresos = float(input("Dame los egresos: "))
num_cheques = int(input("Dame el número de cheques: "))

saldo_final = (saldo_mes_anterior + ingresos) - (egresos +(num_cheques * 13))
interes_saldo = (saldo_final * 0.075)
saldo_por_mostrar = saldo_final - interes_saldo

print("El saldo final de la cuenta es:", saldo_por_mostrar)


if __name__ == '__main__':
    main()

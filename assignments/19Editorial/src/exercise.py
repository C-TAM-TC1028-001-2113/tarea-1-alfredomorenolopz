def main():
    # escribe tu código abajo de esta línea

from math import ceil
num_palabras = int(input("Dame el número de palabras: "))
pagina = ceil(num_palabras/475)
publicacion = (pagina * 60)
total = (publicacion * 0.90)

print("El costo de la publicación es:", total)


if __name__ == '__main__':
    main()

def crear_sala():
    print("\n--- CREAR SALA DE CINE ---")

    while True:
        try:
            filas = int(input("Ingresa el numero de filas: "))
            columnas = int(input("Ingresa el numero de columnas: "))

            if filas > 0 and columnas > 0:
                break
            print("Los numeros deben ser mayores a 0.")

        except ValueError:
            print("Ingresa numeros enteros.")

    sala = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append("L")
        sala.append(fila)

    print("\nSala creada correctamente!")

    return sala


def mostrar_sala(sala):
    print("\n--- SALA DE CINE ---")

    for i in range(len(sala)):
        print(f"Fila {i + 1}: ", end="")

        for j in range(len(sala[i])):
            print(sala[i][j], end=" ")

        print()


def reservar_asiento(sala):
    print("\n--- RESERVAR ASIENTO ---")

    try:
        fila = int(input("Ingresa el numero de fila: "))
        columna = int(input("Ingresa el numero de columna: "))

        if fila < 1 or fila > len(sala):
            print("La fila no existe.")
            return

        if columna < 1 or columna > len(sala[0]):
            print("La columna no existe.")
            return

        if sala[fila - 1][columna - 1] == "L":
            sala[fila - 1][columna - 1] = "X"
            print("Asiento reservado correctamente!")

        else:
            print("Este asiento ya esta ocupado.")

    except ValueError:
        print("Debes ingresar numeros enteros.")


def liberar_asiento(sala):
    print("\n--- LIBERAR ASIENTO ---")

    try:
        fila = int(input("Ingresa el numero de fila: "))
        columna = int(input("Ingresa el numero de columna: "))

        if fila < 1 or fila > len(sala):
            print("La fila no existe.")
            return

        if columna < 1 or columna > len(sala[0]):
            print("La columna no existe.")
            return

        if sala[fila - 1][columna - 1] == "X":
            sala[fila - 1][columna - 1] = "L"
            print("Asiento liberado correctamente!")

        else:
            print("Este asiento ya esta libre.")

    except ValueError:
        print("Debes ingresar numeros enteros.")


def contar_asientos(sala):
    print("\n--- ESTADISTICAS DE LA SALA ---")

    libres = 0
    ocupados = 0

    for i in range(len(sala)):
        for j in range(len(sala[i])):

            if sala[i][j] == "L":
                libres += 1

            elif sala[i][j] == "X":
                ocupados += 1

    print("Asientos libres:", libres)
    print("Asientos ocupados:", ocupados)
    print("Total de asientos:", libres + ocupados)


def main():

    sala = crear_sala()

    while True:

        print("\n================================")
        print("       SISTEMA DE CINE")
        print("===============================")
        print("1. Mostrar sala")
        print("2. Reservar asiento")
        print("3. Liberar asiento")
        print("4. Contar asientos ocupados y libres")
        print("5. Salir")
        print("================================")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            mostrar_sala(sala)

        elif opcion == "2":
            reservar_asiento(sala)

        elif opcion == "3":
            liberar_asiento(sala)

        elif opcion == "4":
            contar_asientos(sala)

        elif opcion == "5":
            print("\nGracias por utilizar el sistema de cine!")
            break

        else:
            print("\nOpcion incorrecta. Intenta nuevamente.")


if __name__ == "__main__":
    main()
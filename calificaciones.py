estudiantes = int(input("Ingresa la cantidad de estudiantes: "))
materias = int(input("Ingresa la cantidad de materias: "))

matriz = []

for i in range(estudiantes):
    print(f"\n--- Estudiante {i + 1} ---")
    fila = []
    for j in range(materias):
        while True:
            calif = float(input(f"Calificación de la materia {j + 1} (0-100): "))
            if 0 <= calif <= 100:
                fila.append(calif)
                break
            else:
                print("Error: La calificación debe estar entre 0 y 100.")
    matriz.append(fila)

def imprimir_reporte(matriz, estudiantes, materias):
    print("\n" + "=" * 35)
    print("       REPORTE DE RESULTADOS")
    print("=" * 35)

    # Promedio de cada estudiante
    print("\nPromedio por estudiante:")
    for i in range(estudiantes):
        promedio_est = sum(matriz[i]) / materias
        print(f"  Estudiante {i + 1}: {promedio_est:.2f}")

    # Promedio de cada materia
    print("\nPromedio por materia:")
    for j in range(materias):
        suma_materia = sum(matriz[i][j] for i in range(estudiantes))
        promedio_mat = suma_materia / estudiantes
        print(f"  Materia {j + 1}: {promedio_mat:.2f}")

    # Calificación más alta y más baja de toda la matriz
    calif_max = max(max(fila) for fila in matriz)
    calif_min = min(min(fila) for fila in matriz)

    print("\nEstadísticas generales:")
    print(f"  Calificación más alta: {calif_max:.2f}")
    print(f"  Calificación más baja: {calif_min:.2f}")
    print("=" * 35)


imprimir_reporte(matriz, estudiantes, materias)
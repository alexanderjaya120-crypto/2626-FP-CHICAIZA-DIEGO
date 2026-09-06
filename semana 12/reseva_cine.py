# Programa de reserva de asientos de una sala de cine
# La sala tiene 3 filas y 4 columnas.
# 0 = asiento libre
# 1 = asiento reservado

# Crear una matriz de 3 filas por 4 columnas
# Todos los asientos comienzan libres (0).
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar al usuario la fila y la columna del asiento
fila = int(input("Ingrese la fila del asiento (0 a 2): "))
columna = int(input("Ingrese la columna del asiento (0 a 3): "))

# Verificar que la fila y la columna estén dentro del rango permitido
if fila >= 0 and fila <= 2 and columna >= 0 and columna <= 3:

    # Verificar si el asiento ya está reservado
    if asientos[fila][columna] == 0:

        # Marcar el asiento como reservado
        asientos[fila][columna] = 1
        print("\nEl asiento fue reservado correctamente.")

    else:
        print("\nEl asiento ya estaba reservado.")

    # Mostrar el estado completo de la sala
    print("\nEstado de la sala:")
    print("---------------")

    # Recorrer la matriz utilizando dos bucles anidados
    for i in range(3):
        for j in range(4):
            print(asientos[i][j], end=" ")
        print()

    print("---------------")

else:
    # Mostrar mensaje si los datos ingresados no son válidos
    print("\nError: la fila debe estar entre 0 y 2.")
    print("Error: la columna debe estar entre 0 y 3.")

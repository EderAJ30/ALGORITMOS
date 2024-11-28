import random

por_pasar = ["persona", "lobo", "gallina", "maiz"]
pasados = []

def mostrar_estado(por_pasar, pasados):
    print(f"Por pasar: {por_pasar}")
    print(f"Ya pasados: {pasados}")

def mover_elementos(por_pasar, pasados, elementos):
    for elemento in elementos:
        if elemento in por_pasar:
            por_pasar.remove(elemento)
            pasados.append(elemento)
        elif elemento in pasados:
            pasados.remove(elemento)
            por_pasar.append(elemento)

def verificacion(por_pasar, pasados):
    if "persona" not in por_pasar:
        if "lobo" in por_pasar and "gallina" in por_pasar:
            return False, "El lobo ha comido a la gallina en la orilla izquierda."
        if "gallina" in por_pasar and "maiz" in por_pasar:
            return False, "La gallina ha comido el maíz en la orilla izquierda."
    if "persona" not in pasados:
        if "lobo" in pasados and "gallina" in pasados:
            return False, "El lobo ha comido a la gallina en la orilla derecha."
        if "gallina" in pasados and "maiz" in pasados:
            return False, "La gallina ha comido el maíz en la orilla derecha."
    return True, ""

def mover(por_pasar, pasados):
    movimientos = [
        ["persona", "gallina"], # Persona lleva la gallina
        ["persona"],            # Persona regresa sola
        ["persona", "lobo"],    # Persona lleva el lobo
        ["persona", "gallina"], # Persona regresa con la gallina
        ["persona", "maiz"],    # Persona lleva el maíz
        ["persona"],            # Persona regresa sola
        ["persona", "gallina"]  # Persona lleva la gallina
    ]

    pasos_realizados = []

    for i, movimiento in enumerate(movimientos):
        if random.random() < 0.2:  
            print("\nError del sistema experto: movimiento inesperado.")
            movimiento_erroneo = generacion_aleatorio(por_pasar, pasados)
            mover_elementos(por_pasar, pasados, movimiento_erroneo)
            pasos_realizados.append(f"Movimiento inesperado: {movimiento_erroneo}")
        else:
            mover_elementos(por_pasar, pasados, movimiento)
            pasos_realizados.append(f"Movimiento {i + 1}: {movimiento}")

        mostrar_estado(por_pasar, pasados)

        seguro, mensaje = verificacion(por_pasar, pasados)
        if not seguro:
            print(f"\nAdvertencia: {mensaje}")
            return False, pasos_realizados
    return True, pasos_realizados

def generacion_aleatorio(por_pasar, pasados):
    movimientos_posibles = []
    if "persona" in por_pasar:
        if "lobo" in por_pasar:
            movimientos_posibles.append(["persona", "lobo"])
        if "gallina" in por_pasar:
            movimientos_posibles.append(["persona", "gallina"])
        if "maiz" in por_pasar:
            movimientos_posibles.append(["persona", "maiz"])
        movimientos_posibles.append(["persona"])  
    if "persona" in pasados:
        if "lobo" in pasados:
            movimientos_posibles.append(["persona", "lobo"])
        if "gallina" in pasados:
            movimientos_posibles.append(["persona", "gallina"])
        if "maiz" in pasados:
            movimientos_posibles.append(["persona", "maiz"])
        movimientos_posibles.append(["persona"])
    
    return random.choice(movimientos_posibles) if movimientos_posibles else ["persona"]

print("Estado inicial:")
mostrar_estado(por_pasar, pasados)

exito, pasos = mover(por_pasar, pasados)

if exito and por_pasar == []:
    print("\nAcertijo resueltooooooooo")
    print("\nPasos realizados para resolver el acertijo con éxitooooooo:")
    for paso in pasos:
        print(paso)
else:
    print("\nEl sistema experto falló en resolver el acertijooo")
import csv

def cargar_paises(ruta_archivo):
    paises = []
    try:
        with open(ruta_archivo, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                pais = {
                    "nombre": fila["nombre"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"]),
                    "continente": fila["continente"]
                }
                paises.append(pais)
        print(f"Se cargaron {len(paises)} países correctamente.")
    except FileNotFoundError:
        print("No se encontró el archivo CSV.")
    except Exception as e:
        print("Ocurrió un error al leer el archivo:", e)
    return paises

def guardar_paises(ruta_archivo, paises):
    try:
        with open(ruta_archivo, "w", newline='', encoding='utf-8') as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for p in paises:
                escritor.writerow(p)
        print("Cambios guardados correctamente.")
    except Exception as e:
        print("Error al guardar el archivo:", e)


def buscar_pais(paises, texto):
    encontrados = []
    for p in paises:
        if texto.lower() in p["nombre"].lower():
            encontrados.append(p)
    return encontrados


def filtrar_por_continente(paises, cont):
    filtrados = []
    for p in paises:
        if p["continente"].lower() == cont.lower():
            filtrados.append(p)
    return filtrados


def filtrar_por_poblacion(paises, minimo, maximo):
    resultado = []
    for p in paises:
        if minimo <= p["poblacion"] <= maximo:
            resultado.append(p)
    return resultado


def filtrar_por_superficie(paises, minimo, maximo):
    resultado = []
    for p in paises:
        if minimo <= p["superficie"] <= maximo:
            resultado.append(p)
    return resultado


def ordenar_paises(paises, campo, descendente=False):
    return sorted(paises, key=lambda x: x[campo], reverse=descendente)


def mostrar_lista(paises):
    if len(paises) == 0:
        print("No se encontraron resultados.")
    else:
        for p in paises:
            print(f"{p['nombre']} - {p['continente']} - Pob: {p['poblacion']} - Sup: {p['superficie']} km²")


def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])

    prom_pob = sum(p["poblacion"] for p in paises) / len(paises)
    prom_sup = sum(p["superficie"] for p in paises) / len(paises)

    print(f"País con más población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menos población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Población promedio: {int(prom_pob)}")
    print(f"Superficie promedio: {int(prom_sup)} km²")

    print("\nCantidad de países por continente:")
    continentes = {}
    for p in paises:
        cont = p["continente"]
        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    for cont, cant in continentes.items():
        print(f"{cont}: {cant}")

def agregar_pais(paises):
    print("\n--- Agregar un nuevo país ---")
    nombre = input("Nombre del país: ").strip()
    poblacion = int(input("Población: "))
    superficie = int(input("Superficie en km²: "))
    continente = input("Continente: ").strip()

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("Ese país ya existe en la lista.")
            return

    nuevo = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo)
    print("País agregado correctamente.")


def actualizar_pais(paises):
    print("\n--- Actualizar datos de un país ---")
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(f"Datos actuales: Población {p['poblacion']}, Superficie {p['superficie']} km²")
            try:
                nueva_pob = int(input("Nueva población: "))
                nueva_sup = int(input("Nueva superficie: "))
                p["poblacion"] = nueva_pob
                p["superficie"] = nueva_sup
                print("Datos actualizados correctamente.")
                return
            except ValueError:
                print("Debe ingresar valores numéricos válidos.")
                return

    print("No se encontró el país ingresado.")

def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Buscar país por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por rango de población")
    print("4. Filtrar por rango de superficie")
    print("5. Ordenar países")
    print("6. Ver estadísticas")
    print("7. Salir")
    print("8. Agregar un país")
    print("9. Actualizar superficie y población")

def main():
    from pathlib import Path
    script_dir = Path(__file__).parent
    ruta = script_dir / "paises.csv"   
    paises = cargar_paises(ruta)

    if not paises:
        return

    while True:
        menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            nombre = input("Ingrese nombre o parte del nombre: ")
            resultado = buscar_pais(paises, nombre)
            mostrar_lista(resultado)

        elif opcion == "2":
            cont = input("Ingrese continente: ")
            resultado = filtrar_por_continente(paises, cont)
            mostrar_lista(resultado)

        elif opcion == "3":
            minimo = int(input("Población mínima: "))
            maximo = int(input("Población máxima: "))
            resultado = filtrar_por_poblacion(paises, minimo, maximo)
            mostrar_lista(resultado)

        elif opcion == "4":
            minimo = int(input("Superficie mínima: "))
            maximo = int(input("Superficie máxima: "))
            resultado = filtrar_por_superficie(paises, minimo, maximo)
            mostrar_lista(resultado)

        elif opcion == "5":
            campo = input("Ordenar por (nombre/poblacion/superficie): ").lower()
            desc = input("¿Descendente? (s/n): ").lower()
            descendente = desc == "s"
            ordenados = ordenar_paises(paises, campo, descendente)
            mostrar_lista(ordenados)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "7":
            guardar_paises(ruta, paises)
            print("Programa finalizado.")
            break

        elif opcion == "8":
            agregar_pais(paises)

        elif opcion == "9":
            actualizar_pais(paises)

        else:
            print("Opción no válida, intente otra vez.")

main()
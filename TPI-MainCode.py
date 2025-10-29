import csv
from pathlib import Path


def es_entero_valido(s):
    if not isinstance(s, str):
        return False
    s = s.strip()
    return s.isdigit() and s != ""


def convertir_a_enteros_fila(fila):
    pob = fila.get("poblacion", "").strip()
    sup = fila.get("superficie", "").strip()
    if es_entero_valido(pob) and es_entero_valido(sup):
        return int(pob), int(sup)
    return None, None


def cargar_paises(ruta_archivo):
    paises = []
    ruta = Path(ruta_archivo)
    if not ruta.exists():
        print("No se encontró el archivo CSV:", ruta)
        return paises

    with ruta.open(newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        linea = 1
        for fila in lector:
            linea += 1
            nombre = fila.get("nombre", "").strip()
            continente = fila.get("continente", "").strip()
            pob, sup = convertir_a_enteros_fila(fila)

            if nombre == "" or continente == "" or pob is None or sup is None:
                print(
                    f"Aviso: fila {linea} ignorada por datos incompletos o inválidos."
                )
                continue

            paises.append(
                {
                    "nombre": nombre,
                    "poblacion": pob,
                    "superficie": sup,
                    "continente": continente,
                }
            )

    print(f"Se cargaron {len(paises)} países correctamente.")
    return paises


def guardar_paises(ruta_archivo, paises):
    ruta = Path(ruta_archivo)
    parent = ruta.parent
    if not parent.exists():
        print("Error: la carpeta destino no existe:", parent)
        return

    with ruta.open("w", newline="", encoding="utf-8") as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for p in paises:
            escritor.writerow(
                {
                    "nombre": p.get("nombre", ""),
                    "poblacion": int(p.get("poblacion", 0)),
                    "superficie": int(p.get("superficie", 0)),
                    "continente": p.get("continente", ""),
                }
            )
    print("Cambios guardados correctamente.")


def buscar_pais(paises, texto):
    return [p for p in paises if texto.lower() in p["nombre"].lower()]


def filtrar_por_continente(paises, cont):
    return [p for p in paises if p["continente"].lower() == cont.lower()]


def filtrar_por_poblacion(paises, minimo, maximo):
    return [p for p in paises if minimo <= p["poblacion"] <= maximo]


def filtrar_por_superficie(paises, minimo, maximo):
    return [p for p in paises if minimo <= p["superficie"] <= maximo]


def ordenar_paises(paises, campo, descendente=False):
    campos_permitidos = {"nombre", "poblacion", "superficie", "continente"}
    if campo not in campos_permitidos:
        print("Campo inválido para ordenar. Se usará 'nombre' por defecto.")
        campo = "nombre"
    return sorted(paises, key=lambda x: x[campo], reverse=descendente)


def mostrar_lista(paises):
    if not paises:
        print("No se encontraron resultados.")
    else:
        for p in paises:
            print(
                f"{p['nombre']} - {p['continente']} - Pob: {p['poblacion']} - Sup: {p['superficie']} km²"
            )


def mostrar_estadisticas(paises):
    if not paises:
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
        continentes[cont] = continentes.get(cont, 0) + 1
    for cont, cant in continentes.items():
        print(f"{cont}: {cant}")


def pedir_entero_valido(mensaje, minimo=0, maximo=None):
    while True:
        valor = input(mensaje).strip()
        if es_entero_valido(valor):
            num = int(valor)
            if num < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue
            if maximo is not None and num > maximo:
                print(f"El valor debe ser <= {maximo}.")
                continue
            return num
        print("Ingrese un número entero válido.")


def agregar_pais(paises):
    print("\n--- Agregar un nuevo país ---")
    nombre = input("Nombre del país: ").strip()
    if not nombre:
        print("Nombre inválido.")
        return
    poblacion = pedir_entero_valido("Población: ", minimo=0)
    superficie = pedir_entero_valido("Superficie en km²: ", minimo=0)
    continente = input("Continente: ").strip()
    if not continente:
        print("Continente inválido.")
        return

    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print("Ese país ya existe en la lista.")
            return

    paises.append(
        {
            "nombre": nombre,
            "poblacion": poblacion,
            "superficie": superficie,
            "continente": continente,
        }
    )
    print("País agregado correctamente.")


def actualizar_pais(paises):
    print("\n--- Actualizar datos de un país ---")
    nombre = input("Ingrese el nombre del país a actualizar: ").strip()
    for p in paises:
        if p["nombre"].lower() == nombre.lower():
            print(
                f"Datos actuales: Población {p['poblacion']}, Superficie {p['superficie']} km²"
            )
            p["poblacion"] = pedir_entero_valido("Nueva población: ", minimo=0)
            p["superficie"] = pedir_entero_valido("Nueva superficie: ", minimo=0)
            print("Datos actualizados correctamente.")
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
    print("10. Guardar cambios")


def main():
    script_dir = Path(__file__).parent
    ruta = script_dir / "paises.csv"
    paises = cargar_paises(ruta)

    while True:
        menu()
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            nombre = input("Ingrese nombre o parte del nombre: ")
            mostrar_lista(buscar_pais(paises, nombre))
        elif opcion == "2":
            cont = input("Ingrese continente: ")
            mostrar_lista(filtrar_por_continente(paises, cont))
        elif opcion == "3":
            minimo = pedir_entero_valido("Población mínima: ", minimo=0)
            maximo = pedir_entero_valido("Población máxima: ", minimo=minimo)
            mostrar_lista(filtrar_por_poblacion(paises, minimo, maximo))
        elif opcion == "4":
            minimo = pedir_entero_valido("Superficie mínima: ", minimo=0)
            maximo = pedir_entero_valido("Superficie máxima: ", minimo=minimo)
            mostrar_lista(filtrar_por_superficie(paises, minimo, maximo))
        elif opcion == "5":
            campo = input(
                "Ordenar por (nombre/poblacion/superficie/continente): "
            ).lower()
            desc = input("¿Descendente? (s/n): ").lower() == "s"
            mostrar_lista(ordenar_paises(paises, campo, desc))
        elif opcion == "6":
            mostrar_estadisticas(paises)
        elif opcion == "7":
            print("Programa finalizado.")
            break
        elif opcion == "8":
            agregar_pais(paises)
        elif opcion == "9":
            actualizar_pais(paises)
        elif opcion == "10":
            guardar_paises(ruta, paises)
        else:
            print("Opción no válida, intente otra vez.")

main()

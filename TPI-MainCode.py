import csv
from pathlib import Path


def es_entero(texto):
    #Revisa si el texto representa un número entero positivo.
    if not isinstance(texto, str):
        return False

    texto = texto.strip()
    return texto.isdigit()


def leer_enteros_fila(fila):
    #Convierte los campos población y superficie a enteros.
    poblacion_txt = fila.get("poblacion", "").strip()
    superficie_txt = fila.get("superficie", "").strip()

    if es_entero(poblacion_txt) and es_entero(superficie_txt):
        poblacion = int(poblacion_txt)
        superficie = int(superficie_txt)
        return poblacion, superficie

    return None, None

def cargar_paises(ruta_archivo):
    lista = []
    ruta = Path(ruta_archivo)

    if not ruta.exists():
        print("No se encontró el archivo:", ruta)
        return lista

    with ruta.open(newline="", encoding="utf-8") as arch:
        lector = csv.DictReader(arch)
        numero_fila = 1

        for fila in lector:
            numero_fila += 1

            nombre = fila.get("nombre", "").strip()
            continente = fila.get("continente", "").strip()

            poblacion, superficie = leer_enteros_fila(fila)

            if nombre == "" or continente == "" or poblacion is None or superficie is None:
                print("Aviso: fila", numero_fila, "ignorada por datos inválidos.")
                continue

            pais = {
                "nombre": nombre,
                "poblacion": poblacion,
                "superficie": superficie,
                "continente": continente
            }
            lista.append(pais)

    print("Se cargaron", len(lista), "países.")
    return lista


def guardar_paises(ruta_archivo, paises):
    ruta = Path(ruta_archivo)

    if not ruta.parent.exists():
        print("Error: la carpeta destino no existe:", ruta.parent)
        return

    with ruta.open("w", newline="", encoding="utf-8") as arch:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(arch, fieldnames=campos)
        escritor.writeheader()

        for pais in paises:
            escritor.writerow(pais)

    print("Cambios guardados correctamente.")

def buscar_por_nombre(paises, texto):
    resultados = []
    texto = texto.lower()

    for pais in paises:
        nombre = pais["nombre"].lower()
        if texto in nombre:
            resultados.append(pais)

    return resultados


def filtrar_por_continente(paises, cont):
    resultados = []
    cont = cont.lower()

    for pais in paises:
        if pais["continente"].lower() == cont:
            resultados.append(pais)

    return resultados


def filtrar_por_rango(paises, campo, minimo, maximo):
    resultados = []

    for pais in paises:
        valor = pais[campo]
        if valor >= minimo and valor <= maximo:
            resultados.append(pais)

    return resultados


def ordenar_paises(paises, campo, descendente=False):
    campos_validos = ["nombre", "poblacion", "superficie", "continente"]

    if campo not in campos_validos:
        print("Campo inválido. Se usará 'nombre'.")
        campo = "nombre"

    ordenados = paises[:]  # copia de la lista

    for i in range(len(ordenados)):
        for j in range(i + 1, len(ordenados)):
            a = ordenados[i][campo]
            b = ordenados[j][campo]

            if descendente:
                if a < b:
                    ordenados[i], ordenados[j] = ordenados[j], ordenados[i]
            else:
                if a > b:
                    ordenados[i], ordenados[j] = ordenados[j], ordenados[i]

    return ordenados


def mostrar_lista(paises):
    if len(paises) == 0:
        print("No hay resultados.")
        return

    for p in paises:
        print(p["nombre"], "-", p["continente"],
              "- Pob:", p["poblacion"],
              "- Sup:", p["superficie"], "km²")


def mostrar_estadisticas(paises):
    if len(paises) == 0:
        print("No hay datos cargados.")
        return

    # mayor población
    mayor = paises[0]
    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais

    # menor población
    menor = paises[0]
    for pais in paises:
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

    # promedios
    suma_pob = 0
    suma_sup = 0

    for pais in paises:
        suma_pob += pais["poblacion"]
        suma_sup += pais["superficie"]

    prom_pob = suma_pob / len(paises)
    prom_sup = suma_sup / len(paises)

    print("País con más población:", mayor["nombre"], mayor["poblacion"])
    print("País con menos población:", menor["nombre"], menor["poblacion"])
    print("Población promedio:", int(prom_pob))
    print("Superficie promedio:", int(prom_sup))

    print("\nPaíses por continente:")
    conteo = {}

    for pais in paises:
        cont = pais["continente"]
        if cont not in conteo:
            conteo[cont] = 1
        else:
            conteo[cont] += 1

    for cont in conteo:
        print(cont + ":", conteo[cont])

def pedir_entero(mensaje, minimo=0, maximo=None):
    while True:
        valor = input(mensaje).strip()

        if es_entero(valor):
            numero = int(valor)

            if numero < minimo:
                print("El valor debe ser mayor o igual a", minimo)
                continue

            if maximo is not None and numero > maximo:
                print("El valor debe ser menor o igual a", maximo)
                continue

            return numero

        print("Ingrese un número válido.")


def agregar_pais(paises):
    print("\n--- Agregar país ---")

    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("Nombre inválido.")
        return

    # evitar duplicados
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Ese país ya existe.")
            return

    poblacion = pedir_entero("Población: ", 0)
    superficie = pedir_entero("Superficie km²: ", 0)
    continente = input("Continente: ").strip()

    if continente == "":
        print("Continente inválido.")
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
    print("\n--- Actualizar país ---")

    nombre = input("Nombre del país: ").strip()

    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Datos actuales: Pob", pais["poblacion"], " - Sup", pais["superficie"])
            pais["poblacion"] = pedir_entero("Nueva población: ", 0)
            pais["superficie"] = pedir_entero("Nueva superficie: ", 0)
            print("Actualizado correctamente.")
            return

    print("No se encontró ese país.")

def menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Buscar por nombre")
    print("2. Filtrar por continente")
    print("3. Filtrar por población")
    print("4. Filtrar por superficie")
    print("5. Ordenar países")
    print("6. Ver estadísticas")
    print("7. Agregar país")
    print("8. Actualizar país")
    print("9. Guardar cambios")
    print("10. Salir")


def main():
    ruta = Path(__file__).parent / "paises.csv"
    paises = cargar_paises(ruta)

    while True:
        menu()
        opcion = input("Opción: ").strip()

        if opcion == "1":
            texto = input("Buscar: ")
            resultados = buscar_por_nombre(paises, texto)
            mostrar_lista(resultados)

        elif opcion == "2":
            cont = input("Continente: ")
            resultados = filtrar_por_continente(paises, cont)
            mostrar_lista(resultados)

        elif opcion == "3":
            minimo = pedir_entero("Población mínima: ")
            maximo = pedir_entero("Población máxima: ", minimo)
            resultados = filtrar_por_rango(paises, "poblacion", minimo, maximo)
            mostrar_lista(resultados)

        elif opcion == "4":
            minimo = pedir_entero("Superficie mínima: ")
            maximo = pedir_entero("Superficie máxima: ", minimo)
            resultados = filtrar_por_rango(paises, "superficie", minimo, maximo)
            mostrar_lista(resultados)

        elif opcion == "5":
            campo = input("Campo para ordenar: nombre, poblacion, superficie, continente")
            orden = input("¿Descendente? (s/n): ").lower()
            desc = False
            if orden == "s":
                desc = True
            ordenados = ordenar_paises(paises, campo, desc)
            mostrar_lista(ordenados)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "7":
            agregar_pais(paises)

        elif opcion == "8":
            actualizar_pais(paises)

        elif opcion == "9":
            guardar_paises(ruta, paises)

        elif opcion == "10":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


main()

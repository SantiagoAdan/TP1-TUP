# Gestión de Datos de Países (TPI Programación I)

## Integrantes
- **Santiago Adan Aladzeme**  
- **Ezequiel Gómez**

**Carrera:** Tecnicatura Universitaria en Programación  
**Materia:** Programación I  
**Año:** 2025

---

## 1. Descripción del trabajo
En este trabajo práctico integrador desarrollamos un programa en **Python** que permite gestionar información sobre distintos países.  
El sistema usa un archivo **CSV** para cargar los datos y ofrece distintas opciones para **agregar**, **modificar**, **filtrar**, **ordenar** y **calcular estadísticas**.  

El objetivo fue aplicar los temas vistos en la materia, como el uso de **listas**, **diccionarios**, **funciones**, **estructuras de control** y **lectura de archivos**.

---

## 2. Funcionalidades principales
El programa cuenta con un menú en consola que permite realizar las siguientes acciones:

1. Agregar un nuevo país.  
2. Actualizar la población o superficie de un país existente.  
3. Buscar un país por nombre.  
4. Filtrar países por continente, rango de población o superficie.  
5. Ordenar países por nombre, población o superficie.  
6. Mostrar estadísticas generales.  
0. Salir del programa.  

Cada opción muestra mensajes claros para guiar al usuario y se validan los datos ingresados para evitar errores.

---

## 3. Estructuras y conceptos utilizados
Para resolver el trabajo utilizamos principalmente **listas** y **diccionarios**.  
Cada país se guarda como un diccionario con los campos:

- `nombre`
- `población`
- `superficie`
- `continente`

Todos los países se almacenan dentro de una lista.  

Se implementaron varias **funciones** para dividir las tareas (por ejemplo: agregar, buscar o calcular estadísticas), lo que permite mantener un código **ordenado y modular**.

Se usaron **condicionales** (`if`, `else`) para validar datos y tomar decisiones, y **bucles** (`for`, `while`) para recorrer las listas y mostrar resultados.  
Además, el programa lee los datos desde un **archivo CSV**, lo que facilita trabajar con muchos países a la vez.

---

## 4. Ejemplo del menú principal
===== GESTIÓN DE PAÍSES =====

1. Buscar país por nombre
2. Filtrar por continente
3. Filtrar por rango de población
4. Filtrar por rango de superficie
5. Ordenar países
6. Ver estadísticas
7. Agregar un país
8. Actualizar superficie y población
9. Guardar cambios
10. Salir

---

## 5. Ejemplo de resultados

País con mayor población: China (1,400,000,000)
País con menor población: Islandia (372,000)
Promedio de población: 83,500,000
Promedio de superficie: 2,750,000 km²

Cantidad de países por continente:
América: 5
Europa: 3
Asia: 4
África: 2
Oceanía: 1

## 6. Capturas de pantalla
En este punto se deben insertar las imágenes de la ejecución del programa.  
Nosotros incluimos capturas del **menú principal**, una **búsqueda de país**, un **filtro por continente** y las **estadísticas finales**.

---

## 7. Video explicativo
Grabamos un video de aproximadamente **12 minutos** donde los dos integrantes nos presentamos, explicamos el objetivo del trabajo y mostramos el programa funcionando.  
En el video también comentamos las **dificultades encontradas** y **lo que aprendimos** durante el desarrollo.

---

## 8. Conclusión
Este trabajo nos sirvió para **poner en práctica** todo lo aprendido durante el cuatrimestre.  
Pudimos comprender mejor cómo utilizar las **estructuras de datos** para resolver problemas reales y cómo **organizar el código en funciones**.  

También aprendimos a **validar datos**, **leer archivos CSV** y **trabajar en equipo**.  
En general, fue un trabajo muy completo que nos ayudó a **reforzar los conocimientos** adquiridos en la materia.
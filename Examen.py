peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False]
}
#Formato {codigo: [nombre, genero, duracion, clasificacio, idioma, 3D]}
cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3]
}
#Formatto {codigo: [precio, asientos]}

#Copie los ejemplos del mismo examen para no empezar con un diccionario va

#funcion de validacion
def val_content(palabra): 
    if palabra.strip() == "":
        return False
    return True

#Funcion de opcion 1
def cupos_genero(genero):
    list_cod= []
    for codigo, generos in peliculas.items():
        if genero.lower() == generos[1]:
            list_cod.append(codigo)
    for codigo, cupo in cartelera.items():
        if codigo in list_cod:
            cupos += cupo[1]
    if cupos == 0:
        print("No hay películas en ese rango de precios.")
    else:
        print(f"Hay {cupos} disponibles para ese género de película")


#funcion opcion 2
def busqueda_precio(p_min, p_max):
    list_cod = []
    for codigo, precio in cartelera.items():
        if p_min < precio[0] < p_max:
            list_cod.append(codigo)
    
    if list_cod:
        titulo_cod = []
        for codigo, nombre in peliculas.items():
            if codigo in list_cod:
                titulo_cod.append(f"{nombre[0]}--{codigo}")
                titulo_cod.sort()
    
    if titulo_cod:
        print("Las peliculas en su rango de precio son:")
        k=0
    while k < len(titulo_cod):
        print(f"{titulo_cod[k]}")
        k += 1
    else: 
        print("No se encontraron peliculas en su rango de precio.")

#funcion opcion3 
"""
def actualizar_precio(codigo, nuevo_precio):
    while True:
        for codigo, precio in cartelera.items():
            if codigo in cartelera.items():
                precio[0] = nuevo_precio
"""

#funcion opcion4 
#Validaciones previas
def val_cod(codigo):
    cod = []
    if val_content(codigo) == False:
        return False
    for codigos, k in cartelera.items():
        cod.append(codigos)
    
    if codigo in codigos:
        return False
    
    return True

def val_tit(titulo):
    if val_content(titulo) == True:
        return False
    return True

def val_gen(genero):
    if val_content(genero) == True:
        return False
    return True
def val_dur(dura):
    if int(dura) < 0:
        return False
    return True
def val_clas(clas):
    if clas.upper not in ["A", "B", "C"]:
        return False
    return True
def val_idioma(idioma):
    if val_content(idioma) == True:
        return False
    return True
def val_tresd(tresd):
    if val_content(tresd) == False:
        if tresd.lower == "s":
            estresd = True
            return estresd
        if tresd.lower == "n":
            estresd = False
            return estresd
        return True
    return False

def val_precio(precio):
    if int(precio) < 0:
        return False
    return True
def val_cupos(cupos):
    if int(cupos) <= 0:
        return False
    return True

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    datos = []
    datos.appens[titulo,genero,duracion,clasificacion,idioma,es_3d,precio,cupos]
    pelicula = {
        codigo, datos
    }
    peliculas.append(pelicula)

def menu():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Cupos por género")
        print("2. Búsqueda de películas por rango de precio")
        print("3. Actualizar precio de película")
        print("4. Agregar película")
        print("5. Eliminar película")
        print("6. Salir")
        print("=====================================")

        opcion = input("Ingrese opcion: ")

        if opcion == "1":
            genero = input("Ingrese genero a consultar")
            cupos_genero(genero)
        
        elif opcion == "2":
            p_min = int(input("Ingrese el precio minimo: "))
            p_max = int(input("Ingrese precio maximo: "))

            if (p_min > 0) and (p_max > 0) and (p_min < p_max):
                busqueda_precio(p_min, p_max)
        
        elif opcion == "3":
            continue

        elif opcion == "4":
            codigo = input("Ingrese el codigo: ")
            titulo = input("Ingrese el titulo: ")
            genero = input("Ingrese el genero: ")
            duracion = input("Ingrese la duracion: ")
            clasificacion = input("Ingrese la clasificacion: ")
            idioma = input("Ingrese el idioma: ")
            es_3d = input("Ingrese si la pelicula es 3D (s/n): ")
            precio = input("Ingrese el precio: ")
            cupos = input("Ingrese el cupos: ")
            if val_cod(codigo) == False:
                print("El codigo ingresado esta vacio o no existe")
            if val_tit(titulo) == False:
                print("El titulo ingresado esta vacio")
            if val_gen(genero) == False:
                print("El genero ingresado esta vacio")
            if val_dur(duracion) == False:
                print("La duracion debe ser un entero mayor a 0")
            if val_clas(clasificacion) == False:
                print("La clasificacionj debe ser A, B o C")
            if val_tresd(es_3d) == False:
                print("Ingrese txto (s/n)")
            
            agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos)
        elif opcion == "5":
            continue

        elif opcion == "6":
            print("Programa finalizado.")
            break
        
        else:
            print("Ingrese una opcion valida")

menu()
            
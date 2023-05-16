class habitat:
    def __init__(self,id,nombre,animales):
        self.id = id
        self.nombre = nombre
        self.animales = animales


    def mostrarHabitat(self):
        print("ID:",self.id)
        print("NOMBRE:",self.nombre)

class animal:


    def __init__(self,id,nombre,especie,alimentacion,dieta,edad):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.alimentacion = alimentacion
        self.dieta = dieta
        self.edad = edad

    def mostrarAnimal(self):
        print("ID:",self.id)
        print("NOMBRE:",self.nombre)
        print("ESPECIE:",self.especie)
        print("ALIMENTACION:",self.alimentacion)
        if len(self.dieta) > 0:
            print("DIETA:", end = " ")
            for i in self.dieta:
                print(i, end = ",")
        print("")
        print("EDAD:", self.edad)


#caballo = animal(1,"juan","caballo","herbivoro",["maticas"],5)

#caballo.mostrarInfo()

zoologico = []



def agregarHabitat(id):

    print()
    lista = ["selvatico","desertico","artico","acuatico"]
    x = 0
    for i in range(len(lista)):
        print("(" + str(i+1) + ")" + lista[i])
        x += 1
    print()

    var = False

    while not var:
        try:
            opc = int(input("digite el numero del habitat: "))
            if 0 < opc <= x:
                var = True
            else:
                print()
                print("opcion no disponible")

        except ValueError:
            print()
            print("seleccione las opciones disponibles")


    nuevoHabitat = habitat(id,lista[opc-1],[])

    zoologico.append(nuevoHabitat)

def agregarAnimal(idA):

    opc = 0
    n_habitat = ""

    grupos = [["selvatico", "Leon", "Tigre", "Puma", "Elefante", "Mono", "Gorila", "Chiguiro", "Orangutan", "Ocelote","Pangolino"],
     ["desrtico", "Coyote", "Escorpión", "Jabalí", "Cobra", "Búho", "Gacela de Grant", "Serpiente cascabel","Canguro ratón", "Geco leopardo", "Ardilla"],
     ["artico", "Oso polar", "Zorro ártico", "Morsa", "Foca de Groenlandia", "Ballena beluga", "Caribú","León marino", "Liebre ártica", "Búho nival", "Narval"],
    ["acuatico", "Delfín", "Ballena jorobada", "Tiburón blanco", "Tortuga marina", "Manatí","Pingüino emperador", "Pez payaso", "Pulpo", "Foca común", "Estrella de mar"]
     ]

    # posicion [0][n] los de seltavito, [1][n] del desertico, [2][n] artico y por ultimo [3][n] acuatico

    if len(zoologico)>0:

        print()
        # toma dato nombre
        nombre = input("Nombre: ")
        x = 1
        for habitat in zoologico:
            print("("+str(x)+")"+habitat.nombre)
            x += 1
        print()

        # toma dato habitat que se agregara

        var = False

        while not var:
            try:
                opc = int(input("digite al habitat que va agregar a " + nombre+": "))
                if 0 < opc <= x:
                    var = True
                    n_habitat = zoologico[opc-1].nombre
                else:
                    print()
                    print("opcion no disponible")

            except ValueError:
                print()
                print("seleccione las opciones disponibles")

        #toma dato especie del animal

        lista = {"selvatico":0,"desrtico":1,"artico":2,"acuatico":3}

        x = 1
        for i in range(1,len(grupos[lista[n_habitat]])):
            print("("+str(i)+")"+grupos[lista[n_habitat]][i])
            x += 1
        print()

        var = False

        while not var:
            try:
                especie = int(input("seleccione la especie de " + nombre + ": "))
                if 0 < especie <= x:
                    var = True
                    especie = grupos[lista[n_habitat]][especie]
                else:
                    print()
                    print("opcion no disponible")

            except ValueError:
                print()
                print("seleccione las opciones disponibles")

        # toma alimentacion del animal

        print()
        lista_alimentacion = ["carnivoro","herbivoro","omnivoro"]

        print("(1) carnivoro")
        print("(2) herbivoro")
        print("(3) omnivoro")

        var = False

        while not var:
            try:
                alimentacion = int(input("seleccione la alimentacion " + nombre + ": "))
                if 0 < alimentacion <= 3:
                    var = True
                    alimentacion = lista_alimentacion[alimentacion-1]
                else:
                    print()
                    print("opcion no disponible")

            except ValueError:
                print()
                print("seleccione las opciones disponibles")

        # toma de dato dieta del animal

        var = False
        dieta = []

        while not var:
            try:
                print()
                print("digite los alimentos en la dieta de " + nombre)
                print("si no desea agregar mas digite la letra n")

                dato = ""
                while dato != "n":
                    dato = input()
                    dieta.append(dato)

                if dato == "n":
                    var = True

                else:
                    print()
                    print("opcion no disponible")

            except ValueError:
                print()
                print("seleccione las opciones disponibles")

        # toma dato edad

        while True:
            try:
                edad = int(input("digite la edad de "+nombre+": "))
                break
            except ValueError:
                print()
                print("valor no disponible")


        nuevo_animal = animal(idA,nombre,especie,alimentacion,dieta,edad)

        zoologico[opc-1].animales.append(nuevo_animal)

        print(nombre + " fue agregado con exito")


    else:
        print()
        print("no hay habitats disponibles para agregar el animal")



def mostrarInfo():

    print()
    print("|HABITATS|")
    if len(zoologico) > 0:
        for h in zoologico:
            h.mostrarHabitat()
            print("|ANIMALES|")
            if len(h.animales) > 0:

                for i in range(len(h.animales)):
                    h.animales[i].mostrarAnimal()
            else:
                print("sin animales")
            print()

    else:
        print("el zoologico no tiene habitats, agrega uno")



def dieta():

    salida = False

    print()
    if len(zoologico) > 0:
        info = input("digite el id del animal que quiere editar su dieta: ")
        for h in zoologico:
            if salida == True:
                break
            for i in h.animales:
                if salida == True:
                    break

                if i.id == info:
                    if len(i.dieta) > 0:
                        for j in i.dieta:
                            print(j)
                    else:
                        print("no se encuentra ningun alimento en la dieta")

                print()
                opc = 0

                while opc != 3:
                    print("(1) agregar")
                    print("(2) eliminar")
                    print("(3) salir")


                    var = False

                    while not var:

                        try:
                            opc = int(input("digite la opcion que desea: "))
                            if(0 < opc <= 3):
                                var = True
                        except ValueError:
                            print("seleccione una opcion disponible")

                    if opc == 1:
                        opc = input("digite el alimento a ingresar: ")
                        i.dieta.append(opc)
                    elif opc == 2:
                        var2 = False
                        opc = input("digite el alimento que va a eliminar: ")
                        for j in i.dieta:
                            if j == opc:
                                i.dieta.remove(j)
                                var2 = True
                        if(var2 == False):
                            print("el alimento no se encuentra en la dieta")
                    elif opc == 3:
                        salida = True

    else:
        print("el zoologico no tiene habitats, agrega uno")




def zoo():


    opc = -1
    id = 1
    idA = 1

    funciones = [agregarHabitat,agregarAnimal,mostrarInfo,dieta]

    while opc != 0:
        print()

        print("   ZOOLOGICO")
        print("(1) agregar habitat")
        print("(2) agregar animal")
        print("(3) visualizar informacion")
        print("(4) dieta")
        print("(5) accion")
        print("(0) salir")
        print()


        var = False
        while not var:
            try:
                opc = int(input("digite la opcion: "))
                if(0 < opc <= 5):
                    var = True
                else:
                    print()
                    print("seleccione las opciones disponibles")

            except ValueError:
                print()
                print("valor no disponible")
        var = True

        if opc == 1:
            funciones[0](id)
            id += 1
        elif opc == 2:
            funciones[1](idA)
            idA += 1
        else:
            funciones[opc-1]()


zoo()
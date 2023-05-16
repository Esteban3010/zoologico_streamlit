import streamlit as st

import pandas as pd
import numpy as np



class habitat:
    def __init__(self,Id,nombre,animales):
        self.Id = Id
        self.nombre = nombre
        self.animales = animales


    def mostrarHabitat(self):
        st.write("### Habitat",self.nombre)
        st.write("ID:",self.Id)
        
        

class animal:


    def __init__(self,Id,nombre,especie,alimentacion,dieta,edad):
        self.Id = Id
        self.nombre = nombre
        self.especie = especie
        self.alimentacion = alimentacion
        self.dieta = dieta
        self.edad = edad

    def mostrarAnimales(self):
        var = ""
        st.write("ID: ",self.Id)
        st.write("NOMBRE: ",self.nombre)
        st.write("ESPECIE: ",self.especie)
        st.write("ALIMENTACION: ",self.alimentacion)
        if len(self.dieta) > 0:
            #st.write("DIETA:",self.dieta)
            for i in self.dieta:
                var += i
                var += ", "
            st.write("DIETA: ",var)
        else:
            st.write("no hay alimentos en la dieta")
        st.write("")
        st.write("EDAD: ", self.edad)

        

def main():


    if "zoologico" not in st.session_state:
        st.session_state.zoologico = []

    if "idh" not in st.session_state:
        st.session_state.idh = 0

    if "ida" not in st.session_state:
        st.session_state.ida = 0
        

    if "opc" not in st.session_state:
        st.session_state.opc = 0

    if "op2" not in st.session_state:
        st.session_state.op2 = 0

    if "lista_dieta" not in st.session_state:
        st.session_state.lista_dieta = []

        

    
    st.markdown("<h1 style='text-align: center;'>Zoologico</h1>", unsafe_allow_html=True)

    st.subheader("Menu")
    
    boton_agregar_habitat = st.button('Agregar habitat',1)
    boton_agregar_animal = st.button("Agregar animal",2)
    boton_info = st.button("Mostrar Informacion",3)
    boton_dieta = st.button("Editar Dieta",5)
    
    # asignacion botones
    if boton_agregar_habitat:
        st.session_state.opc = 1
        
    elif boton_agregar_animal:
        st.session_state.opc = 2
        
    elif boton_info:
        st.session_state.opc = 3

    elif boton_dieta:
        st.session_state.opc = 4
    

        
        
    # ejecucion botones
    if st.session_state.opc == 1:
        agregarHabitat()
        
    elif st.session_state.opc == 2:
        if len(st.session_state.zoologico) > 0:
            agregarAnimal()
        else:
            st.write("no hay habitats disponibles, agrega uno")
        
    elif st.session_state.opc == 3:
        mostrarInfo()

    elif st.session_state.opc == 4:
        if len(st.session_state.zoologico) > 0:
            editarDieta()
        else:
            st.write("no hay habitats disponibles, agrega uno")
        
        

    if st.session_state.opc != 0:
        if st.button("salir"):
            st.session_state.opc = 0
            st.experimental_rerun()
        

def agregarHabitat():
    
    st.write("Seleccione el tipo de hábitat:")
    options = ["selvatico", "desertico", "artico","acuatico"]
    selected_option = st.radio("", options)

    if st.button("confirmar",4):
        st.session_state.idh += 1
        nuevo = habitat(st.session_state.idh,selected_option,[])
        st.session_state.zoologico.append(nuevo)
        st.session_state.opc = 0
        st.experimental_rerun()
            
def agregarAnimal():

    grupos = [["selvatico", "Leon", "Tigre", "Puma", "Elefante", "Mono", "Gorila", "Chiguiro", "Orangutan", "Ocelote","Pangolino"],
     ["desrtico", "Coyote", "Escorpión", "Jabalí", "Cobra", "Búho", "Gacela de Grant", "Serpiente cascabel","Canguro ratón", "Geco leopardo", "Ardilla"],
     ["artico", "Oso polar", "Zorro ártico", "Morsa", "Foca de Groenlandia", "Ballena beluga", "Caribú","León marino", "Liebre ártica", "Búho nival", "Narval"],
    ["acuatico", "Delfín", "Ballena jorobada", "Tiburón blanco", "Tortuga marina", "Manatí","Pingüino emperador", "Pez payaso", "Pulpo", "Foca común", "Estrella de mar"]
     ]



    nombre = st.text_input("Escribe el nombre del animal:",key = 4)
    

    st.write("Habitat en el que lo vas agregar")
    lista_disponibles = []
    for h in st.session_state.zoologico:
        lista_disponibles.append([h.Id,h.nombre])
    valor = st.radio("", lista_disponibles)
    
    id_habitat = valor[0]
    habitat = valor[1]


    st.write("selecciona una especie para un habitat del tipo",habitat,":")
    lista_animales = []
    if habitat == "selvatico":
        for i in range(1,len(grupos[0])):
            lista_animales.append(grupos[0][i])
    elif habitat == "desertico":
        for i in range(1,len(grupos[0])):
            lista_animales.append(grupos[1][i])
    elif habitat == "artico":
        for i in range(1,len(grupos[0])):
            lista_animales.append(grupos[2][i])
    elif habitat == "acuatico":
        for i in range(1,len(grupos[0])):
            lista_animales.append(grupos[3][i])
    especie = st.radio("", lista_animales)

    
    st.write("seleccione el tipo de alimentacion")
    lista_alimentacion = ["carnivoro","herbivoro","omnivoro"]
    alimentacion = st.radio("", lista_alimentacion)


    st.write("agregue los alimentos del animal:")
    st.write(st.session_state.lista_dieta)
    var = st.text_input("",key=10)
    if st.button("agregar"):
        if var not in st.session_state.lista_dieta: 
            st.session_state.lista_dieta.append(var)
            st.experimental_rerun()
        else:
            st.write("ya se encuentra el alimento")


    edad = st.slider("Selecciona la edad del animal:",1,100)

    opc = 0
    if st.button("Enviar"):
        opc = 1
            
    if opc == 1:
        st.session_state.ida += 1
        nuevo = animal(st.session_state.ida,nombre,especie,alimentacion,st.session_state.lista_dieta,edad)

        for h in st.session_state.zoologico:
            if h.Id == id_habitat:
                h.animales.append(nuevo)
        st.session_state.opc = 0
        st.experimental_rerun()

def editarDieta():

    st.write("selecciona el habitat del animal:",key=6)
    lista_disponibles = []
    for h in st.session_state.zoologico:
        lista_disponibles.append([h.Id,h.nombre])
    valor = st.radio("", lista_disponibles)

    id_habitat = valor[0]

    st.write("selecciona la dieta del animal que quiere editar:",key=7)
    lista_animales = []
    tamaño = 0
    for h in st.session_state.zoologico:
        if h.Id == id_habitat:
            tamaño = h.animales
            break
            
    if(len(tamaño) > 0):
        
        for j in h.animales:
            lista_animales.append([j.Id,j.nombre])
        valor_2 = st.radio("",lista_animales)
        id_animal = valor_2[0]

        st.write("alimentos en dieta:")
        alimentos = []
        for x in h.animales:
            if x.Id == id_animal:
                alimentos = x.dieta
                break
            
        st.write(alimentos)

        opc = 0

        boton_agregar = st.button("agregar")
        boton_eliminar = st.button("eliminar")

        if boton_agregar:
            st.session_state.op2 = 1
        elif boton_eliminar:
            st.session_state.op2 = 2


        if st.session_state.op2 == 1:
            dato = st.text_input("Escribe el dato que vas agregar:",key = 11)
            if st.button("confirmar"):
                st.session_state.op2 = 3
                
            if st.session_state.op2 == 3:
                for x in h.animales:
                    if x.Id == id_animal:
                        if dato not in x.dieta: 
                            x.dieta.append(dato)
                            st.experimental_rerun()
                        else:
                            st.write("ya se encuentra el alimento")       
                        break
                    
        elif st.session_state.op2 == 2:

            
            dato = st.text_input("Escribe el dato que va eliminar:",key = 13)
            if st.button("confirmar"):
                st.session_state.op2 = 3

            if st.session_state.op2 == 3:
                for x in h.animales:
                    if x.Id == id_animal:
                        if dato in x.dieta: 
                            x.dieta.remove(dato)
                            st.experimental_rerun()
                        else:
                            st.write("el dato no se encuentra en la lista")       
                        break
            
            
            
    else:
        st.write("no hay animales en este habitat")
    

    
    

def mostrarInfo():
    

    if len(st.session_state.zoologico) > 0:
        
        for i in st.session_state.zoologico:
            st.write("")
            st.write("")
            st.write("")
            i.mostrarHabitat()
            if len(i.animales) > 0:
                st.write("#### Animales")
                for j in i.animales:
                    j.mostrarAnimales()
            else:
                st.write("no hay animales disponibles")
            
    else:
        st.write("no se encuentran habitats, agrega uno")


if __name__ == "__main__":
    main()
        
   
    





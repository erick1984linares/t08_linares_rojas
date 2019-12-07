#ejercicio1
nombre="erick"
escuela="EPIE"
curso="progrmacion 1"

mensaje=nombre, "estudia", curso, "en la", escuela
print(mensaje)

#ejercicio2
cliente="john"
deuda=3000
calle="balta #302"
hora="10:20 a.m"

mensaje="estimado cliente", cliente, "ud tiene una deuda de s/", deuda, "porfavor acercarse a la calle", calle, "a la hora", hora
print(mensaje)

#ejercicio3
nombre="juan"
trabajo="ingeniero"
edad="28 años"
mensaje=nombre + " es " + trabajo + "\n" + " tiene " + edad
print(mensaje)

#ejercicio4
empresa="PLAZAVEA"
cliente="Juan"
producto="carne de res"
mensaje=nombre + " compra " + producto + "\n" + " en " + empresa
print(mensaje)

#ejercicio5
candidato="Keiko"
elecciones=2021
mensaje=candidato, " postulara en las elecciones del ", elecciones
print(mensaje)

#ejercicio6
animal="rinoceronte negro"
lugar="Africa"
anio=2018
mensaje="El ", animal, " de ", lugar, "fue declarado extinto en el año", anio
print(mensaje)

#ejercicio7
alumno="pedro"
curso="programacion"
lenguaje="python"
mensaje=alumno, "utiliza", lenguaje, "como lengiaje de maquina en", curso
print(mensaje)

#ejercicio8
celular1="sansumg"
celular2="iphone"
celular3="LG"
mensaje=celular1, celular2, "y", celular3, "compiten en el mercado mundial"
print(mensaje)

#ejercicio9
bebida1="coca cola"
bebida2="pepsi"
bebida3="corona"
mercado="a nivel mundial"
mensaje=bebida1, bebida2, "y", bebida3, "son las bebidas mas compradas", mercado
print(mensaje)

#ejercicio10
pregunta="¿Cual es tu edad?"
print(pregunta)
respuesta=input("ingrese rspuesta:")
if (respuesta=="50"):
    print("respuesta correcta")
else:
    print("respuesta incorrecta")

#ejercicio11
pregunta="¿Cual es el nombre del rector?"
print(pregunta)
respuesta=input("ingrese rspuesta:")
if (respuesta=="Aurelio"):
    print("respuesta correcta")
else:
    print("respuesta incorrecta")

#ejercicio12
pregunta="¿como te llamas?"
print(pregunta)
respuesta=input("ingrese rspuesta:")
if (respuesta=="juana"):
    print("respuesta correcta")
else:
    print("respuesta incorrecta")

#ejercicio13
pregunta="¿donde vives?"
print(pregunta)
respuesta=input("ingrese rspuesta:")
if (respuesta=="chiclayo"):
    print("respuesta correcta")
else:
    print("respuesta incorrecta")

#ejercicio14
pregunta="¿Que estudias?"
print(pregunta)
respuesta=input("ingrese rspuesta:")
if (respuesta=="Ing civil"):
    print("respuesta correcta")
else:
    print("respuesta incorrecta")

#ejercicio15
import os
nombre, profesion, lugar_de_trabajo, edad="", "", "", 0

#concatenacion
nombre=os.sys.argv[1]
profesion=os.sys.argv[2]
lugar_de_trabajo=os.sys.argv[3]
edad=int(os.sys.argv[4])

mensaje=nombre + "tiene" + edad + "es" + profesion + "y trabaja en" + lugar_de_trabajo
print(mensaje)
if (edad>50):
    mensaje=nombre + "gano un puesto de trabajo en" + lugar_de_trabajo + "como" + profesion
    #fin_if

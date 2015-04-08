# -*- coding:utf-8 -*-
"""
Autor: @Statick, Martin Cueva
Objetivo del Juego: Atrapar la mayor cantidad de Tortas de Jamon que caen del cielo

"""

#Importamos la Biblioteca de Pilas-Engine y el módulo random
import pilasengine
import random

#Iniciando PilasEngine en un sola variable parara facilitar la programación
pilas = pilasengine.iniciar()

#Reinicia el juego si existe algun inconveniente
pilas.reiniciar_si_cambia(__file__)

#Declarando la clase Chavo
class Chavo(pilasengine.actores.Actor):

    #Creando la función iniciar del actor chavo
    def iniciar(self):

        self.imagen = "data/chavo.png"
        self.y = -144
        self.escala = 0.9
        self.etiquetas.agregar('chavo')
        self.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 60, 170, sensor=True)

    #Creando la función actualizar del actor chavo
    def actualizar(self):

        #Haciendo que el actor chavo se mueva a la derecha con tecla derecha
        if pilas.control.izquierda:
            self.x -= 5
            self.espejado = True

        if self.x <= -280:
                self.x = -280

	#Haciendo que el actor chavo se mueva a la izquierda con la tecla izquierda
        if pilas.control.derecha:
            self.x += 5
            self.espejado = False

        if self.x >= 280:
                self.x = 280

#Creando la clase Torta de Jamon
class Torta_de_Jamon(pilasengine.actores.Aceituna):

    #Inicializando la clase Torta de Jamon
    def iniciar(self):
        self.imagen = "data/torta_de_jamon.png"
        self.aprender(pilas.habilidades.PuedeExplotarConHumo)
        self.x = pilas.azar(-280, 280)
        self.y = 290
        self.velocidad = pilas.azar(5, 30)/10.0
        self.etiquetas.agregar('torta')
        self.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 60, 40, sensor=True)

    #Creando función actualizar
    def actualizar(self):
        self.rotacion += 5
        self.y -= self.velocidad

        #Eliminar el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()

#Agregando Fondo
fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar("data/vecindad_fondo.jpg")

#Creando el grupo tortas
tortas = pilas.actores.Grupo()

#Creando la función crear_torta, esta función permite crear los enemigos
def crear_torta():
    actor = Torta_de_Jamon(pilas)
    tortas.agreagar(actor)

#Agregar la tarea de crear el enemigo cada 0.5 segundos
pilas.tareas.siempre(1, crear_torta)

#crear el objeto chavo
chavo = Chavo(pilas)

#Agregando el Puntaje
puntaje = pilas.actores.Puntaje(-280, 200, color = pilas.colores.blanco)

#Crear la función que permite al objeto chavo comer las Tortas de Jamon
def cuando_toca_torta(v, i):
    i.eliminar()
    puntaje.aumentar(1)
    puntaje.escala = 2
    puntaje.escala = [1],0.2
    puntaje.rotacion = random.randint(30, 60)
    puntaje.rotacion = [0], 0.2

#Se crea las colisiones entre los actores pilas, torta y se llama a la función cuanto toca torta
pilas.colisiones.agregar("chavo", "torta", cuando_toca_torta)

#Muestra un mensaje en pantalla con indicaciones de que se trata el Juego
pilas.avisar(u"Intente atrapar la mayor cantidad de Tortas de Jamon")

#Permite al motor de pilas ejecutarse
pilas.ejecutar()

# -*- coding:utf-8 -*-
"""
Autor: Martin Cueva
Objetivo del Juego: Atrapar la mayor cantidad de tortas de jamon que caen del cielo

"""

#Importamos la Biblioteca de Pilas-Engine
import pilasengine

#Iniciando PilasEngine en un sola variable parara facilitar la programación
pilas = pilasengine.iniciar()

#Agregando el puntaje
puntaje = pilas.actores.Puntaje(-280, 200, color = pilas.colores.blanco)

#Declarando la clase Chavo
class Chavo(pilasengine.actores.Actor):


    #Creando la función iniciar del actor chavo
    def iniciar(self):

        self.imagen = "data/chavo.png"
        self.y = -144
        self.escala = 0.9
    
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

#Creando la clase Galleta
class Galleta(pilasengine.actores.Aceituna):

    #Inicializando la clase Galleta
    def iniciar(self):
        self.imagen = "data/torta_de_jamon.png"
        self.aprender(pilas.habilidades.PuedeExplotarConHumo)
        self.x = pilas.azar(-200, 200)
        self.y = 290
        self.velocidad = pilas.azar(5, 30)/10.0

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
#Creando el grupo enemigos
enemigos = pilas.actores.Grupo()

#Creando la función enemigo, esta función permite crear los enemigos
def crear_enemigo():
    actor = Galleta(pilas)
    enemigos.agreagar(actor)

#Agregar la tarea de crear el enemigo cada 0.5 segundos
pilas.tareas.siempre(1, crear_enemigo)

#crear el objeto chavo
chavo = Chavo(pilas)

#Crear la función que permite al objeto chavo comer las galletas
def comer_pastel(chavo, Galleta):
    Galleta.eliminar()

#pilas.colisiones.agreagar(chavo, Galleta, comer_pastel)

pilas.avisar(u"enemigas")

pilas.ejecutar()

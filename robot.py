# coding: utf-8
"""
   Un module pour tracer des figures géométriques à l'aide
   d'opérations de dessin primitives.

   Modélise un robot traceur disposant d'un stylet se déplaçant
   sur une feuille de dessin. Ce stylet peut être baissé
   (au contact de la feuille) ou levé (pas de contact avec la feuille).

    - Quel que soit son contact avec la feuille, le stylet avance ou recule selon
     sa direction courante (qui est le nord par défaut).
    - Une commande permet également de le replacer au centre de la feuille.
    - Le stylet peut être orienté dans les 4 directions (nord, sud, est, ouest).
    - Il peut également pivoter vers la droite ou vers la gauche par rapport à
     son orientation courante, ou selon un angle exprimé en degrés (qui est toujours
     considéré comme étant vers la droite de la position courante).
    - La couleur de tracé est noire par défaut, mais elle peut être modifiée, auquel
     cas le tracé restera de la couleur choisie jusqu'au prochain changement de couleur.
"""

import turtle

__robot = None


def init(titre="", largeur=640, hauteur=480):
    """ Initialise l'environnement  (titre et taille de la fenêtre) et place le
    robot au centre, en position levée, orienté vers le nord, tracé de couleur noire """
    global __robot
    turtle.setup(largeur, hauteur)
    turtle.Screen()
    turtle.title(titre)
    turtle.mode('logo')
    __robot = turtle.Turtle()
    up()
    center()
    north()
    color("noir")


def north():
    """ Oriente le robot vers le nord """
    __robot.setheading(0)


def south():
    """ Oriente le robot vers le sud """
    __robot.setheading(180)


def east():
    """ Oriente le robot vers l'est """
    __robot.setheading(90)


def west():
    """ Replace le robot vers l'ouest """
    __robot.setheading(270)


def color(coul):
    """ Modifie la couleur du stylet. Les couleurs possibles sont :
        blanc, noir, rouge, vert, bleu, jaune, violet. Ces couleurs
        sont des chaînes de caractères : couleur("violet"),
        par exemple."""
    couleurs = {'blanc': 'white', 'rouge': 'red',
                'vert': 'green', 'bleu': 'blue',
                'jaune': 'yellow', 'violet': 'purple'}

    if coul in couleurs:
        __robot.color(couleurs[coul])
    else:
        __robot.color('black')


def forward(nb_pas=1):
    """ Avance de nb_pas dans la direction courante """
    __robot.forward(nb_pas)


def backward(nb_pas=1):
    """ Recule de nb_pas dans la direction courante """
    __robot.backward(nb_pas)


def pivote(nb_degres):
    """ Pivote le robot de nb_degres vers la droite """
    __robot.right(nb_degres)


def right():
    """ Pivote de 90° vers la droite par rapport à l'orientation courante """
    __robot.right(90)


def left():
    """ Pivote de 90° vers la gauche par rapport à l'orientation courante """
    __robot.left(90)


def up():
    """ Lève le stylet s'il est baissé """
    __robot.up()


def down():
    """ Met le stylet au contact de la feuille """
    __robot.down()


def center():
    """ Replace le stylet au centre orienté au nord """
    __robot.home()


def hide():
    """ Cache le curseur de tracé """
    __robot.hideturtle()


def quit():
    """ Attend que l'utilisateur clique pour fermer la fenêtre """
    turtle.exitonclick()


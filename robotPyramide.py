#Programme pilotant Robot pour dessiner une Pyramide a base de carrés

from robot import *

nb_etage= 20
nb_espace = 2
nb_pas=1

init("Pyramide")
color("noir")

for etage in range(nb_etage):
	
	#Positionnner le Crayon pour le prochain carré
	up()
	south()	
	forward(nb_espace)
	west()
	forward(nb_espace)
	north()	
	
	#Dessiner le carré
	for nb_cote in range(4):
		down()
		forward(nb_pas)
		right()	
	
	#Ogmenter le nombre de pas a faire pour le prochain carré
	nb_pas = nb_pas+nb_espace*2
hide()
quit()

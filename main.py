from login import User
from  animal import Animal
from objet import Objet
from personne import Personne
user=User.sayHelo()
print ("voulez vous enregistrer des animaux des personnes ou des objets")
choix=input("entre votre choix:")
if choix=="animaux":
    nombre=int(input("entrez le nombre:"))
    animal=Animal.faireChoix()
    animaux=Animal.creeeAnimal(animal,nombre)
    Animal.affichage(animaux)
elif choix=="personnes":
    nombre=int(input("entrez le nombre:"))
    choice=Personne.choisir()
    humain=Personne.creerPersonne(choice,nombre)
    Personne.affichage(humain)

else:
    nombre=int(input("entrez le nombre:")) 
    choisit=Objet.choisir()
    materiel=Objet.creerObjet(choisit,nombre)
    Objet.afficher(materiel)
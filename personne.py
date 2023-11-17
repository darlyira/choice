class Personne():
    def __init__(self,nom,prenom,age,adress):
        self.nom=nom
        self.prenom=prenom
        self.age=age
        self.adress=adress

    def choisir():
        choix=""
        while(choix!="homme" and choix!="femme"):
          choix= input("choisissez homme ou femme") 
        return choix

    def creerPersonne(choisir,nombre):
        list_personne=()
        if(choisir=="homme"):
            for i in range (0,nombre,1):
                nom=input("entrez le nom :")
                prenom=input("entrez le prenom:")
                age=input("entrez l'age :")   
                adress=input("entrez l'adress :") 
                personne=Homme.creationHomme(nom,prenom,age,adress)
                perso=list(list_personne)
                perso.append(personne)
                list_personne=tuple(perso)

        else:
            for i in range (0,nombre,1):
                nom=input("entrez le nom :")
                prenom=input("entrez le prenom :")
                age=input("entrez l;age :")
                adress=input("entrez l'adress :")
                personne=Femme.CreationFemme(nom,prenom,age,adress)
                perso=list(list_personne)
                perso.append(personne)
                list_personne=tuple(perso) 

        return list_personne


    def affichage(liste):
        for item in liste:
            print(f"nom: {item.nom} prenom: {item.prenom} age: {item.age} adress: {item.adress}")  
        pass                             

class Homme(Personne):
        def creationHomme(nom,prenom,age,adress):
          lapersonneHomme=Personne(nom,prenom,age,adress) 
          return lapersonneHomme
        
class Femme(Personne):
      def CreationFemme(nom,prenom,age,adress):
          lapersonneFemme=Personne(nom,prenom,age,adress)
          return lapersonneFemme        

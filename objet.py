class Objet():
    def __init__(self, nom,numeroSerie):
        self.nom=nom
        self.numeroSerie=numeroSerie

    def choisir()    :
        choix=""
        while(choix!= "materiel electronique" and choix!="materiel champetre"):
          choix=  input("choisissez entre materiel electronique et materiel champetre")
        return choix
    
    def creerObjet(choisir,nombre):
        list_objet=()
        if(choisir=="materiel electronique"):
            for i in range(0,nombre,1):
                nom=input("entrez le nom du materiel electronik")
                numeroSerie=input("entrez le numero de serie du materiel electronik")
                materiel_electronic=Electronique.creationObjet1(nom,numeroSerie)
                mat=list(list_objet)
                mat.append(materiel_electronic)
                list_objet=tuple(mat)
        else:
            for i in range(0,nombre,1):
                nom=input("entrez le nom du materiel champetre")
                numeroSerie=input("entrez le numero de serie du materiel champetre")
                materiel_champetre=Champetre.creationObjet2(nom,numeroSerie)
                mat=list(list_objet)
                mat.append(materiel_champetre)
                list_objet=tuple(mat)
        return list_objet



    def afficher(liste):
        for item in liste:
            print(f"nom: {item.nom} numero de serie: {item.numeroSerie}")
            
        


class Electronique(Objet): 
    
    def creationObjet1(nom,numeroSerie):
        electronique=Objet(nom,numeroSerie)
        return electronique    
             
class Champetre(Objet): 
    
    def creationObjet2(nom,numeroSerie):
        objetChampentre=Objet(nom,numeroSerie)
        return objetChampentre    
             
            



        
class Animal:
    def __init__(self, name, age, race):
      self.name = name
      self.age = age
      self.race=race

    def faireChoix():
        choix=""
        while (choix!="chien" and choix!="chat" and choix!="vache"):
            choix=input("Choisissez entre chien,chat et vache ")
        return choix
    def creeeAnimal(choix,nombre):
        list_animaux=()
        if(choix== "chien"):
            for i in range(0,nombre,1):
                nom=input("entre le nom du chien: ")
                age=input("entre l'age du chien: ")
                race=input("entre la race du chien: ")
                chien=Chien.creerChien(nom,age,race)
                chiens=list(list_animaux)
                chiens.append(chien)
                list_animaux=tuple(chiens)
        elif(choix=="chat"):
            for i in range(0,nombre,1):
                
                nom=input("entre le nom du chat: ")
                age=input("entre l'age du chat: ")
                race=input("entre la race du chat: ")
                chat=Chat.creeChat(nom,age,race)
                chats=list(list_animaux)
                chats.append(chat)
                list_animaux=tuple(chats)
                
        else:
          for i in range(0, nombre,1): 
                nom=input("entre le nom de la vache: ")
                age=input("entre l'age de la vache: ")
                race=input("entre la race de la vache: ")
                vache=Vache.creerVache(nom,age,race)
                vaches=list(list_animaux)
                vaches.append(vache)
                list_animaux=tuple(vaches)
        return list_animaux

    def affichage(liste):
        for item in liste:
           print(f"Nom:{item.name} age: {item.age}ans race: {item.race} ")
        pass
        
     
class Chat(Animal):
    def creeChat(name,age,race):
        chat=Animal(name,age, race)
        return chat

class Chien(Animal):
    def __init__(self, name, age,race):
       self.name = name
       self.age = age
       self.race= race
    def creerChien(name,age,race):
        chien=Chien(name,age,race)
        return chien

class Vache(Animal):
    def __init__(self, name, age, race):
      self.name=name
      self.age = age
      self.race=race
    def creerVache( name, age, race):
        vache=Vache( name, age, race)
        return vache


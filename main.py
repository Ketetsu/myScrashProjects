from projet_2 import Liste_des_taches
from datetime import datetime
import json

def menu(taches):
  print("  -------------------MENU-------------------")
  print("""
  1. Ajouter une tâche        2. Trouver une tâche

  3. Liste des tâches         4. Retour à l'acceuil

              <ENTRER> pour quitter
  --------------------------------------------------
  """)
  reponse = input('> ')

  if reponse == '1':
    ajouter_tache(taches)
  elif reponse == '2':
    trouver_tache(taches)
  elif reponse == '3':
    liste_taches(taches)
  elif reponse == '4':
    return acceuil(taches)
  else:
    return

  return menu(taches)

def afficher_tache(tache):
  print(f"""
    Tache : {tache['titre']} ({tache['position']}) 
    Statut : {tache['statut']}
    Details : {tache['contenu']}
    A achever avant le : {tache['echeance']}""")
  print('**********************************')

  rep = input("""
  1. Modifier le titre          2. Modifier l'écheance

  3. Modifier le contenu        4. Achever la tâche
  
                <ENTRER> pour quitter
  >  """)

  if rep == '1':
    new_nom = input('Nouveau titre : ')
    tache['titre'] = new_nom
  elif rep == '2':
    if check_date() != None:
      tache['echeance'] = check_date()
  elif rep == '3':
    new_cont = input('Nouveau contenu : ')
    tache['contenu'] = new_cont
  elif rep == '4':
    tache['statut'] = 'achevé'
  else:
    return

  print('Tâche modifiée !')
  return afficher_tache(tache)
  

def check_date():
  echeance = input("\nEntrez la date d'échéance (jj/mm/aaaa) : ")
  if echeance != '':
    return None
  try:
     datetime.strptime(echeance, "%d/%m/%Y")
  except:
    print("La date d'échéance n'est pas valide. \n")
    return check_date()
  
  return echeance


def ajouter_tache(taches):
  print("\n# Ajouter une tâche \n")
  titre = input("Entrez le titre de la tâche : ")
  new_tache = taches.creer_tache(titre)

  if check_date() != None:
    new_tache['echeance'] = check_date()
        
  return afficher_tache(new_tache)
      
def trouver_tache(taches):
  print("\n# Trouver une tâche \n")
  titre = input("Entrez le titre ou la position de la tâche : ")
  if titre.isdigit():
    index = int(titre) - 1
  else:
    if titre == '':
      return
      
    index = taches.rechercher(titre)

  if index < 0:
    print("La tâche n'existe pas. \n")
    return trouver_tache(taches)
  
  tache = taches.data_liste[index]
  return afficher_tache(tache)
  
def liste_taches(taches):
  print("# Liste des tâches \n")
  taches.afficher_liste()

  input("Appuyez sur <ENTRER> pour retourner au menu")

def rappel_tache(taches):
  classes = taches.classer()
  
  taches_urgentes = classes.get("en cours", []) if classes.get("urgent", []) == []
  if taches_urgentes == [] : return 
    
  taches.trier(taches_urgentes, "echeance")
  print("# Rappel des tâches \n")
  for tache in taches_urgentes:
    index = taches.rechercher(tache)
    print(f"	@ [{index}] {tache}")

def charger_fichier():
		#recupere les informations sauvegardées dans le fichier datas
		#retourne les donnees
		with open("sauvegarde.json", "r") as mon_fichier:
			data = json.loads(mon_fichier.read()) 
		return data

def sauvegarder(taches):
  with open("mon_fichier.json", "w") as fichier_json:
    json.dump(taches, fichier_json)

def acceuil():
  try:
    data = charger_fichier()
  except:
    data = exemple
  taches = Liste_des_taches(data)

  print("  -------------------ACCEUIL-------------------")
  print("\nBienvenue dans votre gestionnaire de tâches !")
  rappel_tache(taches)
  menu(taches)
  


# Exemple---------------------------------------

exemple =[
  {"creation" : "19/09/2024",
    "titre" : "Faire du sport",
    "contenu" : "",
    "position" : 3,
    "echeance" : "24/09/2024",
    "statut" : "urgent"},
  {"creation" : "18/09/2024",
    "titre" : "Lire un livre",
    "contenu" : "",
    "position" : 4,
    "echeance" : "22/09/2024",
    "statut" : "urgent"},
  {"creation" : "17/09/2024",
    "titre" : "Planifier la semaine",
    "contenu" : "",
    "position" : 2,
    "echeance" : "27/09/2024",
    "statut" : "en cours"},
  {"creation" : "16/09/2024",
    "titre" : "Rencontrer des gens",
    "contenu" : "",
    "position" : 1,
    "echeance" : "28/09/2024",
    "statut" : "en cours"},
  {"creation" : "15/09/2024",
    "titre" : "Jouer la guitare",
    "contenu" : "",
    "position" : 5,
    "echeance" : "23/09/2024",
    "statut" : "achevé"},
]

acceuil(exemple)
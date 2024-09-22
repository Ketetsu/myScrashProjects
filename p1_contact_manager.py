import csv
from datetime import datetime
def main():
	
	#Projet : Gestionnaire de Contacts

	#Objectif : Créer un programme Python qui permet de gérer une liste de contacts. Chaque contact doit avoir un nom, un numéro de téléphone, et un âge. Le programme doit permettre de :
		
	def charger_fichier():
		#recupere les informations sauvegardées dans le fichier datas
		#retourne les donnees
		with open("datas.csv", "r") as mon_fichier:
			mon_fichier_csv = csv.DictReader(mon_fichier) 
			donnees = [ligne for ligne in mon_fichier_csv]
		history('Chargement', 'Données')
		return donnees
				
				
	def enregistrer(liste):
				
		#enregistre les informations de la lisye dans le fichier csv
		with open('datas.csv', 'w') as csvfile:
			fieldnames = ["Nom", "Age","Telephone"] 
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames) 
			
			writer.writeheader()
			for element in liste: 
				writer.writerow(element) 
		history('Mise à jour', 'contacts')
				
	def history(action, element):
		#enregistre dans un fichier txt chaque action effectue
		#prend en entrée l'action et l'element sur lequel elle est effectuée
		
		with open('logs.txt', 'a') as log:
			date = datetime.now()
			log.write(f'_ {date} - {action} de {element}\n')
	#1. Stockage des contacts : Utilise une liste pour stocker les contacts. Chaque contact peut être représenté par un dictionnaire avec les clés nom, telephone, et age.
	try:
		contacts = charger_fichier()
		if contacts == [] : raise ValueError
	except:
		history('Utilisation', 'Template')
		contacts = [
		{"Nom": "Bill", "Age":"23", "Telephone": "57285389"},
		{"Nom": "Eudes", "Age":"17", "Telephone": "67229743"},
		{"Nom": "Thomas", "Age":"38", "Telephone": "73862843"},
		{"Nom": "Emmanuel", "Age":"19", "Telephone": "32996721"},
	]
	
	#2. Ajouter un contact : Crée une fonction qui demande à l'utilisateur de saisir les informations pour un nouveau contact et ajoute ce contact à la liste.
	def ajouter_contact(liste):
		#nouveau contact
		contact = {}
		#demande à l'utilisateur de saisir les informations pour un nouveau contact
		print("Renseignez les informations du contact à ajouter")
		contact["Nom"] = input("Nom : ")
		contact["Age"]  = input("Age : ")
		contact["Telephone"] = input("Telephone : ")
		
		#ajoute ce contact à la liste
		liste.append(contact)
		
		print(f"{contact['Nom']} ajouté aux contacts")
		history('Ajout', contact['Nom'])
		
		return liste
	
	#3. Afficher les contacts : Crée une fonction qui affiche tous les contacts de la liste en format lisible.
	def afficher(contact):
		#affiche les détails du contact
		for key, value in contact.items():
			print(f"{key} : {value}")
		print("--------------------------------")
		
	def afficher_contacts(liste):
		#affiche tous les contacts de la liste en format lisible
		for contact in liste:
			afficher(contact)
		input("	entrer pour continuer ")
	#4. Rechercher un contact : Crée une fonction qui permet à l'utilisateur de rechercher un contact par son nom. Affiche les détails du contact s'il est trouvé.
	def rechercher(liste):
		#rechercher un contact par son nom
		print("Renseigner le nom du contact à afficher")
		nom = input("Nom : ")
		
		for index, contact in enumerate(liste):
			if contact["Nom"].lower() == nom.lower():
				#affiche les détails du contact s'il est trouvé.
				print("--------------------------------")
				afficher(contact)
				history('Recherche', nom)
		#retourne l'index du contact s'il est trouvé, sinon -1
				return index
				
		print("Contact non retrouvé")
		return -1
	
	#5. Supprimer un contact : Crée une fonction qui permet à l'utilisateur de supprimer un contact par son nom.
	def supprimer(liste):
		print("Suppression")
		index = rechercher(liste)
		if index >= 0:
			contact = liste[index]
			print(f"ATTENTION : Supprimer le contact de {contact['Nom']}")
			if input(" y/n ?") == "y":
				liste.pop(index)
				print("\n ...Supprimé...")
				history('Suppression', contact['Nom'])
	
	#6. Trier les contacts : Crée une fonction qui trie les contacts par âge et affiche la liste triée.
	def trier_age(liste):
		#trie les contacts par âge
		trie = sorted(liste, key= lambda e: int(e["Age"]))
		afficher_contacts(trie)

	def start(contacts):
		#affiche le menu
		print("\n********************************")
		print("Projet : Gestionnaire de Contacts")
		print("********************************")
		print('''
	1. Ajouter un nouveau contact
	2. Afficher tous les contacts
	3. Rechercher un contact par nom
	4. Supprimer un contact par nom
	5. Trier les contacts par âge
			
	Autre pour quitter
********************************
		''')
		#renvoi vers les fonctions du programme
		reponse = input(" Votre choix : ")
		print()
		
		if reponse=="1":
			print("Ajouter contact")
			print("************************")
			contacts = ajouter_contact(contacts)
		elif reponse=="2":
			print("Afficher les contacts")
			print("************************")
			afficher_contacts(contacts)
		elif reponse=="3":
			print("Rechercher contact")
			print("************************")
			rechercher(contacts)
			input("	entrer pour continuer ")
		elif reponse=="4":
			print("Supprimer contact")
			print("************************")
			supprimer(contacts)
			input("	entrer pour continuer ")
		elif reponse=="5":
			print("Trier les contacts")
			print("************************")
			trier_age(contacts)
		else:
			#arret du programme
			return
		#sauvegarder les informations
		enregistrer(contacts)
		#reboucler le programme
		return start(contacts)
	
	#lancement du programme
	start(contacts)

main()

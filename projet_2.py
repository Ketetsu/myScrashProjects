from datetime import date, timedelta, datetime

'''

from datetime import datetime, timedelta

# Exemple de chaîne de caractères représentant une date
date_str = "2024-09-22"

# Convertir la chaîne en objet datetime
date_echeance = datetime.strptime(date_str, "%Y-%m-%d")

# Obtenir la date actuelle
maintenant = datetime.now()

# Vérifier si la différence entre l'échéance et maintenant est inférieure à 36 heures
duree_r
if duree_restante.total_seconds() < 0:
    print("La tâche est en retard !")
else:
    print(f"Il reste {duree_restante} avant l'échéance.")


class Tache():
	
	def __init__(self, dico, titre=""):
		if titre != "":
			#crée un dictionnaire à partir du titre
			dico = {
				"creation" : date.now().date().strftime("%d/%m/%Y"),,
				"titre" : titre,
				"contenu" : "",
				"echeance" : None,
				"statut" : "en cours"}
				
		self.details = dico
		statut()
		return self.details
		
	def modifier_titre(self, titre):
		self.details["titre"] = titre
		return self.details
	
	def modifier_cont(self, cont):
		self.details["contenu"] = cont
		return self.details
		
	def modifier_fin(self, fin):
		self.details["echeance"] = fin
		return self.details
		
	def achever(self):
		self.details["statut"] = "acheve"
		return self.details
'''

class Liste_des_taches():
		
	def __init__(self, datas):
		self.data_liste = datas #à modifier
		
	def creer_tache(self, titre):
		#crée un objet Tache
		tache = {
			"creation" : date.now().date().strftime("%d/%m/%Y"),
			"titre" : titre,
			"contenu" : "",
			"position" : len(self.data_liste) ,
			"echeance" : None,
			"statut" : "en cours"}
		#ajoute la tache à la liste
		self.data_liste.append(tache)
		#returne l'objet créé'
		return tache
		
	def rechercher(self, nom):
		#parcours les taches
		for index, tache in enumerate(self.data_liste):
			if tache["titre"].lower() == nom.lower():
				#retourne l'index si la tache est trouvée
				return index
		#retourne -1 si non
		return -1
			
	def supprimer(self, index):
		#supprime la tache de la liste
		self.data_liste.pop(index)
		
	def classer(self):
		#met a jour le statu des taches
		self.update_statu()
		liste_classed = {}
		
		#classe les taches par statu 
		for tache in self.data_liste:
			statu = tache["statut"]
			liste_classed[statu] = liste_classed.get(statu, []) + [tache["titre"]]		
			
		return liste_classed      
	
	def update_statu(self):
		#met à jour le statu des listes
			
		for tache in self.data_liste:
			date_echeance = datetime.strptime(tache["echeance"], "%d/%m/%Y")		
			delai = date_echeance - datetime.now()
				
			#statu ==> urgent si echeance est moins de 36h
			if tache["statut"] == "en cours" and delai <= timedelta(hours=36) :
				tache["statut"] = "urgent"
					
			#statu ==> retard si echeance est depassée
			if tache["statut"] == "urgent" and delai.total_seconds() < 0 :
				tache["statut"] = "retard"
			
	def trier(self, liste, critera="creation"):
		
		def get_critera(element):
			index = self.rechercher(element)
			return self.data_liste[index][critera]
			
		#trie une liste en fonction du critere donné
		return sorted(liste, key = get_critera)
		
	def afficher_liste(self):
		#trie la liste en fonction de la date de creation 
		#puis classe du plus ancien au plus recent
		
		trie = sorted(liste, key= lambda e: e["creation"], reverse = True)
		#parcours la liste triée et affiche les taches
		for tache in trie:
			print(f"	@ [{tache['position']}] {tache['titre']}")

#----------------------------------------------------------
#test zone


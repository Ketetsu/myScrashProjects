from datetime import datetime

'''
class Tache():
	
	def __init__(self, dico, titre=""):
		if titre != "":
			#crée un dictionnaire à partir du titre
			dico = {
				"creation" : datetime.now(),
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
			"creation" : datetime.now(),
			"titre" : titre,
			"contenu" : "",
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
		#cree un nouveau dictionnaire où les taches sont classés en fonction de leurs statut
		liste_classed = {}
		'''
		liste_classed = {tache["statut"] : liste_classed.get( tache["statut"], []) + [tache["titre"]] for tache in self.data_liste}
		
		
		for tache in self.data_liste:
			statu = tache["statut"]
			liste_classed[statu] = liste_classed.get(statu, [])
			print(liste_classed[statu])
			liste_classed[statu] = liste_classed[statu].extend(tache["titre"])
			print(liste_classed)'''
		liste_classed = {statut: [tache["titre"] for tache in self.data_liste if tache["statut"] == statut] for statut in set(t["statut"] for t in self.data_liste)}

		return liste_classed
		
		
	def afficher_liste(self):
		#trie la liste en fonction de la date de creation 
		#puis classe du plus ancien au plus recent
		
		trie = sorted(liste, key= lambda e: e["creation"], reverse = True)
		#parcours la liste triée et affiche les taches
		for tache in trie:
			print(f"	@ {tache['titre']}")
		

#-----------
#test zone
exemple =[
	{"creation" : None,
		"titre" : "Faire du sport",
		"contenu" : "",
		"echeance" : None,
		"statut" : "en cours"},
	{"creation" : None,
		"titre" : "Lire un livre",
		"contenu" : "",
		"echeance" : None,
		"statut" : "achevé"},
	{"creation" : None,
		"titre" : "Planifier la semaine",
		"contenu" : "",
		"echeance" : None,
		"statut" : "en cours"},
]

ex = Liste_des_taches(exemple)
print(ex.classer())

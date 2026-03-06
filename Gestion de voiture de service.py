class Employee:
    def __init__(self,NumPermis,nom,prenom):
        self.NumPermis=NumPermis
        self.nom=nom
        self.prenom=prenom
        self.voitureService=None
    def affecter_voiture(self,voiture):
        if self.voitureService==None:
            if voiture.chauffeur==None:
                self.voitureService=voiture
                voiture.chauffeur=self
            else:
                print("la voiture contienne déja un chauffeur")
        else:
            print("le chaufeur a déja une voiture de service")
    def retirer_voiture(self):
        if self.voitureService!=None:
            self.voitureService.chauffeur=None
            self.voitureService=None
        else:
            print("la voiture est dija libre")
    def afficherInformations(self):
        print(f"l'employee {self.nom}  {self.prenom} qui contient numéro de permis{self.NumPermis} ")
        if self.voitureService!=None:
            print(f"le chauffeur posséde la voiture : {self.voitureService.matricule}")
        else:
            print("il n'a pas de voiture pour le moment")
class Voiture:
    def __init__(self,matricule,annee,marque,kilometrage):
        self.matricule=matricule
        self.annee=annee
        self.marque=marque
        self.kilometrage=kilometrage
        self.chauffeur=None


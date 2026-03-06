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
    def afficherInformations(self):
        print(f"la voiture est immatriculer:{self.matricule}annee: {self.annee} marque: {self.marque}kilometrage: {self.kilometrage}")
        if self.chauffeur!=None:
            print(f"son chauffeur est : {self.chauffeur.nom}")
        else:
            print("elle n'a pas de chauffeur pour le moment")
em1= Employee("1233","guerda","said")
em2= Employee("1433","adi","amine")
v1= Voiture ("abc123",2020,"toyota",5000)
v2= Voiture ("arc143",2021,"honda",44000)
em1.affecter_voiture(v1)
em2.affecter_voiture(v2)
em1.affecter_voiture(v2)


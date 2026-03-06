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

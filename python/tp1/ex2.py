class Etudiant():
    def __init__(self, nom, age, notes):
        self.nom = nom
        self.age = age
        self.notes = notes
        
eleves = []

for _ in range(0, 10):
    nom = input("Nom de l'étudiant : ")
    age = int(input("Age de l'étudiant : "))
    notes = [int(input("Notes de l'étudiant : ")) for _ in range(3)]
    eleves.append(Etudiant(nom, age, notes))
    
totalNote = 0
nbNotes = 0
note_max = 0
note_min = 100                                                               

for eleve in eleves:
    
    # On parcourt toutes les notes pour chaque étudiant
    for note in notes:
        
        nbNotes += 1
        totalNote += note
        
        if note > note_max:
            note_max = note
            
        if note < note_min:
            note_min = note

print("Note min : ", note_min)
print("Note max : ", note_max)
print("Moyenne des notes : ", totalNote/nbNotes)
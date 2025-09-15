import csv

#nominert_1/2 er en variabel som blir lagd og blir to av de partiene du kan stemme
nominert_1=input("skriv inn navnet til første nominert: ")
nominert_2=input("skriv inn navnet til andre nominert: ")

# Variabeler for hvem av de nominerte du kan stemme på
nom_1_votes=0
nom_2_votes=0

# en liste med "ID" som du bruker når du stemmer, så det er da 10 stykker som kan stemme
votes_id = ["1","2","3","4","5","6","7","8","9","10"]

num_of_voter=len(votes_id)

while True:
    if votes_id == []:
        print("Avstemningssesjonen er over!")
        if nom_1_votes>nom_2_votes: # Hvis 1. nominerte har større verdi enn 2. nominerte printer den at nominert_1 har vunnet valget
            prosent = (nom_1_votes / num_of_voter) * 100 # Ganger det med 100 for å få prosent
            print(nominert_1,"har vunnet valget","med",prosent,"% stemmer!")
            break

        elif nom_1_votes<nom_2_votes: # Det samme som den over bare med motsatt nominert
            prosent = (nom_2_votes / num_of_voter) * 100
            print(nominert_2,"har vunnet valget","med",prosent,"% stemmer!")
            break

        else:
            print("Valget ble uavgjort!")
            break # Break er for å stoppe den til å gå i loop

    else:
        voter=input("Skriv inn velger-ID-en din, 1-10: ") # Her skriver du "IDen" din og hvis du ikke skriver inn en gyldig "ID" eller en ID som allerede er brukt får du ikke stemmet.
        if voter in votes_id: # Hvis "IDen" er gyldig printer den at du kan stemme og spør deg hva du vil stemme 
            print("Du er en velger ")
            votes_id.remove(voter) #Fjerner "IDen" som ble brukt så den ikke kan bli brukt på nytt
            vote = int(input(f"Legg inn din stemme, 1 for {nominert_1}, 2 for {nominert_2}: ")) # Her velger du hvem av de to nominerte du stemmer. "F" gjør det til en F-string

            if vote==1: # Hvis stemme går til 1, får 1. nominerte ett poeng
                nom_1_votes+=1
                print("Takk for at du avga din stemme!")
                stemme_navn = nominert_1

                with open("stemmer.csv", "a", newline="", encoding="utf-8") as fil:
                    writer = csv.writer(fil)
                    writer.writerow([voter, stemme_navn])

            elif vote==2:
                nom_2_votes+=1
                print("Takk for at du avga din stemme!")
                stemme_navn = nominert_2

                with open("stemmer.csv", "a", newline="", encoding="utf-8") as fil:
                    writer = csv.writer(fil)
                    writer.writerow([voter, stemme_navn])
    
        else: # Hvis brukeren skriver inn noe annet enn 1 eller 2
            print("Du er ikke velger, eller så har du allerede stemt")

                
def id_sjekk(bruker):
    return bruker in votes_id


#Kilde: https://youtu.be/KqyZc6uR9QU?si=iv0IS2KaU-IL1Kkz

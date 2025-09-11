nominert_1=input("skriv inn navnet til første nominert: ")
nominert_2=input("skriv inn navnet til andre nominert: ")

#Variabeler for hvem av de nominerte du kan stemme på
nom_1_votes=0
nom_2_votes=0

#en liste med "ID" som du bruker når du stemmer, så det er da 10 stykker som kan stemme
votes_id = [1,2,3,4,5,6,7,8,9,10]

num_of_voter=len(votes_id)

while True:
    if votes_id == []:
        print("Avstemningssesjonen er over")
        if nom_1_votes>nom_2_votes:
            prosent = (nom_1_votes / num_of_voter) * 100
            print(nominert_1,"har vunnet valget","med",prosent,"% stemmer")
            break

        elif nom_1_votes<nom_2_votes:
            prosent = (nom_2_votes / num_of_voter) * 100
            print(nominert_2,"har vunnet valget","med",prosent,"% stemmer")
            break

    else:
        voter=int(input("Skriv inn velger-ID-en din ")) #Her skriver du "IDen" din og hvis du ikke skriver inn en gyldig "ID" eller en ID som allerede er brukt får du ikke stemmet.
        if voter in votes_id:
            print("Du er en velger ")
            votes_id.remove(voter)
            vote = int(input("Legg inn din stemme, 1 eller 2: ")) #Her velger du hvem av de to nominerte di stemmer

            if vote==1:
                nom_1_votes+=1
                print("Takk for at du avga din stemme")

            elif vote==2:
                nom_2_votes+=1
                print("Takk for at du avga din stemme")
    
            else:
                print("Du er ikke velger, eller så har du allerede stemt")
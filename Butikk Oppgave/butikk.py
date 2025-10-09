import sqlite3
 
databasekobling = sqlite3.connect('butikk.db')
c = databasekobling.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS inventar (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    navn TEXT NOT NULL,
    pris REAL NOT NULL,
    antall INTEGER NOT NULL
          
)
""")
databasekobling.commit()
 
# Funksjon for å legge til en vare3@
 
def legg_til_vare():
    navn = input("Skriv inn varenavn: ")
    pris = float(input("Pris: "))
    antall = int(input("Antall: "))
    c.execute(
        "INSERT INTO inventar (navn, pris, antall) VALUES (?, ?, ?)",
        (navn, pris, antall)
    )
    databasekobling.commit()
    print(f"Vare '{navn}' ble lagt til.")
# Funksjon for å vise varer sortert etter pris (dyrest først)
def vis_varer_sortert():
    c.execute("SELECT id, navn, pris, antall FROM inventar ORDER BY pris DESC")
    varer = c.fetchall()
 
    if not varer:
        print("Ingen varer i databasen.")
        return
 
    print("\n Varer sortert fra dyrest til billigst:\n")
    for vare in varer:
        print(f"ID: {vare[0]} | Navn: {vare[1]} | Pris: {vare[2]} | Antall: {vare[3]}")
 
# vare slett funksjon
def slett_vare():
    vare_id = input("Skriv id til varen som skal slettes: ")
    c.execute("DELETE FROM inventar WHERE id = ?", (vare_id,))
    databasekobling.commit()
    print(f"Vare med id {vare_id} ble slettet.")
 
# Hovedmeny
def meny():
    while True:
        print("""
        MENY
        1. Legg til vare
        2. Slett vare
        3. Vis varer sortert (dyrest - billigst)
        q. Avslutt
        """)
        valg = input("Velg et alternativ: ").strip()
 
        if valg == "1":
            legg_til_vare()
        elif valg == "2":
            slett_vare()
        elif valg == "3":
            vis_varer_sortert()
        elif valg.lower() == "q":
            print("Avslutter programmet...")
            break
        else:
            print("Ugyldig valg, prøv igjen.")
meny()
databasekobling.close()
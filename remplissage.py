"""Approche modulaire et testable pour gérer une base de donnée SQLite"""


import sqlite3, random
from datetime import datetime, timedelta



# Fonction pour générer des dates aléatoires dans une plage donnée
class BaseLogement:
    def __init__(self, db_name="logement.db"):
        self.db_name = db_name

    
    # ouverture/initialisation de la base de donnee 
    def connect(self):
        self.conn = sqlite3.connect('logement.db')
        self.conn.row_factory = sqlite3.Row
        self.cursor = self.conn.cursor()

    def close(self):
        # fermeture
        self.conn.commit()
        self.conn.close()


    @staticmethod
    def random_date(start, end):
        delta = end - start
        random_days = random.randint(0, delta.days)
        return start + timedelta(days=random_days)

    # Ajout de mesures
    def insert_mesures(self, capteurs, start_date, end_date, n=5):
        for capteur_id in capteurs:
            for _ in range(n):  
                valeur = round(random.uniform(10, 50), 2)  # Valeur aléatoire entre 10 et 50
                date = self.random_date(start_date, end_date)
                self.cursor.execute(
                    "INSERT INTO mesure (valeur, date_insertion, id_capteur) VALUES (?, ?, ?)",
                    (valeur, date, capteur_id),
                )

    # Ajout de factures
    def insert_factures(self, logements, types_factures, start_date, end_date, n=4):
        for logement in logements:
            for _ in range(n): 
                type_facture = random.choice(types_factures)
                montant = round(random.uniform(20, 100), 2)  # Montant aléatoire entre 20 et 100
                valeur_consomme = round(random.uniform(10, 50), 2)  # Valeur consommée entre 10 et 50
                date_facture = self.random_date(start_date, end_date)
                self.cursor.execute(
                    "INSERT INTO facture (type_facture, date_facture, montant, valeur_consommee, id_logement) VALUES (?, ?, ?, ?, ?)",
                    (type_facture, date_facture, montant, valeur_consomme, logement),
                )


if __name__=="__main__":
    db_manager = BaseLogement()
    db_manager.connect()

    #Remplissage de la base de données
    db_manager.insert_mesures(
        capteurs = [1, 2],
        start_date = datetime(2023, 1, 1),
        end_date = datetime (2023, 12, 31),
    )
    db_manager.insert_factures(
        logements = ["7 rue Larue"],
        types_factures = ["Eau", "Electricite", "Dechets", "Gaz"],
        start_date = datetime(2023, 1, 1),
        end_date = datetime(2023, 12, 31,)
    )
    db_manager.close()




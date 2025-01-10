import unittest
import sqlite3
from remplissage import BaseLogement
from datetime import datetime



class TestBaseLogement(unittest.TestCase):
    def setUp(self):
        self.db_manager = BaseLogement(":memory:")
        self.db_manager.connect()

        self.db_manager.cursor.execute("DROP TABLE IF EXISTS mesure")
        self.db_manager.cursor.execute("DROP TABLE IF EXISTS facture")


        self.db_manager.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS mesure (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                valeur REAL,
                date_insertion TEXT,
                id_capteur INTEGER
            )
            """
        )
        self.db_manager.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS facture (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type_facture TEXT,
                date_facture TEXT,
                montant REAL,
                valeur_consommee REAL,
                id_logement TEXT
            )
            """
        )

    def tearDown(self):
        self.db_manager.close()

    def test_random_date(self):
        start = datetime(2023, 1, 1)
        end = datetime(2023, 12, 31)
        date = self.db_manager.random_date(start, end)
        self.assertTrue(start <= date <= end)

    def test_insert_mesures(self):
        self.db_manager.insert_mesures(
            capteurs=[1, 2],
            start_date=datetime(2023, 1, 1),
            end_date=datetime(2023, 12, 31),
            n=3,
        )
        self.db_manager.cursor.execute("SELECT COUNT(*) as count FROM mesure")
        count = self.db_manager.cursor.fetchone()["count"]
        self.assertEqual(count, 6)

    def test_insert_factures(self):
        self.db_manager.insert_factures(
            logements=["7 rue Larue"],
            types_factures=["Eau", "Electricité"],
            start_date=datetime(2023, 1, 1),
            end_date=datetime(2023, 12, 31),
            n=2,
        )
        self.db_manager.cursor.execute("SELECT COUNT(*) as count FROM facture")
        count = self.db_manager.cursor.fetchone()["count"]
        self.assertEqual(count, 2)


if __name__ == "__main__":
    unittest.main()
        
-- Suppression des tables si elles existent
DROP TABLE IF EXISTS logement;
DROP TABLE IF EXISTS piece;
DROP TABLE IF EXISTS capteur_actionneur;
DROP TABLE IF EXISTS mesure;
DROP TABLE IF EXISTS type_capteur_actionneur;
DROP TABLE IF EXISTS facture;

-- Création des tables

-- Table logement
CREATE TABLE logement (
    adresse TEXT PRIMARY KEY,
    numero_tel TEXT,
    adresse_ip TEXT,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);



-- Table piece
CREATE TABLE piece (
    id_piece INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT,
    coordonnes TEXT,
    id_logement TEXT,
    FOREIGN KEY (id_logement) REFERENCES logement(adresse)
);



-- Table capteur_actionneur
CREATE TABLE capteur_actionneur (
    id_capteur INTEGER PRIMARY KEY AUTOINCREMENT,
    type_capteur_actionneur INTEGER,
    reference_commerciale TEXT,
    id_piece INTEGER,
    port_communication TEXT,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (type_capteur_actionneur) REFERENCES type_capteur_actionneur(id_type),
    FOREIGN KEY (id_piece) REFERENCES piece(id_piece)
);



-- Table mesure
CREATE TABLE mesure (
    id_mesure INTEGER PRIMARY KEY AUTOINCREMENT,
    valeur FLOAT,
    date_insertion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    id_capteur INTEGER,
    FOREIGN KEY (id_capteur) REFERENCES capteur_actionneur(id_capteur)
);



-- Table type_capteur_actionneur
CREATE TABLE type_capteur_actionneur (
    id_type INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_type TEXT,
    unite_mesure TEXT,
    plage_precision TEXT
);



-- Table facture
CREATE TABLE facture (
    id_facture INTEGER PRIMARY KEY AUTOINCREMENT,
    type_facture TEXT,
    date_facture DATE,
    montant FLOAT,
    valeur_consommee FLOAT,
    id_logement TEXT,
    FOREIGN KEY (id_logement) REFERENCES logement(adresse)
);





-- Insertion des données

-- Ajout d'un logement
INSERT INTO logement (adresse, numero_tel, adresse_ip)
VALUES ('7 rue Larue', '01 02 03 04 05', '192.168.0.254');



-- Ajout des pièces associées
INSERT INTO piece (nom, coordonnes, id_logement) VALUES 
('Salon', '0,0,0', '7 rue Larue'),
('Cuisine', '1,0,0', '7 rue Larue'),
('Chambre', '0,1,0', '7 rue Larue'),
('Salle de Bain', '1,1,0', '7 rue Larue');



-- Types de capteurs/actionneurs
INSERT INTO type_capteur_actionneur (nom_type, unite_mesure, plage_precision) VALUES
('Temperature', '°C', '0-50'),
('Electricite', 'kWh', '0-200'),
('Luminosite', 'lux', '0-1000'),
('Niveau d eau', 'litres', '0-100');



-- Ajout des capteurs/actionneurs
INSERT INTO capteur_actionneur (type_capteur_actionneur, reference_commerciale, id_piece, port_communication) VALUES
(1, 'TEMP1', 1, 'COM1'),
(2, 'ELEC1', 2, 'COM2');



-- Ajout des mesures
INSERT INTO mesure (valeur, id_capteur) VALUES
(22.5, 1),
(23.0, 1),
(50.5, 2),
(40.8, 2);



-- Ajout des factures
INSERT INTO facture (type_facture, date_facture, montant, valeur_consommee, id_logement) VALUES
('Eau', '2023-01-15', 50.0, 20, '7 rue Larue'),
('Electricite', '2023-02-10', 100.0, 60, '7 rue Larue'),
('Dechets', '2023-03-20', 30.0, 15, '7 rue Larue'),
('Gaz', '2023-04-05', 60.0, 80, '7 rue Larue');


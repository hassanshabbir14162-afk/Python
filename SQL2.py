CREATE TABLE IF NOT EXISTS zoo_animal (
    animal_id  INTERGER PRIMARY KEY,
    name       TEXT     NOT NULL,
    species    TEXT     NOT NULL,
    age_years  INTERGER NOT NULL,
    weight_kg  REAL     NOT NULL
);

INSERT INTO zoo_animals VALUES(1, "lION",     "Big Cat",    5,  190.0);
INSERT INTO zoo_animals VALUES(2, "Tiger",    "Big Cat",    3,  220.0);
INSERT INTO zoo_animals VALUES(3, "Elephant", "Pachyderm",  12, 4500.0);
INSERT INTO zoo_animals VALUES(4, "Giraffe",  "Ungulate",   7,  800.0);
INSERT INTO zoo_animals VALUES(5, "Penguin",  "Bird",       2,  5.0);
INSERT INTO zoo_animals VALUES(6, "Panda",    "Bear",       4,  95.0);
INSERT INTO zoo_animals VALUES(7, "Cheetah",  "Big Cat",    6,  55.0);
INSERT INTO zoo_animals VALUES(8, "Rhino",    "Pachyderm",  9,  2300.0);

SELECT  *  FROM zoo_animal:

SELECT species  FROM zoo_animal;

SELECT DISTINCT species FROM zoo_animal;

SELECT COUNT(DISTINCT species) AS unique_species FROM zoo_animal;
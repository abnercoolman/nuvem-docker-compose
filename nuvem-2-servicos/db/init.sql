CREATE DATABASE infoAnimais;

USE infoAnimais;

CREATE TABLE
  animaisSitioCariri (
    Animal_Nome VARCHAR(50),
    Animal_Raca VARCHAR(50),
    Animal_Peso INT
  );

INSERT INTO
  animaisSitioCariri (Animal_Nome, Animal_Raca, Animal_Peso)
VALUES
  ('Mimosa', 'Nelore', 350),
  ('Delegado', 'Nelore', 450),
  ('Adelaide', 'Angus', 390),
  ('Milka', 'Angus', 470);
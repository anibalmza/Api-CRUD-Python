CREATE DATABASE sistema;
USE sistema;

-- diseño
CREATE TABLE personas  (
    id INT NOT NULL AUTO_INCREMENT,
    apellido VARCHAR(50) NOT NULL,
    nombre VARCHAR(50) NOT NULL,
    dni VARCHAR(11) NOT NULL,
    PRIMARY KEY(id)
)
;

-- ingresar datos
INSERT INTO personas
    (apellido, nombre, dni)
VALUES
    ('ARANCIBIA', 'PABLO', '20567990'),
    ('BARRIOS', 'JOSE', '22444888'),
    ('CABRERA', 'ALBERTO', '11333555'),
    ('DOMINGUEZ', 'DANTE', '12342865'),
    ('ESTRELLA', 'ANTONIO', '28234555'),
    ('FERNANDEZ', 'PASCUAL', '32343888'),
    ('GARAY', 'ANDRES', '40567909'),
    ('HERRERA', 'MARTIN', '42353828')
;
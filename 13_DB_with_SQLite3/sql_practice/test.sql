INSERT INTO contacts
VALUES ("Salman", "Saeed", "123456", "sal@man.com");

SELECT first_name, phone
FROM contacts;

CREATE TABLE contacts
(
    first_name TEXT,
    last_name  TEXT,
    phone      INTEGER,
    email      TEXT
);

DROP TABLE contacts;
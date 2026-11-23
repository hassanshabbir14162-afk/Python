CREATE TABLE IF NOT EXISTS book(
    book_id   INTERGER PRIMARY KEY,
    title     TEXT    NOT NULL,
    genre     TEXT    NOT NULL,
    rating    TEXT    NOT NULL,
    pages     TEXT    NOT NULL,
    pub_year  TEXT    NOT NULL
);

INSERT INTO book VALUES(1, "Dragon Quest",   "Fantasy",   9.2, 312, 2021)
INSERT INTO book VALUES(2, "Code Wizards",   "Sci-Fi",    8.5, 280, 2024)
INSERT INTO book VALUES(3, "Ocean Deep",     "Adventure", 6.5, 355, 2018)
INSERT INTO book VALUES(4, "Star Rangers",   "Sci-Fi",    9.6, 412, 2022)
INSERT INTO book VALUES(5, "Forest Secrets", "Fantasy",   9.9, 188, 2016)
INSERT INTO book VALUES(6, "Robot city",     "Sci-Fi",    7.5, 476, 2023)
INSERT INTO book VALUES(7, "Time Jumpers",   "Adventure", 7.2, 357, 2025)
INSERT INTO book VALUES(8, "Robot city",     "SCI-Fi",    8.8, 295, 2020)

SELECT * FROM book;

SELECT title, rating FROM book ORDER BY rating ASC;

SELECT title, rating FROM book ORDER BY rating DESC;

SELECT title, genre, rating FROM book ORDER BY genre ASC, rating DESC;

SELECT title, rating FROM book ORDER BY rating DESC LIMIT 3;
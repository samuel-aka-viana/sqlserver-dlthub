-- Create tables in master database
CREATE TABLE Authors (
    AuthorID INT PRIMARY KEY,
    Name NVARCHAR(100)
);

INSERT INTO Authors (AuthorID, Name)
VALUES (1, 'Stephen King'), (2, 'Isaac Asimov');

CREATE TABLE Books (
    BookID INT PRIMARY KEY,
    Title NVARCHAR(200),
    AuthorID INT,
    FOREIGN KEY (AuthorID) REFERENCES Authors(AuthorID)
);

INSERT INTO Books (BookID, Title, AuthorID)
VALUES (1, 'The Shining', 1), (2, 'Foundation', 2);
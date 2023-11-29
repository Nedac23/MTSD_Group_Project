CREATE TABLE `books` (
  `ISBN` varchar(14) NOT NULL,
  `Title` varchar(50) DEFAULT NULL,
  `Author` varchar(50) DEFAULT NULL,
  `Genre` varchar(50) DEFAULT NULL,
  `Pages` int(4) DEFAULT NULL,
  `ReleaseDate` varchar(50) DEFAULT NULL,
  `Stock` int(4) DEFAULT NULL
);

INSERT INTO `books` (`ISBN`, `Title`, `Author`, `Genre`, `Pages`,`ReleaseDate`,`Stock`) VALUES
('978-0156028356', 'The Color Purple', 'Alice Walker', 'Epistolary', 304, '1982', 4),
('978-0307265432', 'The Road', 'Cormac McCarthy', 'Post apocalyptic fiction', 287,'September 26 2006', 1),
('978-0312424404', 'Gilead', 'Marilynne Robinson', 'Novel', 247, 'November 4, 2004', 7),
('978-0446310789', 'To Kill a Mockingbird', 'Harper Lee', 'Southern Gothic', 336, 'July 11, 1960', 12),
('978-0451524935', '1984', 'George Orwell', 'Dystopian', 328, 'June 8, 1949', 3),
('978-1400033416', 'Beloved', 'Toni Morrison', 'American Literature', 324, 'September 1987', 90),
('978-1501156748', 'Misery', 'Stephen King', 'Psychological Horror', 310, 'June 8, 1987', 0);

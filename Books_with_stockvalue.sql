CREATE TABLE `books` (
  `ISBN` varchar(14) NOT NULL,
  `Title` varchar(50) DEFAULT NULL,
  `Author` varchar(50) DEFAULT NULL,
  `Year` int(4) DEFAULT NULL,
  `Genre` varchar(50) DEFAULT NULL,
  `Num` int(4) DEFAULT NULL
);

INSERT INTO `books` (`ISBN`, `Title`, `Author`, `Year`, `Genre`,`Num`) VALUES
('978-0156028356', 'The Color Purple', 'Alice Walker', 1982, 'Epistolary', 4),
('978-0307265432', 'The Road', 'Cormac McCarthy', 2006, 'Post apocalyptic fiction', 1),
('978-0312424404', 'Gilead', 'Marilynne Robinson', 2004, 'Novel', 7),
('978-0446310789', 'To Kill a Mockingbird', 'Harper Lee', 1960, 'Southern Gothic', 12),
('978-0451524935', '1984', 'George Orwell', 1949, 'Dystopian', 3),
('978-1400033416', 'Beloved', 'Toni Morrison', 1987, 'American Literature', 90),
('978-1501156748', 'Misery', 'Stephen King', 1987, 'Psychological Horror', 0);

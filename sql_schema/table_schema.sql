CREATE TABLE stations
(
    ID  INT PRIMARY KEY,
    Fwy INT DEFAULT NULL,
    Dir VARCHAR(3) DEFAULT NULL,
    District INT DEFAULT NULL,
    County INT DEFAULT NULL,
    City FLOAT DEFAULT NULL,
    State_PM FLOAT DEFAULT NULL,
    Abs_PM FLOAT DEFAULT NULL,
    Latitude FLOAT DEFAULT NULL,
    Longitude FLOAT DEFAULT NULL,
    Length FLOAT DEFAULT NULL,
    Type VARCHAR(3) DEFAULT NULL,
    Lanes INT DEFAULT NULL,
    Name VARCHAR(20) DEFAULT NULL,
    User_ID_1 VARCHAR(20) DEFAULT NULL,
    User_ID_2 VARCHAR(20) DEFAULT NULL,
    User_ID_3 VARCHAR(20) DEFAULT NULL,
    User_ID_4 VARCHAR(20) DEFAULT NULL
)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
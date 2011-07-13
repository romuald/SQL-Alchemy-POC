CREATE DATABASE IF NOT EXISTS main_db;
USE main_db;

DROP TABLE IF EXISTS Domain_;
CREATE TABLE Domain_ (
    domain_id INT UNSIGNED AUTO_INCREMENT,
    owner_id VARCHAR(255) NOT NULL,
    fqdn VARCHAR(255) NOT NULL,
    date_end DATETIME,
    piapia VARCHAR(32),

    PRIMARY KEY(domain_id)
) ENGINE=InnoDb;


DROP TABLE IF EXISTS Owner;
CREATE TABLE Owner (
    id INT UNSIGNED AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,

    PRIMARY KEY(id)
) ENGINE=Innodb;

INSERT INTO Owner VALUES( 1, "Romuald", "romuald@invalid.net");
INSERT INTO Domain_ VALUES( 1, "data.net", 1, NOW() + INTERVAL 42 WEEK, "zz++");

CREATE DATABASE IF NOT EXISTS second_db;
use second_db;

DROP TABLE IF EXISTS domain_;
CREATE TABLE domain_ (
    dom_id INT UNSIGNED,
    fqdn VARCHAR(255) NOT NULL,
    status SMALLINT UNSIGNED,

    PRIMARY KEY(dom_id)
) ENGINE=InnoDb;


INSERT INTO domain_ VALUES( 1 , "data.net", 72);


CREATE TABLE IF NOT EXISTS crimes (
id int NOT NULL AUTO_INCREMENT,
latitude FLOAT (10,6),
longitude FLOAT(10,6),
date DATETIME,
category VARCHAR(50),
description VARCHAR(1000),
updated_at TIMESTAMP,
PRIMARY KEY (id)
);


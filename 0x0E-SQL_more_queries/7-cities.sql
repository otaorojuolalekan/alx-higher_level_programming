-- cities table task 7
CREATE DATABASE 
    IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE
    IF NOT EXISTS cities (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        state_id INT NOT NULL,
        FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
        name VARCHAR(256)
    );

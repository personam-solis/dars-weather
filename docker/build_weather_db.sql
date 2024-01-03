CREATE ROLE postgres with login SUPERUSER PASSWORD 'password';

CREATE TABLE earth_weather_full (
    account_id serial PRIMARY KEY,
    name VARCHAR (50) NOT NULL);
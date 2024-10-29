-- Write a script that lists all cities contained in the database hbtn_0d_usa.
-- 	cities.id: Refers to the id column specifically in the cities table.
-- cities.name: Refers to the name column specifically in the cities table.

SELECT cities.id, cities.name, 
       (SELECT states.name FROM states WHERE states.id = cities.state_id) AS state_name
FROM cities
ORDER BY cities.id ASC;
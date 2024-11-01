-- changes wal_level
ALTER SYSTEM SET wal_level = logical;

-- check wal_level 
select * from pg_settings where name ='wal_level'

-- create table super_heroes
CREATE TABLE public.super_heroes (
	id serial4 NOT NULL,
	"name" varchar(255) NOT NULL,
	secret_identity varchar(255) NOT NULL,
	powers varchar(255) NOT NULL,
	CONSTRAINT super_heroes_pkey PRIMARY KEY (id)
);

-- insert data
INSERT INTO super_heroes ("name", secret_identity, powers)
    VALUES ('SuperMan', 'Clark', 'flight, x-ray vision, strength, heat vision');

-- update data
UPDATE super_heroes SET secret_identity = 'Clark Kent' where id = 1;

-- check Replica Identity 
SELECT CASE relreplident
          WHEN 'd' THEN 'default'
          WHEN 'n' THEN 'nothing'
          WHEN 'f' THEN 'full'
          WHEN 'i' THEN 'index'
       END AS replica_identity
FROM pg_class
WHERE oid = 'super_heroes'::regclass;

-- set Replica Identity
ALTER TABLE super_heroes REPLICA IDENTITY FULL;


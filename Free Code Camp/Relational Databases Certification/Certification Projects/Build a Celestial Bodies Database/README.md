# Build a Universe Database

## Objective

Create a PostgreSQL relational database that represents a simplified universe containing galaxies, stars, planets, moons, and asteroids.

The goal is to practice designing a relational database, creating relationships between tables, inserting data, and using constraints such as primary keys, foreign keys, `UNIQUE`, and `NOT NULL`.

## Database Structure

The database contains five tables:

* `galaxy` — Stores information about galaxies.
* `star` — Stores information about stars and their galaxies.
* `planet` — Stores information about planets and their stars.
* `moon` — Stores information about moons and their planets.
* `asteroid` — Stores information about asteroids and their distance from Earth.

The main relationships are:

```text
Galaxy
   ↓
Star
   ↓
Planet
   ↓
Moon
```

Asteroids are stored independently.

## Data

The database contains:

* 6 galaxies
* 6 stars
* 12 planets
* 20 moons
* 3 asteroids

Some examples include:

```text
Galaxy: Milky Way

Star: Sun

Planets:
- Earth
- Mercury
- Venus
- Mars
- Jupiter
- Saturn
- Uranus
- Neptune

Moons:
- Moon
- Phobos
- Deimos
- Io
- Europa
- Ganymede
- Callisto
```

## Concepts Practiced

* PostgreSQL
* Relational databases
* Creating databases and tables
* Primary keys
* Foreign keys
* One-to-many relationships
* `UNIQUE` constraints
* `NOT NULL` constraints
* Boolean values
* Integer and text data types
* Sequences
* `INSERT`
* `SELECT`
* `JOIN`
* Database normalization

## Example Queries

Find all planets:

```sql
SELECT *
FROM planet;
```

Find the moons of Jupiter:

```sql
SELECT moon.name
FROM moon
JOIN planet
ON moon.planet_id = planet.planet_id
WHERE planet.name = 'Jupiter';
```

Find the star of Earth:

```sql
SELECT star.name
FROM planet
JOIN star
ON planet.star_id = star.star_id
WHERE planet.name = 'Earth';
```

## Technologies

* PostgreSQL
* SQL
* FreeCodeCamp

## Project

This project was developed as part of the **FreeCodeCamp Relational Database Certification** to practice SQL and relational database design.

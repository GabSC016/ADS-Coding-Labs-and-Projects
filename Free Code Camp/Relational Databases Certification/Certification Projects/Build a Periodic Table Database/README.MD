# Build a Periodic Table Database

## Objective

Create a PostgreSQL relational database that represents chemical elements and their physical properties.

The goal of the project is to practice relational database design, creating relationships between tables, inserting and updating data, using SQL queries, and applying constraints such as primary keys, foreign keys, `UNIQUE`, and `NOT NULL`.

## Database Structure

The database contains three tables:

* `elements` — Stores information about chemical elements, including their atomic number, symbol, and name.
* `properties` — Stores physical properties of each element, including atomic mass, melting point, boiling point, and element type.
* `types` — Stores the different classifications of elements, such as nonmetals, metals, and metalloids.

The main relationships are:

```text
Types
  ↓
Properties
  ↓
Elements
```

Each element has a set of physical properties, and each property record is associated with an element type.

## Data

The database contains:

* 10 chemical elements
* 10 property records
* 3 element types

Some examples include:

```text
Element: Hydrogen (H)
Atomic Number: 1
Type: nonmetal
Atomic Mass: 1.008 amu
Melting Point: -259.1 °C
Boiling Point: -252.9 °C
```

```text
Element: Lithium (Li)
Atomic Number: 3
Type: metal
Atomic Mass: 6.94 amu
Melting Point: 180.54 °C
Boiling Point: 1342 °C
```

```text
Element: Boron (B)
Atomic Number: 5
Type: metalloid
Atomic Mass: 10.81 amu
Melting Point: 2075 °C
Boiling Point: 4000 °C
```

The database includes the following elements:

```text
Hydrogen (H)
Helium (He)
Lithium (Li)
Beryllium (Be)
Boron (B)
Carbon (C)
Nitrogen (N)
Oxygen (O)
Fluorine (F)
Neon (Ne)
```

## Concepts Practiced

* PostgreSQL
* Relational databases
* Creating databases and tables
* Primary keys
* Foreign keys
* One-to-one relationships
* `UNIQUE` constraints
* `NOT NULL` constraints
* Integer, numeric, and text data types
* Sequences
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* `JOIN`
* Database normalization
* Bash scripting
* Command-line PostgreSQL
* Passing arguments to Bash scripts
* Conditional statements in Bash

## Bash Script

The project also includes a Bash script that allows users to search for an element using:

* Atomic number
* Chemical symbol
* Element name

Example:

```bash
./element.sh 1
```

Output:

```text
The element with atomic number 1 is Hydrogen (H). It's a nonmetal, with a mass of 1.008 amu. Hydrogen has a melting point of -259.1 celsius and a boiling point of -252.9 celsius.
```

The script uses PostgreSQL queries to retrieve information from the database and combines the results into a formatted response.

## Example Queries

Find all elements:

```sql
SELECT *
FROM elements;
```

Find an element by its atomic number:

```sql
SELECT *
FROM elements
WHERE atomic_number = 1;
```

Find the properties of Hydrogen:

```sql
SELECT *
FROM properties
WHERE atomic_number = 1;
```

Find the type of an element:

```sql
SELECT types.type
FROM types
INNER JOIN properties
USING(type_id)
WHERE properties.atomic_number = 1;
```

Find an element together with its properties and type:

```sql
SELECT elements.name,
       elements.symbol,
       properties.atomic_mass,
       properties.melting_point_celsius,
       properties.boiling_point_celsius,
       types.type
FROM elements
JOIN properties
ON elements.atomic_number = properties.atomic_number
JOIN types
ON properties.type_id = types.type_id;
```

## Technologies

* Bash
* PostgreSQL
* SQL
* Git
* FreeCodeCamp

## Project

This project was developed as part of the **FreeCodeCamp Relational Database Certification**.

The project was completed successfully and demonstrates practical knowledge of PostgreSQL, relational database design, SQL queries, foreign keys, constraints, database normalization, and Bash scripting.

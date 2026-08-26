# World Cup Database

## Objective

Create a PostgreSQL relational database that stores information about World Cup games from the final three rounds of the 2014 and 2018 tournaments.

The goal is to practice designing a relational database, creating relationships between tables, inserting data from a CSV file using a Bash script, and querying the database using SQL.

The project also practices primary keys, foreign keys, `UNIQUE`, `NOT NULL`, `JOIN`, aggregate functions, and Bash scripting.

## Database Structure

The database is named `worldcup` and contains two tables:

* `teams` — Stores information about the national teams.
* `games` — Stores information about World Cup games, including the year, round, teams involved, and goals scored.

The main relationships are:

```text
teams
  ↑
  │
winner_id
  │
games
  │
opponent_id
  │
  ↓
teams
```

The `games` table references the `teams` table twice:

* `winner_id` — References the winning team.
* `opponent_id` — References the opposing team.

## Data

The database contains:

* 24 unique teams
* 32 games
* Games from the 2014 and 2018 World Cups
* Games from the final three rounds: Eighth-Final, Quarter-Final, Semi-Final, Final, and Third Place

Some examples of teams include:

```text
France
Croatia
Belgium
England
Germany
Argentina
Brazil
Netherlands
Spain
Portugal
```

Examples of games include:

```text
2018 — Final
France 4 x 2 Croatia

2018 — Third Place
Belgium 2 x 0 England

2014 — Final
Germany 1 x 0 Argentina
```

## Concepts Practiced

* PostgreSQL
* SQL
* Relational databases
* Creating databases and tables
* Primary keys
* Foreign keys
* One-to-many relationships
* `UNIQUE` constraints
* `NOT NULL` constraints
* `SERIAL`
* Integer and text data types
* `INSERT`
* `SELECT`
* `WHERE`
* `INNER JOIN`
* `UNION ALL`
* `DISTINCT`
* `COUNT`
* `SUM`
* `AVG`
* `MAX`
* `ROUND`
* `LIKE`
* Database normalization
* Bash scripting
* Reading CSV files
* Bash variables
* `while` loops
* `IFS`
* PostgreSQL queries from Bash

## Bash Scripts

### `insert_data.sh`

The `insert_data.sh` script reads the `games.csv` file and inserts the teams and games into the PostgreSQL database.

The script:

1. Reads the CSV file while skipping the header.
2. Extracts the winner and opponent from each game.
3. Checks whether each team already exists.
4. Inserts new teams into the `teams` table.
5. Retrieves the corresponding `team_id`.
6. Inserts each game into the `games` table using the correct team IDs.

The script also supports the FreeCodeCamp test database through the `test` argument:

```bash
./insert_data.sh test
```

## Database Queries

The `queries.sh` script contains SQL queries that retrieve information from the database.

Some queries calculate statistics such as:

```sql
SELECT SUM(winner_goals) FROM games;
```

Total goals scored by both teams:

```sql
SELECT SUM(winner_goals + opponent_goals) FROM games;
```

Average goals scored by winning teams:

```sql
SELECT AVG(winner_goals) FROM games;
```

Maximum goals scored by one team in a single game:

```sql
SELECT MAX(winner_goals) FROM games;
```

The project also uses `INNER JOIN` to connect games with their corresponding teams.

For example, finding the winner of the 2018 tournament:

```sql
SELECT name
FROM teams
INNER JOIN games
ON games.winner_id = teams.team_id
WHERE round = 'Final' AND year = 2018;
```

Finding teams that played in the 2014 Eighth-Final round:

```sql
SELECT name
FROM games
INNER JOIN teams
ON games.winner_id = teams.team_id
WHERE games.year = 2014 AND games.round = 'Eighth-Final'

UNION ALL

SELECT name
FROM games
INNER JOIN teams
ON games.opponent_id = teams.team_id
WHERE games.year = 2014 AND games.round = 'Eighth-Final';
```

## Technologies

* PostgreSQL
* SQL
* Bash
* Linux
* FreeCodeCamp

## Project Files

```text
worldcup/
├── games.csv
├── worldcup.sql
├── insert_data.sh
└── queries.sh
```

* `games.csv` — Source data containing the World Cup games.
* `worldcup.sql` — PostgreSQL database dump used to recreate the database.
* `insert_data.sh` — Bash script responsible for inserting teams and games.
* `queries.sh` — Bash script containing SQL queries for analyzing the data.


## Project

This project was developed as part of the **FreeCodeCamp Relational Database Certification** to practice PostgreSQL, SQL queries, relational database design, Bash scripting, data insertion, and database relationships.

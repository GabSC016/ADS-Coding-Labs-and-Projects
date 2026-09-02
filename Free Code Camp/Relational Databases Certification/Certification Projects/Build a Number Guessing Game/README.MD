# Number Guessing Game

A command-line number guessing game developed in **Bash** as part of the freeCodeCamp Relational Database certification.

The program generates a random number between **1 and 1000** and challenges the user to guess it. Player information and game statistics are stored in a **PostgreSQL** database.

## Features

* Generates a random secret number between 1 and 1000.
* Requests a username when the game starts.
* Identifies returning players.
* Stores player information in PostgreSQL.
* Tracks the total number of games played.
* Tracks the player's best game based on the fewest guesses.
* Provides hints when the guess is too high or too low.
* Validates that guesses are integers.
* Counts the number of guesses made in each game.

## Technologies

* **Bash**
* **PostgreSQL**
* **Git**
* **psql**

## Database

The project uses a PostgreSQL database called `number_guess`.

### `game_info`

| Column         | Type          | Description                     |
| -------------- | ------------- | ------------------------------- |
| `user_id`      | `integer`     | Unique identifier for each user |
| `username`     | `varchar(22)` | Player's username               |
| `games_played` | `integer`     | Total number of games played    |
| `best_game`    | `integer`     | Fewest guesses needed to win    |

The database dump is included in the project as `number_guess.sql` and can be used to recreate the database.

## How It Works

When the script starts, the user is asked to enter a username:

```text
Enter your username:
```

If the username has not been registered before:

```text
Welcome, Gabs! It looks like this is your first time here.
```

If the username already exists:

```text
Welcome back, Gabs! You have played 5 games, and your best game took 13 guesses.
```

The game then asks the user to guess the secret number:

```text
Guess the secret number between 1 and 1000:
```

The player receives hints depending on the guess:

```text
It's lower than that, guess again:
```

or:

```text
It's higher than that, guess again:
```

Invalid input is handled with:

```text
That is not an integer, guess again:
```

When the player guesses correctly:

```text
You guessed it in 13 tries. The secret number was 542. Nice job!
```

## Project Structure

```text
number_guessing_game/
├── number_guess.sh
├── number_guess.sql
└── README.md
```

## Running the Project

Make sure PostgreSQL is running and the `number_guess` database has been created.

Give the script executable permission:

```bash
chmod +x number_guess.sh
```

Run the game:

```bash
./number_guess.sh
```

The script connects to PostgreSQL using:

```bash
PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"
```

## Restoring the Database

If the database needs to be recreated from the dump:

```bash
psql -U postgres < number_guess.sql
```

## Git

This project was developed using Git with incremental commits documenting the development process.

The repository was completed on the `main` branch with a clean working tree.

## Project Requirements

This project was created to practice:

* Bash scripting
* Conditional statements
* Loops
* Regular expressions
* Variables
* Random number generation
* PostgreSQL queries
* CRUD operations
* Bash and PostgreSQL integration
* Git version control

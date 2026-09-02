#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=number_guess -t --no-align -c"

# input username
echo "Enter your username:"
read USERNAME

MAIN_QUERY=$($PSQL "SELECT username, games_played, best_game FROM game_info WHERE username='$USERNAME'")

# if has't played
if [[ -z $MAIN_QUERY ]]
then
  echo "Welcome, $USERNAME! It looks like this is your first time here."
  INSERT=$($PSQL "INSERT INTO game_info(username) VALUES('$USERNAME');")

# if has played
else
  echo "$MAIN_QUERY" | while IFS="|" read USERNAME GAMES_PLAYED BEST_GAME
  do
    echo "Welcome back, $USERNAME! You have played $GAMES_PLAYED games, and your best game took $BEST_GAME guesses."
  done
fi

# The game
SECRET_NUMBER=$((RANDOM % 1000 + 1))
NUMBER_OF_GUESSES=1

echo "Guess the secret number between 1 and 1000:"
read GUESS

while [[ $GUESS -ne $SECRET_NUMBER ]] 
do
  if [[ ! $GUESS =~ ^[0-9]+$ ]]
  then
    echo "That is not an integer, guess again:"
  else
    if [[ $GUESS -gt $SECRET_NUMBER ]]
    then
      echo "It's lower than that, guess again:"
    else
      echo "It's higher than that, guess again:"
    fi
  fi
  read GUESS
  ((NUMBER_OF_GUESSES++))
done

NEW_QUERY=$($PSQL "SELECT username, games_played, best_game FROM game_info WHERE username='$USERNAME'")

echo "$NEW_QUERY" | while IFS="|" read USERNAME GAMES_PLAYED BEST_GAME
do
  # UPDATE GAMES PLAYED

  if [[ -z $GAMES_PLAYED ]]
  then
    UPDATE_GP=$($PSQL "UPDATE game_info SET games_played=1 WHERE username='$USERNAME';")
  else
    UPDATE_GP=$($PSQL "UPDATE game_info SET games_played = games_played + 1 WHERE username='$USERNAME';")
  fi

  # UPDATE BEST GAME

  if [[ -z $BEST_GAME ]]
  then
    UPDATE_BG=$($PSQL "UPDATE game_info SET best_game=$NUMBER_OF_GUESSES WHERE username='$USERNAME';")
  else
    if [[ $NUMBER_OF_GUESSES -lt $BEST_GAME ]]
    then
      UPDATE_BG=$($PSQL "UPDATE game_info SET best_game=$NUMBER_OF_GUESSES WHERE username='$USERNAME';")
    fi
  fi
done

echo "You guessed it in $NUMBER_OF_GUESSES tries. The secret number was $SECRET_NUMBER. Nice job!"


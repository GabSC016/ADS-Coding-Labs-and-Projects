#! /bin/bash

if [[ $1 == "test" ]]
then
  PSQL="psql --username=postgres --dbname=worldcuptest -t --no-align -c"
else
  PSQL="psql --username=freecodecamp --dbname=worldcup -t --no-align -c"
fi

# Do not change code above this line. Use the PSQL variable above to query your database.

tail -n +2 games.csv | while IFS=',' read YEAR ROUND WINNER OPPONENT WINNER_GOALS OPPONENT_GOALS
do
  WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE NAME = '$WINNER';")
  if [[ -z $WINNER_ID ]]
  then
    INSERT_WINNER=$($PSQL "INSERT INTO teams (name) VALUES ('$WINNER')")
    WINNER_ID=$($PSQL "SELECT team_id FROM teams WHERE NAME = '$WINNER';")
  fi

  OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE NAME = '$OPPONENT';")
  if [[ -z $OPPONENT_ID ]]
  then
    INSERT_OPPONENT=$($PSQL "INSERT INTO teams (name) VALUES ('$OPPONENT')")
    OPPONENT_ID=$($PSQL "SELECT team_id FROM teams WHERE NAME = '$OPPONENT';")
  fi

  # Insere jogos na tabela
  INSERT_GAMES=$($PSQL "INSERT INTO games (year, round, winner_id, opponent_id, winner_goals, opponent_goals) VALUES ($YEAR, '$ROUND', $WINNER_ID, $OPPONENT_ID, $WINNER_GOALS, $OPPONENT_GOALS);")
done
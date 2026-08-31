#!/bin/bash

PSQL="psql --username=freecodecamp --dbname=periodic_table -t --no-align -c"

# Verifica se há argumento
if [[ -z "$1" ]]
then
  echo Please provide an element as an argument.
  exit
else
  REFERENCE=$1
fi

# Verifica se a referência é o número atomico, simbolo ou nome
if [[ $REFERENCE =~ ^[0-9]+$ ]]
then
  ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE atomic_number = $REFERENCE;")

else
  if [[ ${#REFERENCE} -le 2 ]]
  then 
    ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE symbol = '$REFERENCE';")
  
  else
    ATOMIC_NUMBER=$($PSQL "SELECT atomic_number FROM elements WHERE name = '$REFERENCE';")
  fi
fi

if [[ -z "$ATOMIC_NUMBER" ]]
then
  echo "I could not find that element in the database."
else
  NAME=$($PSQL "SELECT name FROM elements WHERE atomic_number = $ATOMIC_NUMBER;")
  SYMBOL=$($PSQL "SELECT symbol FROM elements WHERE atomic_number = $ATOMIC_NUMBER;")
  MASS=$($PSQL "SELECT atomic_mass FROM properties WHERE atomic_number = $ATOMIC_NUMBER;")
  MELTING_POINT_CELSIUS=$($PSQL "SELECT melting_point_celsius FROM properties WHERE atomic_number = $ATOMIC_NUMBER;")
  BOILING_POINT_CELSIUS=$($PSQL "SELECT boiling_point_celsius FROM properties WHERE atomic_number = $ATOMIC_NUMBER;")
  TYPE=$($PSQL "SELECT types.type FROM types INNER JOIN properties USING(type_id) WHERE properties.atomic_number = $ATOMIC_NUMBER;")

  echo "The element with atomic number $ATOMIC_NUMBER is $NAME ($SYMBOL). It's a $TYPE, with a mass of $MASS amu. $NAME has a melting point of $MELTING_POINT_CELSIUS celsius and a boiling point of $BOILING_POINT_CELSIUS celsius."
fi
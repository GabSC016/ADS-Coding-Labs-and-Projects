# Salon Appointment Scheduler

## Objective

Create a PostgreSQL relational database and a Bash script that simulates a salon appointment scheduling system.

The project allows users to:

* View available salon services.
* Select a service by its ID.
* Enter their phone number.
* Register as a new customer if the phone number is not found.
* Schedule an appointment by providing a preferred time.
* Store customers, services, and appointments in a PostgreSQL database.

The project was developed as part of the **Relational Database** certification on freeCodeCamp.

## Technologies

* Bash
* PostgreSQL
* psql
* SQL
* Linux

## Database Structure

The database is named `salon` and contains three tables:

### `services`

Stores the services offered by the salon.

| Column       | Type        | Description                   |
| ------------ | ----------- | ----------------------------- |
| `service_id` | INTEGER     | Primary key, auto-incremented |
| `name`       | VARCHAR(30) | Name of the service           |

### `customers`

Stores customer information.

| Column        | Type        | Description                   |
| ------------- | ----------- | ----------------------------- |
| `customer_id` | INTEGER     | Primary key, auto-incremented |
| `phone`       | VARCHAR     | Unique customer phone number  |
| `name`        | VARCHAR(30) | Customer name                 |

### `appointments`

Stores scheduled appointments.

| Column           | Type        | Description                         |
| ---------------- | ----------- | ----------------------------------- |
| `appointment_id` | INTEGER     | Primary key, auto-incremented       |
| `customer_id`    | INTEGER     | Foreign key referencing `customers` |
| `service_id`     | INTEGER     | Foreign key referencing `services`  |
| `time`           | VARCHAR(20) | Appointment time                    |

## Services

The database contains the following services:

```text
1) cut
2) color
3) perm
4) style
5) trim
```

## Bash Script

The `salon.sh` script connects to PostgreSQL using `psql` and provides an interactive menu for scheduling appointments.

The main flow is:

1. Display the available services.
2. Ask the user to select a service.
3. Validate the selected service ID.
4. Ask for the customer's phone number.
5. Check whether the customer already exists.
6. If the customer does not exist, ask for their name and create a new customer.
7. Ask for the desired appointment time.
8. Create the appointment in the database.
9. Display a confirmation message.

Example:

```text
~~~~~ MY SALON ~~~~~

Welcome to My Salon, how can I help you?

1) cut
2) color
3) perm
4) style
5) trim

1

What's your phone number?

555-5555

What time would you like your cut, Gabriel?

10:30

I have put you down for a cut at 10:30, Gabriel.
```

## Input Validation

The script validates the service selection using a Bash regular expression to ensure that the entered service ID contains only numbers.

If an invalid or nonexistent service is entered, the user is returned to the main menu and shown the list of services again.

```bash
if [[ ! $SERVICE_ID_SELECTED =~ ^[0-9]+$ ]]
```

The script also checks the database to verify whether the selected service actually exists.

## Customer Management

Customers are identified by their phone number.

If the entered phone number already exists in the `customers` table, the existing customer's information is used.

If the phone number does not exist, the script asks for the customer's name and inserts a new record into the database.

## Appointment Management

Appointments are stored in the `appointments` table using foreign keys to maintain relationships between customers and services.

Each appointment contains:

* Customer ID
* Service ID
* Appointment time

## Files

```text
.
├── salon.sh
├── salon.sql
└── README.md
```

### `salon.sh`

Bash script responsible for interacting with the user and scheduling appointments.

### `salon.sql`

PostgreSQL database dump containing the database structure, tables, constraints, sequences, and data.

### `README.md`

Project documentation.

## Database Relationships

```text
customers
    │
    │ customer_id
    ▼
appointments
    ▲
    │ service_id
    │
services
```

The `appointments` table connects customers and services through foreign keys.

## Project Requirements

* Create a database named `salon`.
* Create `customers`, `appointments`, and `services` tables.
* Use automatically incrementing primary keys.
* Follow the `table_name_id` naming convention.
* Use foreign keys for customer and service relationships.
* Store unique customer phone numbers.
* Store salon services and customer names.
* Store appointment times.
* Provide at least three salon services.
* Create an executable `salon.sh` Bash script.
* Display a numbered list of services.
* Validate service selections.
* Register new customers when necessary.
* Schedule appointments.
* Display a confirmation message after successfully scheduling an appointment.

## Author

Developed as part of the **freeCodeCamp Relational Database** curriculum.
# Debezium Tester Application

## Overview

This application is a WebSocket-based FastAPI project that listens for real-time updates from a PostgreSQL database using Debezium and Kafka. Debezium, an open-source distributed platform, enables change data capture (CDC) to capture row-level changes in databases, allowing applications to respond to those changes instantly. This README provides installation, configuration, and usage details for the application.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Debezium Configuration](#debezium-configuration)
- [Application Configuration](#application-configuration)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Makefile Commands](#makefile-commands)
- [Documentation](#documentation)
- [License](#license)

## Prerequisites

- **Docker**: Required to run containers for the application and associated services.
- **Docker Compose**: Manages the multi-container environment.
- **Bruno API Client** (optional): Used for creating and managing requests to Debezium connectors.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/debezium-tester-app.git
   cd debezium-tester-app
   ```

2. **Build and Run the Containers**:

   ```bash
   make build
   make up
   ```

   This builds the FastAPI application and starts PostgreSQL, Kafka, Zookeeper, Debezium Connect, and the FastAPI service, exposing configured ports for each service.

## Debezium Configuration

### 1. Change WAL Level in PostgreSQL

To enable logical replication, set the PostgreSQL Write-Ahead Logging (WAL) level to `logical`:

```sql
ALTER SYSTEM SET wal_level = logical;
```

Verify the WAL level:

```sql
SELECT * FROM pg_settings WHERE name = 'wal_level';
```

### 2. Create the `super_heroes` Table

Run the following SQL commands in PostgreSQL to set up the `super_heroes` table for CDC:

```sql
CREATE TABLE public.super_heroes (
    id serial4 NOT NULL,
    "name" varchar(255) NOT NULL,
    secret_identity varchar(255) NOT NULL,
    powers varchar(255) NOT NULL,
    CONSTRAINT super_heroes_pkey PRIMARY KEY (id)
);
```

Insert initial data:

```sql
INSERT INTO super_heroes ("name", secret_identity, powers)
    VALUES ('SuperMan', 'Clark Kent', 'flight, x-ray vision, strength, heat vision');
```

### 3. Set Replica Identity

Set the replica identity of the `super_heroes` table to `FULL` for Debezium to capture detailed row-level changes:

```sql
ALTER TABLE super_heroes REPLICA IDENTITY FULL;
```

### 4. Create the Debezium Source Connector

Use a POST request to create a source connector for the `super_heroes` table. You can use [Bruno](https://usebruno.com) or another API client to send the following JSON configuration:

```json
{
  "name": "source-connector-super-heroes",
  "config": {
    "connector.class": "io.debezium.connector.postgresql.PostgresConnector",
    "database.hostname": "tester_db",
    "database.port": "5432",
    "database.user": "postgres",
    "database.password": "postgres",
    "database.dbname": "postgres",
    "database.server.name": "postgres",
    "table.include.list": "public.super_heroes",
    "plugin.name": "pgoutput",
    "slot.name": "slotheroes",
    "topic.prefix": "cdc-using-debezium-super-heroes"
  }
}
```

## Application Configuration

Key configurations are located in `app/settings.py` and `pyproject.toml`, including:

- **Kafka Host and Topic**: Ensures alignment with Debezium's Kafka topics.
- **Server Metadata**: Customizable in `pyproject.toml` for project name, version, and contact information.

## Usage

1. **Access the Application**:

   - Navigate to `http://localhost:8000` in your browser.
   - Each client receives a unique ID and connects to a WebSocket to receive real-time messages.

2. **WebSocket Messaging**:
   - Clients connect via `/ws/{client_id}`.
   - Database events (create, update, delete) trigger notifications across connected clients.

## Features

- **Real-Time Database Monitoring**: Listens for PostgreSQL changes via Kafka and broadcasts them.
- **WebSocket Notifications**: WebSocket connections distribute messages to all connected clients.
- **User Interface**: Messages display in a chat interface with styles indicating operation type.

## Project Structure

```plaintext
debezium-tester-app/
├── app/
│   ├── internal/
│   │   ├── consumer.py            # Kafka consumer handling
│   │   ├── connection_manager.py   # WebSocket connection manager
│   ├── routes/
│   │   ├── websockets.py           # WebSocket route definitions
│   ├── templates/
│   │   ├── index.html              # Frontend template
│   ├── static/
│   │   ├── script.js               # Client-side WebSocket logic
│   │   ├── styles.css              # UI styling
│   ├── main.py                     # Main FastAPI app entry
│   ├── settings.py                 # Application configurations
├── Dockerfile
├── docker-compose.yaml             # Docker services configuration
├── pyproject.toml                  # Project metadata
├── docs/                           # Documentation directory
│   ├── bruno_requests/             # Bruno requests for API interactions
│   └── queries/                    # Example SQL queries for PostgreSQL setup
```

## Makefile Commands

- **Build the Docker Image**: Builds the application Docker image.

  ```bash
  make build
  ```

- **Start Containers**: Launches the application and associated services in detached mode.

  ```bash
  make up
  ```

- **Run Linter**: Checks for code style issues and fixes them with `ruff`.

  ```bash
  make linter
  ```

- **Format Code**: Applies code formatting with `ruff`.
  ```bash
  make format
  ```

## Documentation

The `/docs` directory contains:

- **bruno_requests/**: A collection of example Bruno requests for setting up and testing Debezium connectors.
- **queries/**: Example SQL queries for configuring PostgreSQL, including table creation and WAL configuration.

These documents provide helpful resources for configuring the application environment and understanding its capabilities.

## License

This project is licensed under the MIT License.

A simple Python (Flask) application that counts visits, connected to a Redis database. The project is fully dockerized and ready for Kubernetes deployment.

## Requirements
- macOS (Apple Silicon)
- OrbStack (or Docker Desktop)
- Docker Compose

## Quick Start (Docker Compose)

The entire application stack (web server and database) is orchestrated using Docker Compose. You no longer need a local Python environment to run it.

### 1. Start the stack
Run the following command in the root directory of the project to start all services in the background:
```bash
docker compose up -d
```
### 2. Access the application
Open your web browser and navigate to:
http://localhost:5000

### 3. Stop the stack
To stop the application and remove the containers, run:

```bash
docker compose down
```
Useful Commands
- `docker compose ps` - List all running containers for this project.

- `docker compose logs -f` - View live, aggregated logs from both the web app and the database.

- `docker compose up -d --build` - Rebuild the web image and restart the containers (use this after modifying app.py).

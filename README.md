# FastAPI Railway Demo

A FastAPI application template configured for deployment to Railway using Docker and GitHub Actions CI/CD. Includes PostgreSQL database integration with SQLAlchemy.

## Features

- FastAPI web application with RESTful API
- PostgreSQL database integration with SQLAlchemy ORM
- Database migrations with Alembic
- Docker containerization
- Automated testing with pytest
- CI/CD deployment to Railway via GitHub Actions
- Support for SQLite local development

## Local Development

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-railway.git
   cd fastapi-railway
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Choose your database:

   **Option A: SQLite (Recommended for development)**
   - Copy the example environment file:
     ```
     cp .env.example .env
     ```
   - By default, it's configured to use SQLite, which requires no additional setup
   
   **Option B: PostgreSQL**
   - Start a PostgreSQL instance:
     ```
     docker run --name postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=fastapi_db -p 5432:5432 -d postgres
     ```
   - Update the `.env` file with PostgreSQL connection details:
     ```
     DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_db
     ```

5. Run database migrations:
   ```
   alembic upgrade head
   ```

6. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

7. Visit http://localhost:8000 in your browser
   - API documentation available at http://localhost:8000/docs

## API Endpoints

- `GET /tasks` - List all tasks
- `POST /tasks` - Create a new task
- `GET /tasks/{task_id}` - Get a task by ID
- `PUT /tasks/{task_id}` - Update a task
- `DELETE /tasks/{task_id}` - Delete a task

## Database Management

This project uses Alembic for database migrations:

- Generate a migration after model changes:
  ```
  alembic revision --autogenerate -m "description"
  ```

- Apply migrations:
  ```
  alembic upgrade head
  ```

## Testing

Run tests using pytest:
```
pytest
```

## Deployment to Railway

This project is configured to deploy to Railway using a Dockerfile. Railway automatically detects the Dockerfile and uses it to build and deploy the application.

### Required Railway Services

1. PostgreSQL Database
   - Railway provides a PostgreSQL database service
   - The app will automatically connect using the DATABASE_URL environment variable provided by Railway

### Manual Deployment

1. Install the Railway CLI:
   ```
   npm i -g @railway/cli
   ```

2. Login to Railway:
   ```
   railway login
   ```

3. Link your project:
   ```
   railway link
   ```

4. Deploy your application:
   ```
   railway up
   ```

### CI/CD Deployment

This repository includes GitHub Actions workflows that automatically deploy to Railway when you push to the main branch.

To set up CI/CD:

1. Create a Railway API token from the Railway dashboard
2. Add the following secrets to your GitHub repository:
   - RAILWAY_TOKEN: Your Railway API token
   - SERVICE_ID: Your Railway service ID (can be found in the service settings on Railway)
3. Push to the main branch to trigger automatic deployment

### Deployment Configuration

The deployment is configured using the following files:

- `Dockerfile`: Defines how to build the Docker container and run migrations before starting the app
- `.github/workflows/deploy.yml`: Defines the GitHub Actions CI/CD pipeline with PostgreSQL testing

## Project Structure

```
├── .github/
│   └── workflows/         # GitHub Actions workflows
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI application
│   ├── config.py          # Configuration and settings
│   ├── database.py        # Database connection
│   ├── models.py          # SQLAlchemy models
│   └── schemas.py         # Pydantic schemas
├── migrations/            # Alembic migrations
│   ├── versions/          # Migration scripts
│   ├── env.py
│   └── script.py.mako
├── tests/
│   ├── __init__.py
│   ├── test_main.py       # Basic API tests
│   └── test_tasks.py      # Task API tests
├── .gitignore
├── alembic.ini            # Alembic configuration
├── Dockerfile             # Docker configuration
├── README.md
└── requirements.txt       # Python dependencies
``` 
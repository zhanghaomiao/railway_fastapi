# FastAPI Railway Demo

A FastAPI application template configured for deployment to Railway using Docker and GitHub Actions CI/CD.

## Features

- FastAPI web application
- Docker containerization
- Automated testing with pytest
- CI/CD deployment to Railway via GitHub Actions

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

4. Run the application:
   ```
   uvicorn app.main:app --reload
   ```

5. Visit http://localhost:8000 in your browser
   - API documentation available at http://localhost:8000/docs

## Testing

Run tests using pytest:
```
pytest
```

## Deployment to Railway

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
2. Add the token as a GitHub secret named `RAILWAY_TOKEN` in your repository settings

## Project Structure

```
├── .github/
│   └── workflows/         # GitHub Actions workflows
├── app/
│   ├── __init__.py
│   └── main.py            # FastAPI application
├── tests/
│   ├── __init__.py
│   └── test_main.py       # Tests for the application
├── .gitignore
├── Dockerfile             # Docker configuration
├── railway.json           # Railway project configuration
├── README.md
└── requirements.txt       # Python dependencies
``` 
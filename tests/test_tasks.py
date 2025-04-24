import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base, get_db
from app.models import Task

# Create in-memory SQLite database for testing
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency to use test database
@pytest.fixture
def override_get_db():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def client(override_get_db):
    def _get_test_db():
        try:
            yield override_get_db
        finally:
            pass
    
    app.dependency_overrides[get_db] = _get_test_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()

def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "Test Description", "completed": False},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["completed"] == False
    assert "id" in data
    assert "created_at" in data

def test_read_tasks(client):
    # Create a task first
    client.post(
        "/tasks/",
        json={"title": "Test Task", "description": "Test Description"},
    )
    
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["title"] == "Test Task"

def test_update_task(client):
    # Create a task first
    response = client.post(
        "/tasks/",
        json={"title": "Original Task", "description": "Original Description"},
    )
    task_id = response.json()["id"]
    
    # Update the task
    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Updated Task", "description": "Updated Description", "completed": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task"
    assert data["description"] == "Updated Description"
    assert data["completed"] == True

def test_delete_task(client):
    # Create a task first
    response = client.post(
        "/tasks/",
        json={"title": "Task to Delete", "description": "Will be deleted"},
    )
    task_id = response.json()["id"]
    
    # Delete the task
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    
    # Verify it's deleted
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404 
import pytest
import requests
from requests.exceptions import RequestException

BASE_URL = "http://localhost:8000/api/v1"

@pytest.fixture(scope="session")
def setup_admin_user():
    """Set up an initial admin user for testing."""
    register_url = f"{BASE_URL}/auth/register"
    admin_payload = {
        "name": "Initial Admin",
        "email": "initial_admin@example.com",
        "password": "admin123",
        "location": "Admin City",
        "is_public": True,
        "is_admin": True
    }
    try:
        response = requests.post(register_url, json=admin_payload, params={"local_kw": "en_US"})
        print(f"Setup admin user response (status {response.status_code}): {response.text}")
        if response.status_code != 200:
            pytest.skip("Failed to set up initial admin user")
        admin_id = response.json().get("id")
        # Verify is_admin
        login_url = f"{BASE_URL}/auth/token"
        login_payload = {"username": "initial_admin@example.com", "password": "admin123"}
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(login_url, data=login_payload, headers=headers)
        if response.status_code != 200:
            pytest.skip("Failed to login initial admin")
        admin_token = response.json().get("access_token")
        # Update is_admin via API (assumes an initial admin exists or use database)
        update_url = f"{BASE_URL}/admin/users/{admin_id}"
        update_payload = {"is_admin": True}
        headers = {"Authorization": f"Bearer {admin_token}", "Content-Type": "application/json"}
        response = requests.put(update_url, json=update_payload, headers=headers)
        if response.status_code != 200:
            # Fallback to database update
            import sqlite3
            conn = sqlite3.connect("D:/odoo_hackathon/Odoo-Hackathon-Bol-tech/backend/skillswap.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET is_admin = 1 WHERE email = ?", ("initial_admin@example.com",))
            conn.commit()
            conn.close()
    except RequestException as e:
        print(f"Setup admin user failed: {str(e)}")
        pytest.skip(f"Skipping tests due to admin setup failure: {str(e)}")

@pytest.fixture(scope="module")
def token():
    """Fixture to register a user and obtain a token."""
    register_url = f"{BASE_URL}/auth/register"
    register_payload = {
        "name": "Test User",
        "email": "test@example.com",
        "password": "password123",
        "location": "Test City",
        "is_public": True
    }
    try:
        response = requests.post(register_url, json=register_payload, params={"local_kw": "en_US"})
        print(f"Register user response (status {response.status_code}): {response.text}")
        response.raise_for_status()
    except RequestException as e:
        print(f"Register user failed: {str(e)}")
        pytest.skip(f"Skipping tests due to registration failure: {str(e)}")
    login_url = f"{BASE_URL}/auth/token"
    login_payload = {
        "username": "test@example.com",
        "password": "password123"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    try:
        response = requests.post(login_url, data=login_payload, headers=headers)
        print(f"Login response (status {response.status_code}): {response.text}")
        response.raise_for_status()
        return response.json().get("access_token")
    except RequestException as e:
        print(f"Login failed: {str(e)}")
        pytest.skip(f"Skipping tests due to login failure: {str(e)}")

@pytest.fixture(scope="module")
def admin_token(setup_admin_user):
    """Fixture to obtain a token for an admin user."""
    login_url = f"{BASE_URL}/auth/token"
    login_payload = {
        "username": "initial_admin@example.com",
        "password": "admin123"
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    try:
        response = requests.post(login_url, data=login_payload, headers=headers)
        print(f"Admin login response (status {response.status_code}): {response.text}")
        response.raise_for_status()
        return response.json().get("access_token")
    except RequestException as e:
        print(f"Admin login failed: {str(e)}")
        pytest.skip(f"Skipping admin tests due to login failure: {str(e)}")

def test_register_user():
    """Test user registration endpoint."""
    url = f"{BASE_URL}/auth/register"
    payload = {
        "name": "Test User 2",
        "email": "test2@example.com",
        "password": "password123",
        "location": "Test City",
        "is_public": True
    }
    response = requests.post(url, json=payload, params={"local_kw": "en_US"})
    print(f"Register user test response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to register user: {response.text}"
    assert response.json().get("email") == "test2@example.com"
    assert response.json().get("name") == "Test User 2"

def test_login(token):
    """Test login endpoint."""
    assert token is not None, "Token was not generated"
    url = f"{BASE_URL}/auth/token"
    payload = {"username": "test@example.com", "password": "password123"}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(url, data=payload, headers=headers)
    print(f"Login test response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to login: {response.text}"
    assert "access_token" in response.json()

def test_get_current_user(token):
    """Test getting current user details."""
    url = f"{BASE_URL}/users/me"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    print(f"Get current user response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to get user: {response.text}"
    assert response.json().get("email") == "test@example.com"
    assert response.json().get("name") == "Test User"

def test_update_user(token):
    """Test updating user details."""
    url = f"{BASE_URL}/users/me"
    payload = {
        "name": "Updated User",
        "email": "test@example.com",
        "location": "New City",
        "is_public": False
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.put(url, json=payload, headers=headers)
    print(f"Update user response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to update user: {response.text}"
    assert response.json().get("name") == "Updated User"
    assert response.json().get("location") == "New City"

def test_create_skill(token):
    """Test skill creation endpoint."""
    url = f"{BASE_URL}/skills/"
    payload = {
        "name": "Python Programming",
        "description": "Expert in Python coding",
        "is_offered": True,
        "availability": "Weekends"
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    print(f"Create skill response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to create skill: {response.text}"
    assert response.json().get("name") == "Python Programming"
    assert response.json().get("is_offered") is True

def test_list_skills():
    """Test listing all skills endpoint."""
    url = f"{BASE_URL}/skills/"
    response = requests.get(url)
    print(f"List skills response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to list skills: {response.text}"
    assert isinstance(response.json(), list)

def test_search_skills():
    """Test searching skills endpoint."""
    url = f"{BASE_URL}/skills/search?query=Python"
    response = requests.get(url)
    print(f"Search skills response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to search skills: {response.text}"
    assert isinstance(response.json(), list)

def test_create_swap(token):
    """Test swap creation endpoint."""
    # Register a second user
    url = f"{BASE_URL}/auth/register"
    payload = {
        "name": "Receiver User",
        "email": "receiver@example.com",
        "password": "password123",
        "location": "Test City",
        "is_public": True
    }
    response = requests.post(url, json=payload, params={"local_kw": "en_US"})
    print(f"Register receiver response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to register receiver: {response.text}"
    receiver_id = response.json().get("id")

    # Create a skill
    url = f"{BASE_URL}/skills/"
    payload = {
        "name": "Test Skill",
        "description": "Test skill description",
        "is_offered": True,
        "availability": "Weekends"
    }
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    response = requests.post(url, json=payload, headers=headers)
    print(f"Create skill response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to create skill: {response.text}"
    skill_id = response.json().get("id")

    # Create a swap
    url = f"{BASE_URL}/swaps/"
    payload = {
        "receiver_id": receiver_id,
        "skill_offered_id": skill_id,
        "skill_wanted_id": skill_id
    }
    response = requests.post(url, json=payload, headers=headers)
    print(f"Create swap response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to create swap: {response.text}"
    assert response.json().get("status") == "pending"
    assert response.json().get("receiver_id") == receiver_id

def test_list_swaps():
    """Test listing all swaps endpoint."""
    url = f"{BASE_URL}/swaps/"
    response = requests.get(url)
    print(f"List swaps response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to list swaps: {response.text}"
    assert isinstance(response.json(), list)

def test_admin_list_users(admin_token):
    """Test admin endpoint to list all users."""
    url = f"{BASE_URL}/admin/users"
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = requests.get(url, headers=headers)
    print(f"Admin list users response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to list users: {response.text}"
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 2

def test_admin_update_user(admin_token):
    """Test admin endpoint to update user details."""
    url = f"{BASE_URL}/admin/users/1"
    payload = {
        "name": "Admin Updated User",
        "email": "updated_admin_user@example.com",  # Use unique email
        "is_admin": False
    }
    headers = {"Authorization": f"Bearer {admin_token}", "Content-Type": "application/json"}
    response = requests.put(url, json=payload, headers=headers)
    print(f"Admin update user response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to update user: {response.text}"
    assert response.json().get("name") == "Admin Updated User"

def test_admin_delete_user(admin_token):
    """Test admin endpoint to delete a user."""
    url = f"{BASE_URL}/admin/users/2"
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = requests.delete(url, headers=headers)
    print(f"Admin delete user response (status {response.status_code}): {response.text}")
    assert response.status_code == 200, f"Failed to delete user: {response.text}"
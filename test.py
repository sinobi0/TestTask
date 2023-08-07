import requests
import pytest

# Positive API tests

def test_get_users(base_url):
    response = requests.get(f"{base_url}/api/users")
    assert response.status_code == 200

def test_get_user(base_url, user_id):
    response = requests.get(f"{base_url}/api/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["data"]["first_name"] == "George"
    assert response.json()["data"]["last_name"] == "Bluth"

# Negative API tests

def test_get_user_not_found(base_url):
    response = requests.get(f"{base_url}/api/users/23")
    assert response.status_code == 404

def test_get_users_invalid_page_number(base_url):
    response = requests.get(f"{base_url}/api/users?page=99")
    assert response.status_code == 404

# Web tests

def test_get_users_web(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    assert "George" in response.text
    assert "Bluth" in response.text

def test_get_user_web(base_url):
    response = requests.get(f"{base_url}/users/2")
    assert response.status_code == 200
    assert "Janet" in response.text
    assert "Weaver" in response.text

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_parameterized(base_url, user_id):
    response = requests.get(f"{base_url}/api/users/{user_id}")
    if response.status_code == 200:
        assert response.json()["data"]["first_name"] == "George"
        assert response.json()["data"]["last_name"] == "Bluth"
    else:
        assert response.status_code == 404

# Fixtures

@pytest.fixture
def base_url():
    return "https://reqres.in"

# Scalable project

def test_new_page_web(base_url):
    response = requests.get(f"{base_url}/new-page")
    assert response.status_code == 404

def test_new_version_api(base_url):
    response = requests.get(f"{base_url}/api/v2/users")
    assert response.status_code == 404
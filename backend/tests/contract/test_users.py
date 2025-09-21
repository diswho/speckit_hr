import pytest
import httpx

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_user():
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/users", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 201
    assert response.json()["email"] == "test@example.com"

@pytest.mark.asyncio
async def test_get_user():
    # This test will require a user to exist. For now, we expect it to fail.
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/users/123")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_user():
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/users/123", json={"email": "new@example.com"})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_user():
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/users/123")
    assert response.status_code == 204

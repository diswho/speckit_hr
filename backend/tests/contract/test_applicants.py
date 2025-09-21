import pytest
import httpx

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_get_applicants():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/applicants")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_applicant():
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/applicants", json={"name": "John Doe", "email": "john.doe@example.com"})
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"

@pytest.mark.asyncio
async def test_get_applicant():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/applicants/123")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_applicant():
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/applicants/123", json={"name": "Jane Doe"})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_applicant():
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/applicants/123")
    assert response.status_code == 204

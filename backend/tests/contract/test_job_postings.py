import pytest
import httpx

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_get_job_postings():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/job-postings")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_job_posting():
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/job-postings", json={"title": "Software Engineer", "description": "..."})
    assert response.status_code == 201
    assert response.json()["title"] == "Software Engineer"

@pytest.mark.asyncio
async def test_get_job_posting():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/job-postings/123")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_job_posting():
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/job-postings/123", json={"title": "Senior Software Engineer"})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_job_posting():
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/job-postings/123")
    assert response.status_code == 204

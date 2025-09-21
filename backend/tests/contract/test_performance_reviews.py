import pytest
import httpx

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_get_performance_reviews():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/performance-reviews")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_performance_review():
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/performance-reviews", json={"employee_id": "123", "reviewer_id": "456"})
    assert response.status_code == 201
    assert response.json()["employee_id"] == "123"

@pytest.mark.asyncio
async def test_get_performance_review():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/performance-reviews/123")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_performance_review():
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/performance-reviews/123", json={"final_score": 10})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_performance_review():
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/performance-reviews/123")
    assert response.status_code == 204

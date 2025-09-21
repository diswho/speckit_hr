import pytest
import httpx

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_get_onboarding_plans():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/onboarding-plans")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

@pytest.mark.asyncio
async def test_create_onboarding_plan():
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/onboarding-plans", json={"name": "New Hire Onboarding"})
    assert response.status_code == 201
    assert response.json()["name"] == "New Hire Onboarding"

@pytest.mark.asyncio
async def test_get_onboarding_plan():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/onboarding-plans/123")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_update_onboarding_plan():
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/onboarding-plans/123", json={"name": "Updated Onboarding Plan"})
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_onboarding_plan():
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/onboarding-plans/123")
    assert response.status_code == 204

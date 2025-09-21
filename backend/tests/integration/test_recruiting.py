import pytest
import httpx

BASE_URL = "http://localhost:8000"

# Placeholder for getting an auth token for an HR Manager
async def get_hr_manager_token():
    # This will be implemented later
    return "fake-hr-manager-token"

@pytest.mark.asyncio
async def test_create_job_posting_as_hr_manager():
    token = await get_hr_manager_token()
    headers = {"Authorization": f"Bearer {token}"}

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{BASE_URL}/job-postings",
            headers=headers,
            json={"title": "New Role", "description": "A great new role"}
        )
        assert response.status_code == 201
        assert response.json()["title"] == "New Role"

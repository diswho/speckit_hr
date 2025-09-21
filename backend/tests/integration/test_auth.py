import pytest
import httpx

BASE_URL = "http://localhost:8000"

@pytest.mark.asyncio
async def test_user_registration_and_login():
    async with httpx.AsyncClient() as client:
        # Register a new user
        register_response = await client.post(
            f"{BASE_URL}/register",
            json={"email": "integration.test@example.com", "password": "password123"}
        )
        assert register_response.status_code == 201

        # Log in with the new user
        login_response = await client.post(
            f"{BASE_URL}/login",
            data={"username": "integration.test@example.com", "password": "password123"}
        )
        assert login_response.status_code == 200
        assert "access_token" in login_response.json()

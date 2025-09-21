# Quickstart: HR Management Web App

**Status**: Completed

This guide provides instructions for setting up the development environment for the HR Management Web App.

## Prerequisites

- Python 3.9+
- Node.js 16+
- PostgreSQL 13+

## Backend Setup (FastAPI)

1.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

2.  **Install dependencies:**
    ```bash
    pip install fastapi uvicorn psycopg2-binary python-jose passlib bcrypt
    ```

3.  **Configure the database:**
    - Create a PostgreSQL database for the application.
    - Set the database connection URL as an environment variable:
      ```bash
      export DATABASE_URL="postgresql://user:password@localhost/hr_app_db"
      ```

4.  **Run the development server:**
    ```bash
    uvicorn main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

## Frontend Setup (React)

1.  **Install dependencies:**
    ```bash
    npm install
    ```

2.  **Configure the API endpoint:**
    - Create a `.env` file in the `frontend` directory.
    - Add the following line to the `.env` file:
      ```
      REACT_APP_API_URL=http://localhost:8000
      ```

3.  **Run the development server:**
    ```bash
    npm start
    ```
    The application will be available at `http://localhost:3000`.

# Tasks: HR Management Web Application

**Input**: Design documents from `C:\Users\phuong\Documents\Workspaces\spec_kit\speckit_hr\specs\001-design-and-develop\`
**Prerequisites**: plan.md, research.md, data-model.md, contracts/openapi.yml, quickstart.md

## Phase 3.1: Setup

- [ ] T001 Create project structure in `backend/` and `frontend/` directories.
- [ ] T002 [P] Initialize FastAPI project in `backend/` with dependencies (fastapi, uvicorn, sqlalchemy, psycopg2-binary).
- [ ] T003 [P] Initialize Next.js TypeScript project in `frontend/` with dependencies (react, react-dom, next, typescript).
- [ ] T004 [P] Configure linting and formatting for the backend (e.g., black, ruff).
- [ ] T005 [P] Configure linting and formatting for the frontend (e.g., eslint, prettier).
- [ ] T006 Setup PostgreSQL database.

## Phase 3.2: Backend - Tests First (TDD)

- [ ] T007 [P] Create contract test for `POST /auth/login` in `backend/tests/contract/test_auth.py`.
- [ ] T008 [P] Create contract test for `GET /job-openings` in `backend/tests/contract/test_job_openings.py`.
- [ ] T009 [P] Create contract test for `POST /job-openings` in `backend/tests/contract/test_job_openings.py`.
- [ ] T010 [P] Create contract test for `GET /job-openings/{id}` in `backend/tests/contract/test_job_openings.py`.
- [ ] T011 [P] Create contract test for `PUT /job-openings/{id}` in `backend/tests/contract/test_job_openings.py`.
- [ ] T012 [P] Create contract test for `POST /applications` in `backend/tests/contract/test_applications.py`.
- [ ] T013 [P] Create contract test for `GET /onboarding-tasks` in `backend/tests/contract/test_onboarding_tasks.py`.
- [ ] T014 [P] Create contract test for `POST /performance-reviews` in `backend/tests/contract/test_performance_reviews.py`.
- [ ] T015 [P] Create integration test for the job application flow in `backend/tests/integration/test_recruiting.py`.
- [ ] T016 [P] Create integration test for the onboarding flow in `backend/tests/integration/test_onboarding.py`.

## Phase 3.3: Backend - Core Implementation

- [ ] T017 [P] Create User model in `backend/src/models/user.py`.
- [ ] T018 [P] Create JobOpening model in `backend/src/models/job_opening.py`.
- [ ] T019 [P] Create Application model in `backend/src/models/application.py`.
- [ ] T020 [P] Create OnboardingTask model in `backend/src/models/onboarding_task.py`.
- [ ] T021 [P] Create PerformanceReview model in `backend/src/models/performance_review.py`.
- [ ] T022 Implement database connection and session management in `backend/src/database.py`.
- [ ] T023 Implement authentication service (`POST /auth/login`) in `backend/src/api/auth.py`.
- [ ] T024 Implement recruiting service (`/job-openings`, `/applications`) in `backend/src/api/recruiting.py`.
- [ ] T025 Implement onboarding service (`/onboarding-tasks`) in `backend/src/api/onboarding.py`.
- [ ] T026 Implement performance review service (`/performance-reviews`) in `backend/src/api/performance.py`.
- [ ] T027 Implement ZKTimeNet integration service in `backend/src/services/zktime_integration.py`.

## Phase 3.4: Frontend - Core Implementation

- [ ] T028 [P] Create basic layout and navigation components in `frontend/src/components/layout/`.
- [ ] T029 [P] Implement login page in `frontend/src/pages/login.tsx`.
- [ ] T030 [P] Implement dashboard page in `frontend/src/pages/dashboard.tsx`.
- [ ] T031 [P] Implement recruiting module pages (job openings, applications) in `frontend/src/pages/recruiting/`.
- [ ] T032 [P] Implement onboarding module pages in `frontend/src/pages/onboarding/`.
- [ ] T033 [P] Implement performance review module pages in `frontend/src/pages/performance/`.
- [ ] T034 [P] Implement API client service to connect to the backend in `frontend/src/services/api.ts`.

## Phase 3.5: Polish

- [ ] T035 [P] Add unit tests for backend services.
- [ ] T036 [P] Add unit tests for frontend components.
- [ ] T037 [P] Write end-to-end tests with Cypress for the user stories in `quickstart.md`.
- [ ] T038 [P] Add comprehensive API documentation.
- [ ] T039 [P] Perform manual testing based on `quickstart.md`.

## Dependencies
- Backend tests (T007-T016) must be completed before backend implementation (T017-T027).
- Backend implementation (T017-T027) must be completed before frontend implementation (T028-T034).
- Core implementation (T017-T034) must be completed before polish (T035-T039).

## Parallel Example
```
# Launch backend contract tests in parallel:
Task: "T007 [P] Create contract test for POST /auth/login in backend/tests/contract/test_auth.py."
Task: "T008 [P] Create contract test for GET /job-openings in backend/tests/contract/test_job_openings.py."
...

# Launch backend model creation in parallel:
Task: "T017 [P] Create User model in backend/src/models/user.py."
Task: "T018 [P] Create JobOpening model in backend/src/models/job_opening.py."
...
```


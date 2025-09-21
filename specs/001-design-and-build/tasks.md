# Tasks: HR Management Web App

**Input**: Design documents from `/specs/001-design-and-build/`
**Prerequisites**: plan.md, research.md, data-model.md, contracts/

## Phase 3.1: Setup
- [X] T001 Create project structure with `backend/` and `frontend/` directories.
- [X] T002 [P] Initialize FastAPI project in `backend/` with dependencies from `quickstart.md`.
- [X] T003 [P] Initialize React project in `frontend/` with dependencies from `quickstart.md`.
- [X] T004 [P] Configure linting (Ruff) and formatting (Black) for the backend.
- [X] T005 [P] Configure linting (ESLint) and formatting (Prettier) for the frontend.

## Phase 3.2: Tests First (TDD) ⚠️ MUST COMPLETE BEFORE 3.3
**CRITICAL: These tests MUST be written and MUST FAIL before ANY implementation**
- [X] T006 [P] Contract test for User API endpoints in `backend/tests/contract/test_users.py`.
- [X] T007 [P] Contract test for Job Posting API endpoints in `backend/tests/contract/test_job_postings.py`.
- [X] T008 [P] Contract test for Applicant API endpoints in `backend/tests/contract/test_applicants.py`.
- [X] T009 [P] Contract test for Onboarding Plan API endpoints in `backend/tests/contract/test_onboarding_plans.py`.
- [X] T010 [P] Contract test for Performance Review API endpoints in `backend/tests/contract/test_performance_reviews.py`.
- [X] T011 [P] Integration test for user registration and login flow in `backend/tests/integration/test_auth.py`.
- [X] T012 [P] Integration test for creating a job posting as an HR Manager in `backend/tests/integration/test_recruiting.py`.

## Phase 3.3: Core Implementation (ONLY after tests are failing)

### Backend
- [ ] T013 [P] Create User model in `backend/src/models/user.py` based on `data-model.md`.
- [ ] T014 [P] Create Job Posting model in `backend/src/models/job_posting.py`.
- [ ] T015 [P] Create Applicant model in `backend/src/models/applicant.py`.
- [ ] T016 [P] Create Onboarding Plan and Task models in `backend/src/models/onboarding.py`.
- [ ] T017 [P] Create Performance Review model in `backend/src/models/performance_review.py`.
- [ ] T018 Create database session management in `backend/src/database.py`.
- [ ] T019 Implement User service in `backend/src/services/user_service.py`.
- [ ] T020 Implement User API endpoints in `backend/src/api/users.py`.
- [ ] T021 Implement Job Posting service and API endpoints in `backend/src/api/job_postings.py`.
- [ ] T022 Implement Applicant service and API endpoints in `backend/src/api/applicants.py`.
- [ ] T023 Implement Onboarding service and API endpoints in `backend/src/api/onboarding.py`.
- [ ] T024 Implement Performance Review service and API endpoints in `backend/src/api/performance_reviews.py`.

### Frontend
- [ ] T025 [P] Setup React Router for navigation.
- [ ] T026 [P] Create a reusable API client service to communicate with the backend.
- [ ] T027 [P] Create a login page in `frontend/src/pages/LoginPage.tsx`.
- [ ] T028 [P] Create a dashboard page in `frontend/src/pages/DashboardPage.tsx`.
- [ ] T029 [P] Create components for the navigation bar and sidebar.
- [ ] T030 [P] Create components for displaying job postings.
- [ ] T031 [P] Create components for the applicant tracking pipeline.

## Phase 3.4: Integration
- [ ] T032 Implement authentication middleware in `backend/src/auth.py` to handle JWTs and RBAC.
- [ ] T033 Integrate authentication middleware with API endpoints.
- [ ] T034 Implement the ZKTimeNet data import as a nightly background task in `backend/src/tasks/zktimenet_import.py`.
- [ ] T035 Connect frontend components to the backend API to fetch and display data.

## Phase 3.5: Polish
- [ ] T036 [P] Add unit tests for services and utility functions in `backend/tests/unit/`.
- [ ] T037 [P] Add unit tests for React components in `frontend/src/components/`.
- [ ] T038 [P] Add API documentation using FastAPI's automatic docs generation.
- [ ] T039 [P] Review and refine the UI for consistency and ease of use.
- [ ] T040 Perform end-to-end manual testing based on the user stories in `spec.md`.

## Parallel Execution Example

```
# Launch setup tasks T002-T005 together:
Task: "[P] Initialize FastAPI project in backend/ with dependencies from quickstart.md."
Task: "[P] Initialize React project in frontend/ with dependencies from quickstart.md."
Task: "[P] Configure linting (Ruff) and formatting (Black) for the backend."
Task: "[P] Configure linting (ESLint) and formatting (Prettier) for the frontend."

# Launch contract test tasks T006-T010 together:
Task: "[P] Contract test for User API endpoints in backend/tests/contract/test_users.py."
Task: "[P] Contract test for Job Posting API endpoints in backend/tests/contract/test_job_postings.py."
...
```

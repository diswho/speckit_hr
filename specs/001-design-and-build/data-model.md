# Data Model: HR Management Web App

**Status**: Completed

This document describes the data models for the key entities in the HR Management Web App.

## 1. User

Represents any individual interacting with the system.

- **`id`**: `UUID` (Primary Key)
- **`email`**: `String` (Unique, Indexed)
- **`hashed_password`**: `String`
- **`name`**: `String`
- **`role`**: `Enum` (HR_MANAGER, DEPARTMENT_HEAD, EMPLOYEE, APPLICANT)
- **`is_active`**: `Boolean` (default: `true`)
- **`created_at`**: `DateTime`
- **`updated_at`**: `DateTime`

**Relationships:**
- A `User` (as a Department Head) can have multiple `Job Postings`.
- A `User` (as an Employee) can have multiple `Onboarding Plans`.
- A `User` (as an Employee) can have multiple `Performance Reviews`.

## 2. Job Posting

Represents a job opening.

- **`id`**: `UUID` (Primary Key)
- **`title`**: `String`
- **`description`**: `Text`
- **`status`**: `Enum` (OPEN, CLOSED, DRAFT)
- **`department_id`**: `UUID` (Foreign Key to `User` where role is DEPARTMENT_HEAD)
- **`created_at`**: `DateTime`
- **`updated_at`**: `DateTime`

**Relationships:**
- Belongs to a `User` (Department Head).
- Has many `Applicants`.

## 3. Applicant

Represents a person who applied for a job.

- **`id`**: `UUID` (Primary Key)
- **`name`**: `String`
- **`email`**: `String`
- **`phone`**: `String`
- **`resume_url`**: `String`
- **`status`**: `Enum` (APPLIED, SCREENING, INTERVIEW, OFFER, HIRED, REJECTED)
- **`job_posting_id`**: `UUID` (Foreign Key to `Job Posting`)
- **`created_at`**: `DateTime`
- **`updated_at`**: `DateTime`

**Relationships:**
- Belongs to a `Job Posting`.

## 4. Onboarding Plan

A set of tasks for a new hire.

- **`id`**: `UUID` (Primary Key)
- **`name`**: `String`
- **`employee_id`**: `UUID` (Foreign Key to `User` where role is EMPLOYEE)
- **`created_at`**: `DateTime`
- **`updated_at`**: `DateTime`

**Relationships:**
- Belongs to a `User` (Employee).
- Has many `Onboarding Tasks`.

## 5. Onboarding Task

A single task within an onboarding plan.

- **`id`**: `UUID` (Primary Key)
- **`title`**: `String`
- **`description`**: `Text`
- **`due_date`**: `Date`
- **`is_completed`**: `Boolean` (default: `false`)
- **`onboarding_plan_id`**: `UUID` (Foreign Key to `Onboarding Plan`)
- **`created_at`**: `DateTime`
- **`updated_at`**: `DateTime`

**Relationships:**
- Belongs to an `Onboarding Plan`.

## 6. Performance Review

A review cycle for an employee.

- **`id`**: `UUID` (Primary Key)
- **`employee_id`**: `UUID` (Foreign Key to `User` where role is EMPLOYEE)
- **`reviewer_id`**: `UUID` (Foreign Key to `User` where role is DEPARTMENT_HEAD or HR_MANAGER)
- **`self_assessment`**: `Text`
- **`reviewer_assessment`**: `Text`
- **`final_score`**: `Integer`
- **`status`**: `Enum` (SCHEDULED, IN_PROGRESS, COMPLETED)
- **`created_at`**: `DateTime`
- **`updated_at`**: `DateTime`

**Relationships:**
- Belongs to a `User` (Employee).
- Belongs to a `User` (Reviewer).

# Data Model

This document describes the data entities for the HR Management Web Application, based on the feature specification.

## 1. User
Represents any individual with access to the system.

- **id**: `UUID` (Primary Key)
- **email**: `String` (Unique, Indexed)
- **passwordHash**: `String`
- **role**: `Enum` (HR_MANAGER, DEPARTMENT_HEAD, EMPLOYEE, JOB_APPLICANT)
- **createdAt**: `Timestamp`
- **updatedAt**: `Timestamp`

## 2. JobOpening
Represents a vacant position.

- **id**: `UUID` (Primary Key)
- **title**: `String`
- **description**: `Text`
- **status**: `Enum` (OPEN, CLOSED, DRAFT)
- **createdAt**: `Timestamp`
- **updatedAt**: `Timestamp`

## 3. Application
Represents a job applicant's submission for a job opening.

- **id**: `UUID` (Primary Key)
- **jobOpeningId**: `UUID` (Foreign Key to JobOpening)
- **applicantId**: `UUID` (Foreign Key to User)
- **status**: `Enum` (APPLIED, INTERVIEW, OFFER, REJECTED, WITHDRAWN)
- **submittedAt**: `Timestamp`
- **updatedAt**: `Timestamp`

## 4. OnboardingTask
Represents a task to be completed by a new hire.

- **id**: `UUID` (Primary Key)
- **title**: `String`
- **description**: `Text`
- **assigneeId**: `UUID` (Foreign Key to User)
- **dueDate**: `Date`
- **status**: `Enum` (PENDING, IN_PROGRESS, COMPLETED)
- **createdAt**: `Timestamp`
- **updatedAt**: `Timestamp`

## 5. PerformanceReview
Represents a formal assessment of an employee's performance.

- **id**: `UUID` (Primary Key)
- **employeeId**: `UUID` (Foreign Key to User)
- **reviewerId**: `UUID` (Foreign Key to User)
- **selfAssessment**: `Text`
- **reviewerComments**: `Text`
- **finalScore**: `Integer`
- **reviewPeriodStart**: `Date`
- **reviewPeriodEnd**: `Date`
- **status**: `Enum` (PENDING, IN_PROGRESS, COMPLETED)
- **createdAt**: `Timestamp`
- **updatedAt**: `Timestamp`

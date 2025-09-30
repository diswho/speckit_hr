# Quickstart

This document provides a quick way to test the core functionality of the HR Management Web Application, based on the user stories in the feature specification.

## Prerequisites
- The application is running locally.
- You have credentials for the different user roles (HR Manager, Department Head, Employee, Job Applicant).

## 1. Create a Job Opening (HR Manager)
1.  Log in as an HR Manager.
2.  Navigate to the "Recruiting" module.
3.  Click on "Create New Job Opening".
4.  Fill in the title and description.
5.  Click "Save".
6.  **Expected Result**: The new job opening is created and visible in the list of open positions.

## 2. Apply for a Job (Job Applicant)
1.  Log out from the HR Manager account.
2.  Register as a new Job Applicant.
3.  Navigate to the "Careers" page.
4.  Find the job opening created in the previous step.
5.  Click "Apply".
6.  **Expected Result**: You receive an email confirmation, and the application is visible in your dashboard with the status "Applied".

## 3. Assign Onboarding Tasks (HR Manager)
1.  Log in as an HR Manager.
2.  Navigate to the "Onboarding" module.
3.  Select a new hire.
4.  Assign a set of predefined onboarding tasks to the new hire.
5.  **Expected Result**: The onboarding tasks are assigned to the new hire.

## 4. Complete Onboarding Tasks (Employee)
1.  Log in as the new hire.
2.  On your dashboard, you should see a list of your onboarding tasks.
3.  Mark a task as "Completed".
4.  **Expected Result**: The task status is updated to "Completed".

## 5. Initiate a Performance Review (Department Head)
1.  Log in as a Department Head.
2.  Navigate to the "Performance" module.
3.  Select a team member.
4.  Click "Initiate Performance Review".
5.  **Expected Result**: A new performance review is created for the team member.
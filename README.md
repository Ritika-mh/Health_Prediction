# Health Prediction Application

## Project Overview
The Health Prediction Application is a full-stack web application that manages patient information and uses Google's Gemini AI API to generate possible health concerns based on blood test values.

## Technologies Used
- **Frontend:** Angular, TypeScript, HTML, CSS
- **Backend:** Python, Django REST Framework
- **Database:** MySQL
- **AI Integration:** Google Gemini API

## Features
- Add, view, update, and delete patient records (CRUD).
- Validate patient details, email addresses, dates of birth, and numeric blood test values.
- Prevent duplicate email addresses.
- Store patient records in a MySQL database.
- Generate AI-based health predictions using glucose, haemoglobin, and cholesterol values.
- Display the generated prediction in the Remarks field.
- Handle invalid patient records and API errors.

## Project Structure
```text
task2/
├── HealthcareBackend/
│   ├── health_prediction/
│   ├── requirements.txt
│   └── manage.py
└── HealthcareUI/
    ├── src/
    ├── package.json
    ├── package-lock.json
    └── angular.json
```

## Prerequisites
- Python
- Node.js and npm
- Angular CLI
- MySQL
- Google Gemini API key

## Backend Setup
1. Open a terminal and navigate to `HealthcareBackend`.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure the MySQL database in Django settings.
5. Configure your Gemini API key using an environment variable or another secure method. Do not commit real API keys to GitHub.
6. Apply migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. Start the backend:

   ```bash
   python manage.py runserver
   ```

## Frontend Setup
1. Open another terminal and navigate to `HealthcareUI`.
2. Install the dependencies:

   ```bash
   npm install
   ```

3. Start Angular:

   ```bash
   ng serve
   ```

4. Open the local URL displayed in the terminal, usually `http://localhost:4200`.

Ensure the frontend API URL matches the address of your running Django backend.

## API Endpoints
The backend provides endpoints for creating, retrieving, updating, and deleting patient records.

- `POST /api/users/create/` — Create a patient
- `POST /api/users/get/` — Retrieve a patient
- `POST /api/users/getall/` — Retrieve all patients
- `POST /api/users/update/` — Update a patient
- `POST /api/users/delete/` — Delete a patient

Confirm the endpoint paths against your Django URL configuration.

## Validation and Test Cases
The application validates required fields, email format, dates of birth, duplicate emails, and numeric blood test values. Invalid records are rejected with appropriate validation messages.

## Important Note
AI-generated health remarks are informational predictions, not medical diagnoses. Patients should consult a qualified healthcare professional for medical interpretation.

## Security
- Never commit API keys, passwords, database credentials, or `.env` files containing secrets.
- Use environment variables for sensitive configuration.

## Author
Developed as part of the Health Prediction Application assessment.

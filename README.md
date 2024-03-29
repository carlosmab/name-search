# Name search

## Description

Name Search is a FastAPI-based web application that provides three main functionalities:

1. PDF Conversion to Text: Upload a PDF file and convert it to text.

2. Name Extraction from Text: Extract names from a given text.

3. Word Search using Google Search Engine: Search for words or phrases on the Google search engine.

The following modules are still missing and need to be implemented:

- User Management: Module to handle user registration, login, and authentication.

- Search History: Module to store and retrieve user search history.

<br>

## Table of Contents

- [Name search](#name-search)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Authentication](#authentication)
  - [Endpoints](#endpoints)
  - [Tests](#tests)

<br>

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/carlosmab/name-search.git
   cd name-search
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  // For Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up authentication credentials (e.g., JWT tokens, OAuth2, etc.).

<br>

## Usage

1. Run the FastAPI application:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

2. Access the API documentation at `http://localhost:8000/docs`.

<br>

## Authentication

Authentication is required for all endpoints. You can obtain a token using the `/get-token` endpoint with the test credentials:

```json
// Test Credentials for obtaining the token
{
    "username": "user@email.com",
    "password": "password"
}
```

Implement authentication using your chosen method (e.g., JWT tokens, OAuth2, etc.).

<br>

## Endpoints

1. PDF Conversion to Text:

   - **Endpoint**: `/convert-pdf/text`
   - **Method**: POST
   - **Description**: Upload a PDF file and convert it to text.
   - **Authentication**: Required

2. Name Extraction from Text:

   - **Endpoint**: `/extract-names/`
   - **Method**: POST
   - **Description**: Extract names from a given text.
   - **Authentication**: Required

3. Word Search using Google Search Engine:

   - **Endpoint**: `/custom-search/google-cse/`
   - **Method**: POST
   - **Description**: Search for words or phrases on the Google search engine.
   - **Authentication**: Required

<br>

## Tests

To run the API tests:

```bash
python -m unittest discover tests/test_api
```

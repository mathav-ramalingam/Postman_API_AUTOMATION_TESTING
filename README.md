
# Password Management API with Postman Automation Testing

This repository contains a Python Flask API for managing passwords with specific criteria and a Postman automation testing setup to validate the functionality of the `/change-password` endpoint.

## Project Structure

- **Password_Management.py**: Python script implementing a Flask-based API with a single endpoint for changing passwords.
- **password_test_cases.csv**: CSV file containing various test cases for validating the `/change-password` endpoint in Postman.

## Requirements

Ensure you have the following installed on your system:
- **Python** 3.6+
- **Postman**
- **Flask**: Install Flask via `pip` if it is not already installed.

```bash
pip install Flask
```

## API Overview

This API provides a single endpoint, `/change-password`, which allows users to change their password if they meet the security requirements.

### Endpoint: `/change-password`
- **Method**: POST
- **Description**: Change a user's password.
- **Request Parameters**:
  - **email**: Email of the user (string, required).
  - **currentPassword**: The user's current password (string, required).
  - **newPassword**: The new password the user wants to set (string, required).

**Password Requirements**:
- Must be at least 8 characters.
- Must contain uppercase and lowercase letters.
- Must include at least one digit and one special character from the set `!@#$%^&*`.

### Example Request Body

```json
{
  "email": "user@example.com",
  "currentPassword": "CurrentPass123!",
  "newPassword": "NewPass123!"
}
```

### Example Response

- **Success** (200 OK):

    ```json
    {
      "message": "Password changed successfully"
    }
    ```

- **Error** (400 Bad Request or 404 Not Found):

    ```json
    {
      "error": "Detailed error message"
    }
    ```

## Setup and Running the Server

1. Clone the repository:

    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Run the Flask server:

    ```bash
    python Password_Management.py
    ```

3. The server will start at `http://localhost:3000`. Ensure it’s running before proceeding to the testing steps.

## Testing with Postman and Automating with CSV

This repository includes a `password_test_cases.csv` file, which contains various test cases for automated testing in Postman.

### Step-by-Step Testing in Postman

1. **Open Postman**.
2. **Create a New Request**:
   - Set the request method to `POST`.
   - Use the URL `http://localhost:3000/change-password`.

3. **Set Headers**:
   - In the "Headers" tab, add a header `Content-Type` with the value `application/json`.

4. **Automate Tests Using CSV File**:
   - In Postman, create a new collection named `Password Management Tests`.
   - Add the `/change-password` request to this collection.
   - Go to the "Runner" tool in Postman, which allows you to run the collection in bulk.
   - Select the `Password Management Tests` collection and choose the `/change-password` request.
   - In the "Runner" tool, enable "Data File" and upload the `password_test_cases.csv` file.
   - Configure the number of iterations if required, based on the number of rows in the CSV file.

### Writing Tests in Postman

In Postman, you can add tests for each scenario in the "Tests" tab:

1. **Add Success Tests**:

    ```javascript
    pm.test("Status code is 200", function () {
        pm.response.to.have.status(200);
    });

    pm.test("Success message received", function () {
        pm.expect(pm.response.json().message).to.eql("Password changed successfully");
    });
    ```

2. **Add Failure Tests** (Customize based on error cases):

    ```javascript
    pm.test("Status code is 400 or 404", function () {
        pm.expect(pm.response.code).to.be.oneOf([400, 404]);
    });

    pm.test("Error message present", function () {
        pm.expect(pm.response.json()).to.have.property("error");
    });
    ```

## Running the Automated Tests

Once the tests are configured:

1. Start the Flask server (`python Password_Management.py`).
2. Run the Postman collection with the CSV data file by clicking **Run**.
3. Check the results to ensure each test case passes or fails as expected.

## Example Test Cases in `password_test_cases.csv`

| email               | currentPassword | newPassword        | expected_status |
|---------------------|-----------------|--------------------|-----------------|
| alice@example.com   | Password123!    | NewPassword123!    | 200             |
| alice@example.com   | WrongPassword   | NewPassword123!    | 400             |
| nonexistent@example.com | Password123! | ValidPass123!      | 404             |

Each row represents a different scenario, including valid and invalid requests.

## Additional Notes

- This example uses in-memory data storage, which resets each time the server restarts. For a production setup, integrate a persistent database.
- Update test cases in `password_test_cases.csv` based on any changes in password requirements or API structure.


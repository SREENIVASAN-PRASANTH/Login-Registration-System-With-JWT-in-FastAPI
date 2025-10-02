# FastAPI JWT Authentication System
This is a user registration and login system built on FastAPI with JWT-based authentication, featuring secure password hashing and persistent user storage using SQLite. The project covers the full authentication flow from user signup to secure token-based profile access.

## Overview
This project demonstrates fundamental authentication techniques in modern web API development, including:

- Password hashing with bcrypt through passlib for security.

- Issuing and validating JWT access tokens for stateless authentication.

- Managing user data in SQLite for a lightweight backend.

- Using FastAPI's dependency injection and OAuth2PasswordBearer for secure route protection.

- Leveraging the interactive OpenAPI/Swagger API documentation.

- The system supports registering new users, logging in with credentials, and accessing a protected profile endpoint with a valid JWT.

## Key Concepts Learned
**JWT Authentication:** Creation of tokens that encode user identity, allowing token-based session management without server storage.

**Password Security:** Hashing passwords securely to prevent plaintext storage, using industry-standard bcrypt via passlib.

**OAuth2 Scheme:** FastAPI integration with OAuth2PasswordBearer to extract and verify tokens from requests.

**Dependency Injection:** Protecting routes by injecting and verifying current authenticated user from JWT.

**SQLite Integration:** Simple persistent storage for user records without additional external dependencies.

**Swagger/OpenAPI:** Self-generated interactive API documentation enabling easy endpoint testing.

## Installation & Setup
Install required dependencies:
```
pip install fastapi uvicorn python-jose[cryptography] passlib[bcrypt]
```

File structure:
```
JWT Auth System/
├── main.py # FastAPI app and authentication logic
├── database.py # SQLite user database handling
└── README.md # Project documentation (this file)
```

Start the FastAPI server:
```
uvicorn main:app --reload
```
Access interactive API docs at:
http://127.0.0.1:8000/docs

## API Usage
**Register new user: POST /register**

Request body example:

<img width="1794" height="563" alt="image" src="https://github.com/user-attachments/assets/2f7d71ae-08c5-4017-8df6-9001b5917fc0" />
<img width="682" height="299" alt="image" src="https://github.com/user-attachments/assets/7b4797d2-69d2-45ff-9bd2-4af16019c4b8" />

---

**Login user: POST /login**

Response example:

<img width="949" height="575" alt="image" src="https://github.com/user-attachments/assets/1fa1fc46-47a1-4d92-b495-36d2c6c8360f" />
<img width="1375" height="452" alt="image" src="https://github.com/user-attachments/assets/30c00282-d6bf-43a7-a371-598b0f2ad88d" />

---

**Get current user profile: GET /me (Requires Authorization Bearer token)**

Response example:

<img width="950" height="676" alt="image" src="https://github.com/user-attachments/assets/71508176-6e6c-40be-92a2-32f68dde086e" />


## Additional Notes on bcrypt and passlib Installation Issue
During setup, I faced an issue where bcrypt and passlib did not work correctly, throwing errors related to bcrypt version reading and password hashing limits. To fix this, I ran the following commands which resolved the problem:

```
pip uninstall bcrypt
pip uninstall passlib
pip install --no-cache-dir bcrypt==4.0.1 passlib
```
This forced installation of bcrypt version 4.0.1 (a stable known version compatible with passlib) and reinstalled passlib cleanly, resolving the errors.


Acknowledgments
I followed the documentation and tutorial on JWT authentication using FastAPI from GeeksforGeeks to learn core concepts and implemented the project. The coding and testing were done using Visual Studio Code editor for a better development experience.


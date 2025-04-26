# Health Information System

This project is a basic Health Information System built using **FastAPI** and **HTML/CSS/JavaScript**. It allows users to register clients, create health programs, enroll clients into programs, and search for clients.

## Features

- Register new clients with name and age
- Create health programs
- Enroll clients in one or more programs
- Search for clients by name
- View client profiles via a RESTful API

## Tools & Technologies

- **Backend**: FastAPI (Python)
- **Frontend**: HTML, CSS, JavaScript (Vanilla)
- **API Testing**: Swagger UI (via FastAPI `/docs`)
- **Version Control**: Git + GitHub

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Christineteen/Health-Information-System.git
   cd Health-Information-System
   
2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   
3. install dependaancies**
    ```bash
   pip install fastapi uvicorn

4. **run the first API backend**
   ```bash
   uvicorn main:app --reload

6. **Open the index.html file in a browser to interact with the frontend.**

7.**Access Swagger UI at:
http://127.0.0.1:8000/docs**

**DESIGN**
 Design Decisions
Used in-memory Python dictionaries to simulate databases.

UUIDs are used as unique identifiers for clients and programs.

RESTful routes follow semantic structure (e.g., /clients/{id}/enroll).

Frontend is kept minimal and styled using pure CSS.

![Screenshot 2025-04-26 042440](https://github.com/user-attachments/assets/50726c65-4711-40a8-8157-47f5bfbdc543)
![Screenshot 2025-04-26 042411](https://github.com/user-attachments/assets/c5820dac-9f3b-4a35-b0e1-16ec42cd4283)
![Screenshot 2025-04-26 042304](https://github.com/user-attachments/assets/0b0a5095-870b-499e-9878-05959387fd54)
![Screenshot 2025-04-26 042226](https://github.com/user-attachments/assets/f51de277-82cc-47fb-9da8-54f5b060a541)

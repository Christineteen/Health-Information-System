from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Optional
from uuid import uuid4

app = FastAPI()

# Data Models
class Program(BaseModel):
    id: str
    name: str

class Client(BaseModel):
    id: str
    name: str
    age: int
    enrolled_programs: List[str] = []

# In-memory databases
programs_db: Dict[str, Program] = {}
clients_db: Dict[str, Client] = {}

# Routes
@app.post("/programs", response_model=Program)
def create_program(name: str):
    program_id = str(uuid4())
    program = Program(id=program_id, name=name)
    programs_db[program_id] = program
    return program

@app.post("/clients", response_model=Client)
def register_client(name: str, age: int):
    client_id = str(uuid4())
    client = Client(id=client_id, name=name, age=age)
    clients_db[client_id] = client
    return client

@app.post("/clients/{client_id}/enroll")
def enroll_client(client_id: str, program_ids: List[str]):
    if client_id not in clients_db:
        raise HTTPException(status_code=404, detail="Client not found")
    for pid in program_ids:
        if pid not in programs_db:
            raise HTTPException(status_code=404, detail=f"Program {pid} not found")
    clients_db[client_id].enrolled_programs.extend(pid for pid in program_ids if pid not in clients_db[client_id].enrolled_programs)
    return {"message": "Client enrolled successfully"}

@app.get("/clients")
def search_clients(name: Optional[str] = None):
    if name:
        return [client for client in clients_db.values() if name.lower() in client.name.lower()]
    return list(clients_db.values())

@app.get("/clients/{client_id}", response_model=Client)
def get_client_profile(client_id: str):
    client = clients_db.get(client_id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.get("/")
def root():
    return {"message": "Welcome to the Health Information System API! Visit /docs for Swagger UI."}

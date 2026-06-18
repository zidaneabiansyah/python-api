# Cara jalankan:
#    uvicorn main:app --reload
#
# 1. Register: POST /register => body: {"username": "budi", "password": "rahasia"}
# 2. Login:    POST /login    => body: {"username": "budi", "password": "rahasia"}
#    -> dapet access_token
# 3. Profile:  GET /me        => Header: Authorization: Bearer <token>
#
# PostgreSQL (kalo ada):
#   DATABASE_URL = "postgresql://user:pass@localhost/dbname"
#   Kalo pake SQLite, file otomatis kebikin di folder ini

from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
import bcrypt
from jose import JWTError, jwt
from databases import Database
from datetime import datetime, timedelta
import uuid

# Konfigurasi

DATABASE_URL = "sqlite:///./auth.db"
# Ganti ke ini kalo pake PostgreSQL:
# DATABASE_URL = "postgresql://postgres:password@localhost/authdb"

SECRET_KEY = "rahasia-super-aman-ganti-pakai-env"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

database = Database(DATABASE_URL)
security = HTTPBearer()


# Database setup

async def init_db():
    await database.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    await init_db()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)


# Pydantic models

class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: str
    username: str
    created_at: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# Helper functions

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode(), hashed.encode())


def create_token(user_id: str, username: str) -> str:
    payload = {
        "sub": user_id,
        "username": username,
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
        "jti": str(uuid.uuid4()),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(cred: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(cred.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        username = payload.get("username")
        if user_id is None or username is None:
            raise HTTPException(status_code=401, detail="Token tidak valid")
    except JWTError:
        raise HTTPException(status_code=401, detail="Token tidak valid")

    query = "SELECT id, username, created_at FROM users WHERE id = :id"
    user = await database.fetch_one(query, {"id": user_id})
    if user is None:
        raise HTTPException(status_code=401, detail="User tidak ditemukan")
    return dict(user)


# Endpoints

@app.post("/register", response_model=UserResponse)
async def register(data: UserRegister):
    if len(data.password) < 4:
        raise HTTPException(status_code=400, detail="Password minimal 4 karakter")

    existing = await database.fetch_one(
        "SELECT id FROM users WHERE username = :username",
        {"username": data.username},
    )
    if existing:
        raise HTTPException(status_code=400, detail="Username sudah dipakai")

    user_id = str(uuid.uuid4())
    password_hash = hash_password(data.password)
    created_at = datetime.utcnow().isoformat()

    await database.execute(
        "INSERT INTO users (id, username, password_hash, created_at) VALUES (:id, :username, :password_hash, :created_at)",
        {"id": user_id, "username": data.username, "password_hash": password_hash, "created_at": created_at},
    )

    return {"id": user_id, "username": data.username, "created_at": created_at}


@app.post("/login", response_model=TokenResponse)
async def login(data: UserLogin):
    user = await database.fetch_one(
        "SELECT id, username, password_hash FROM users WHERE username = :username",
        {"username": data.username},
    )
    if user is None or not verify_password(data.password, user["password_hash"]):
        raise HTTPException(status_code=401, detail="Username atau password salah")

    token = create_token(user["id"], user["username"])
    return {"access_token": token}


@app.get("/me", response_model=UserResponse)
async def get_profile(user: dict = Depends(get_current_user)):
    return user


@app.get("/users", response_model=list[UserResponse])
async def list_users(user: dict = Depends(get_current_user)):
    query = "SELECT id, username, created_at FROM users"
    rows = await database.fetch_all(query)
    return [dict(row) for row in rows]

import sqlite3
from fastapi import HTTPException
from typing import Optional

DB_PATH = "users.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        create table if not exists users(
            username text primary key,
            hashed_password text not null,
            full_name text)
    """)
    conn.commit()
    conn.close()

def get_user(username: str) -> Optional[dict]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    row = conn.execute("SELECT username, hashed_password, full_name from users where username = ?",(username,)).fetchone()
    conn.close()

    if row:
        return {"username": row["username"], "hashed_password": row["hashed_password"], "full_name":row["full_name"]}
    return None

def create_user(username: str, hashed_password: str, full_name:str = ""):
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute(
            "insert into users (username, hashed_password, full_name) values (?,?,?)",(username,hashed_password,full_name)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        raise HTTPException(status_code = 409, detail = "Username already taken")
    finally:
        conn.close()


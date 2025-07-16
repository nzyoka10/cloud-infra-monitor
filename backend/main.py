# File: backend/main.py
# Description: FastAPI application to receive metrics and save them to PostgreSQL

from fastapi import FastAPI, Request
import psycopg2
import os

app = FastAPI()

@app.post("/metrics")
async def receive_metrics(request: Request):
    data = await request.json()

    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST")
    )

    # Insert metrics data
    cur = conn.cursor()
    cur.execute("INSERT INTO metrics (cpu, memory) VALUES (%s, %s);",
                (data['cpu'], data['memory']))
    conn.commit()

    cur.close()
    conn.close()
    return {"status": "saved"}

# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import get_conn
from app.queries import USER_SENTIMENT_QUERY
from app.models import UserSentiment

app = FastAPI()

# --- CORS ---
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -------------

@app.get("/")
def home():
    return {"status": "FastAPI + StarRocks is running!"}


@app.get("/user/{username}", response_model=UserSentiment)
def get_sentiment(username: str):
    conn = get_conn()
    cur = conn.cursor(dictionary=True)

    cur.execute(USER_SENTIMENT_QUERY, (username,))
    result = cur.fetchone()

    cur.close()
    conn.close()

    if not result:
        return {
            "user": username,
            "total_posts": 0,
            "positive_posts": 0,
            "negative_posts": 0,
            "satisfaction_percentage": 0.0,
            "complaints_percentage": 0.0
        }

    return result

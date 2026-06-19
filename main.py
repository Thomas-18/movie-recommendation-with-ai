from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(title="AI Movie Recommender")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Request Model
class MovieRequest(BaseModel):
    genre: str
    mood: str


@app.get("/")
def home():
    return {
        "message": "🎬 AI Movie Recommendation API is running"
    }


@app.post("/recommend")
def recommend_movies(data: MovieRequest):

    prompt = f"""
You are a professional movie recommendation expert.

Recommend EXACTLY 5 movies.

Genre: {data.genre}
Mood: {data.mood}

Rules:
- Do NOT use markdown
- Do NOT use ** symbols
- Do NOT use bullet points
- Keep descriptions short and engaging

Format:

Movie: Movie Name (Year)
Description: Short description

Movie: Movie Name (Year)
Description: Short description
"""

    try:

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.8,
            max_tokens=1000
        )

        recommendations = (
            response
            .choices[0]
            .message
            .content
        )

        # Remove any markdown if AI still generates it
        recommendations = recommendations.replace("**", "")

        return {
            "recommendations": recommendations
        }

    except Exception as e:

        return {
            "recommendations":
            f"Error generating recommendations: {str(e)}"
        }
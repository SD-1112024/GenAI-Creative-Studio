# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load your .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize FastAPI
app = FastAPI(title="GenAI Creative Studio Backend")

# Request body model
class StoryRequest(BaseModel):
    prompt: str

# Simple home route to check server
@app.get("/")
def home():
    return {"message": "GenAI Backend Running Successfully!"}

# Endpoint to generate story
@app.post("/generate-story")
def generate_story(request: StoryRequest):
    prompt_text = request.prompt
    try:
        response = client.chat.completions.create(
           model="gpt-3.5-turbo",  # changed from gpt-4
           messages=[{"role": "user", "content": prompt_text}],
           max_tokens=500
        )

        story_text = response.choices[0].message.content
        return {"story": story_text}
    except Exception as e:
        return {"error": str(e)}

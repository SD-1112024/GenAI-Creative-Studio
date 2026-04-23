import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Load the Key
load_dotenv()

# 2. Check if Key exists
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("❌ ERROR: API Key not found! Check your .env file.")
else:
    print(f"✅ SUCCESS: API Key found (Starts with {api_key[:5]}...)")

# 3. Test the Brain
try:
    llm = ChatGoogleGenerativeAI(model="models/gemini-flash-latest")
    response = llm.invoke("Say 'System Online' if you can hear me.")
    print(f"🤖 AI RESPONSE: {response.content}")
except Exception as e:
    print(f"❌ CONNECTION ERROR: {e}")
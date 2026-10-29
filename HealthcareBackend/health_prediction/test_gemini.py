import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

print(os.getenv("GEMINI_API_KEY"))

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("models/gemini-flash-latest")

response = model.generate_content("Hello")

print(response.text)
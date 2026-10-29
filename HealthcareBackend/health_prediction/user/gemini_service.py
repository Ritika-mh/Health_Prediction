
from google import genai
from django.conf import settings
import time

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


def generate_health_prediction(patient):
    
    
    prompt = f"""
You are an AI health prediction assistant.

Analyze the patient's blood test values and predict a possible
health condition or disease risk based on the available data.

Patient blood test results:
Glucose: {patient.glucose}
Haemoglobin: {patient.haemoglobin}
Cholesterol: {patient.cholesterol}

Instructions:
- Consider all three blood test values.
- Identify the most relevant possible health concern, if supported
  by the available information.
- Do not assume measurement units or reference ranges.
- Do not claim a definite diagnosis.
- If the information is insufficient, state that clearly.
- Recommend medical consultation when appropriate.

Return ONLY one concise, meaningful sentence of no more than
20 words, suitable for the application's Remarks column.
Do not include the patient's name, headings, bullet points,
or extra explanation.
"""



    for attempt in range(2):
        try:
            response = client.models.generate_content(
                # model="gemini-flash-latest",
                model="gemma-4-26b-a4b-it",
                contents=prompt
            )

            result = (response.text or "").strip()

            if result:
                return " ".join(result.split())

            return None

        except Exception as e:
            print(f"Gemini API attempt {attempt + 1} failed: {e}")

            if attempt == 0:
                time.sleep(2)

    return None

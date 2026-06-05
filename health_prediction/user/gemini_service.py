from google import genai
from django.conf import settings

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)

def generate_health_prediction(patient):

    try:
        prompt = f"""
You are a medical AI.

Return ONLY ONE LINE.

No name, no explanation, no formatting.

Patient data:
Glucose: {patient.glucose}
Hemoglobin: {patient.haemoglobin}
Cholesterol: {patient.cholesterol}
"""

        response = client.models.generate_content(
            model="models/gemini-flash-latest",
            contents=prompt
        )

        result = response.text.strip().replace("\n", " ")

        if not result:
            return None

        return result

    except Exception as e:
        # IMPORTANT: fail safe
        return None
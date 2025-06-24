import os
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_response(user_input):
    input_lower = user_input.lower()

    # Hardcoded quick responses
    if "mental" in input_lower or "depression" in input_lower:
        return "📞 Mental Health Helpline: 1-800-555-1234"
    elif "abuse" in input_lower or "violence" in input_lower:
        return "📞 Domestic Abuse Hotline: 1-800-999-9999"
    elif "police" in input_lower or "crime" in input_lower:
        return "📞 Call 911 for emergencies. For local police: 1-317-555-2121"
    elif "shelter" in input_lower or "homeless" in input_lower:
        return "🏠 Find local shelters: www.indyshelters.org or call 1-800-555-1212"
    
    # Use GPT for other input
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change to gpt-4 if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant providing public safety support for Indiana residents."},
                {"role": "user", "content": user_input}
            ],
            max_tokens=150,
            temperature=0.5
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I couldn't process your request. Please try again later."

def get_response(user_input):
    input_lower = user_input.lower()

    # Fast hardcoded keyword-based help (still useful)
    if "mental" in input_lower or "depression" in input_lower:
        return "For mental health support, call the Indiana Mental Health Helpline: 📞 1-800-555-1234"
    elif "abuse" in input_lower or "violence" in input_lower:
        return "If you are facing domestic abuse, contact Indiana Safe Shelter: 📞 1-800-999-9999"
    elif "police" in input_lower or "crime" in input_lower:
        return "For emergencies, dial 911. For non-emergencies, call Indianapolis Police: 📞 1-317-555-2121"
    elif "shelter" in input_lower or "homeless" in input_lower:
        return "You can find local shelters at www.indyshelters.org or call 📞 1-800-555-1212"
    
    # Otherwise, use GPT-4 to generate a smart response
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo" for faster/cheaper
            messages=[
                {"role": "system", "content": "You are CrisisConnect, a helpful chatbot assisting Indiana residents with public safety, mental health, shelter access, and emergency contacts."},
                {"role": "user", "content": user_input}
            ],
            temperature=0.5,
            max_tokens=150
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I couldn't process your request. Please try again later."

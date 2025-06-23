# chatbot_logic.py

def get_response(user_input):
    input_lower = user_input.lower()

    if "mental" in input_lower or "depression" in input_lower:
        return "For mental health support, please call the Indiana Mental Health Helpline: 📞 1-800-555-1234"
    elif "abuse" in input_lower or "violence" in input_lower:
        return "If you are facing domestic abuse, contact the Indiana Safe Shelter: 📞 1-800-999-9999"
    elif "police" in input_lower or "crime" in input_lower:
        return "For emergencies, dial 911. For non-emergencies, call Indianapolis Police: 📞 1-317-555-2121"
    elif "shelter" in input_lower or "homeless" in input_lower:
        return "You can find local shelters at www.indyshelters.org or call 📞 1-800-555-1212"
    else:
        return "I'm here to help! Could you please provide more details or use keywords like 'mental health', 'violence', 'shelter'?"

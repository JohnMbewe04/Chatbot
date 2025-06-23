from dotenv import load_dotenv
import os
import openai

load_dotenv()  # This loads variables from the .env file

openai.api_key = os.getenv("OPENAI_API_KEY")
print("API KEY:", "FOUND" if openai.api_key else "NOT FOUND")

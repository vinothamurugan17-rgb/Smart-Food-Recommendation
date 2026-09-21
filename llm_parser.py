import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Load Gemini API key from .env
load_dotenv()

# Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

# Prompt for extracting food preferences
prompt = ChatPromptTemplate.from_template("""
You are a food preference extraction assistant.

Read the user's food request and extract these values:

1. meal
2. diet
3. hunger
4. health_preference
5. calorie_preference

Return ONLY one line in this exact format:

meal|diet|hunger|health_preference|calorie_preference

Rules:
- meal must be breakfast, lunch, or dinner
- diet must be vegetarian or non-vegetarian
- hunger must be a number from 0 to 100
- health_preference must be a number from 0 to 100
- calorie_preference must be a number from 0 to 100

Examples:

User: I am very hungry and want a healthy vegetarian breakfast.
Output:
breakfast|vegetarian|90|90|50

User: I want a light dinner with low calories.
Output:
dinner|vegetarian|40|70|90

User request:
{user_input}
""")


def extract_preferences(user_input):

    # Create LangChain messages
    messages = prompt.format_messages(
        user_input=user_input
    )

    # Send request to Gemini through LangChain
    response = llm.invoke(messages)

    # Gemini may return text as a string or a list
    content = response.content

    if isinstance(content, list):
        text = ""

        for item in content:
            if isinstance(item, dict) and "text" in item:
                text += item["text"]

        content = text

    result = str(content).strip()

    # Remove accidental code formatting if Gemini adds it
    result = result.replace("```", "").strip()

    # Split the response
    parts = result.split("|")

    if len(parts) != 5:
        raise ValueError(
            f"Unexpected Gemini response: {result}"
        )

    # Convert the extracted values into usable data
    return {
        "meal": parts[0].strip().lower(),
        "diet": parts[1].strip().lower(),
        "hunger": int(parts[2].strip()),
        "health_preference": int(parts[3].strip()),
        "calorie_preference": int(parts[4].strip())
    }
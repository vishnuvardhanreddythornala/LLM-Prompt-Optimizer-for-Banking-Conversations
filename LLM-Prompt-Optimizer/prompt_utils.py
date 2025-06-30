import json
import os
from typing import List, Dict
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage

# Load environment variables (for Groq API key)
from dotenv import load_dotenv
load_dotenv()

# Initialize the Groq LLM client
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama3-70b-8192",  # correct parameter name is 'model'
    api_key=groq_api_key         # correct parameter name is 'api_key'
)


def load_prompts_from_jsonl(file_path: str) -> List[Dict]:
    """
    Reads prompts from a given JSONL file and returns them as a list of dictionaries.
    """
    prompts = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                prompts.append(data)
            except json.JSONDecodeError as e:
                print(f"Skipping line due to error: {e}")
    return prompts

def generate_response(prompt_data: Dict) -> str:
    """
    Sends prompt to Groq and returns the assistant's response.
    """
    messages = [
        SystemMessage(content=prompt_data["system_prompt"]),
        HumanMessage(content=prompt_data["user_input"])
    ]

    response = llm.invoke(messages)
    return response.content.strip()

def save_responses_to_jsonl(data: List[Dict], output_path: str) -> None:
    """
    Saves updated prompts (with assistant responses) to a new JSONL file.
    """
    with open(output_path, "w", encoding="utf-8") as f:
        for entry in data:
            json.dump(entry, f)
            f.write("\n")

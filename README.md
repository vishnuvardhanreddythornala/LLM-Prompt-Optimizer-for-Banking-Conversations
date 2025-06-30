# LLM-Prompt-Optimizer for Banking Conversations

> A Streamlit-based tool to design, test, and evaluate prompt styles for banking assistance.

## 📑 Table of Contents
- [About the Project](#about-the-project)
- [Demo](#demo)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Limitations and Future Work](#limitations-and-future-work)
- [License](#license)
- [Contact](#contact)

## 📖 About the Project
As banking moves toward AI-powered virtual assistants, getting the right response depends heavily on the way prompts are written.  
This tool helps optimize those prompts through realistic testing and rating.  
It simulates user queries (like balance check, KYC, loan status) using different styles (direct, empathetic, few-shot), then evaluates the assistant’s responses.

## 🎥 Demo
> [coming soon]

## ✨ Features
- Choose banking task: Balance Check, KYC, or Loan Status.
- Select prompt style (e.g., Direct, Empathetic, Few-shot).
- Type your own query and see LLM-generated assistant reply.
- Toggle between Beginner and Advanced view.
- Rate assistant response (Relevance, Clarity, Accuracy, Tone).
- Save evaluations as CSV logs for analysis.

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **LangChain**
- **Groq (LLM API)**
- **OpenAI**
- **Pandas**

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/vishnuvardhanreddythornala/LLM-Prompt-Optimizer.git

# Navigate to the project directory
cd LLM-Prompt-Optimizer

# Install dependencies
pip install -r requirements.txt

# Configure API keys:
Create a .env file in the root directory
Add your Groq API key:
[API_keys]
GROQ_API_KEY = your_api_key_here

# Run the app
streamlit run streamlit_app.py
```
## 🚀 Usage
- Select a banking task (e.g., Balance Check).
- Choose a prompt style (e.g., Empathetic).
- Enter your own user message (e.g., “Can I know my balance?”).
- Click Generate Assistant Response.
- View the AI-generated reply.
- If in Advanced mode, rate the reply on four metrics.
- Click Save Evaluation to log feedback in CSV.
```

## 📁 Project Structure
bash

LLM-Prompt-Optimizer/
├── prompts/
│   ├── balance_check.jsonl
│   ├── kyc_process.jsonl
│   └── loan_status.jsonl
├── results/
│   └── evaluation_log.csv
├── .env
├── streamlit_app.py
├── prompt_utils.py
├── requirements.txt
└── .env
```

## ⚡ Limitations and Future Work
- Current prompts and tasks are predefined.
- Voice input has been removed to avoid complexity.
- Future Work:
- I Add audio input and voice response (optional).
- Integrate analytics dashboard to visualize ratings.
- Support more banking tasks and feedback types.
```

## 📜 License
This project is licensed under the MIT License.

## 📞 Contact
Name: Thornala Vishnu Vardhan Reddy

GitHub: @vishnuvardhanreddythornala

Email: vishnuvardhanreddythornala@gmail.com
```

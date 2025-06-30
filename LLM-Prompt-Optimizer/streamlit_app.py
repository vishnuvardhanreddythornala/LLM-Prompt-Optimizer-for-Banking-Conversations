import streamlit as st
import os
import pandas as pd
from prompt_utils import load_prompts_from_jsonl, generate_response

# 🔧 Page setup
st.set_page_config(page_title="VoiceBot Prompt Optimizer", layout="centered")
st.title("🎯LLM Prompt Optimizer for Banking Conversations🏦")
st.markdown("Use this tool to test and evaluate different prompt styles for banking-related conversations.")

# 🔄 View mode toggle
view_mode = st.radio("🧭 Select View Mode:", ["Beginner", "Advanced"], horizontal=True)

# 📂 Available banking tasks mapped to files
TASK_MAP = {
    "Balance Check": "prompts/balance_check.jsonl",
    "KYC Process": "prompts/kyc_process.jsonl",
    "Loan Status": "prompts/loan_status.jsonl"
}

# 🎯 Select task and prompt style
task_name = st.selectbox("📌 Select a Banking Task", list(TASK_MAP.keys()))
prompt_file = TASK_MAP[task_name]
prompts = load_prompts_from_jsonl(prompt_file)
styles = list(set(p["style"] for p in prompts))
style = st.selectbox("🎨 Select Prompt Style", styles)

# 📄 Load selected prompt template
style_prompt = next((p for p in prompts if p["style"] == style), None)

# 🔍 Show System Prompt
if style_prompt:
    if view_mode == "Beginner":
        st.markdown("### 🧠 Prompt Used")
        st.code(style_prompt["system_prompt"], language="markdown")
    else:
        st.markdown("### 🔍 Prompt Design Preview")
        with st.expander("📄 Show Prompt Sent to AI"):
            st.code(style_prompt["system_prompt"], language="markdown")
else:
    st.warning("No prompt template found for selected style.")
    st.stop()

# 💬 User Input
user_input = st.text_area("✍️ Type your own user message", placeholder="e.g. What’s my current loan balance?")

# 🔁 Store response in session
if "response" not in st.session_state:
    st.session_state.response = None

# 🚀 Generate Assistant Response
if st.button("🚀 Generate Assistant Response") and user_input.strip():
    with st.spinner("Talking to Groq..."):
        custom_prompt = {
            "system_prompt": style_prompt["system_prompt"],
            "user_input": user_input
        }
        response = generate_response(custom_prompt)
        st.session_state.response = response
        st.success("Got a response!")

# 🤖 Show Response and Optional Feedback
if st.session_state.response:
    st.markdown("### 🤖 Assistant Reply")
    st.info(st.session_state.response)

    if view_mode == "Advanced":
        st.markdown("### 📊 Rate the Assistant's Response")
        relevance = st.slider("Relevance", 0, 5, key="rel")
        clarity = st.slider("Clarity", 0, 5, key="cla")
        accuracy = st.slider("Accuracy", 0, 5, key="acc")
        tone = st.slider("Tone", 0, 5, key="ton")

        if st.button("✅ Save Evaluation"):
            os.makedirs("results", exist_ok=True)
            log_data = {
                "task": task_name,
                "style": style,
                "user_input": user_input,
                "assistant_response": st.session_state.response,
                "relevance": relevance,
                "clarity": clarity,
                "accuracy": accuracy,
                "tone": tone
            }
            df = pd.DataFrame([log_data])
            output_path = "results/evaluation_log.csv"
            if os.path.exists(output_path):
                df.to_csv(output_path, mode='a', header=False, index=False)
            else:
                df.to_csv(output_path, index=False)
            st.success("📁 Logged to evaluation_log.csv")

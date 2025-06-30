import os
from prompt_utils import load_prompts_from_jsonl, generate_response, save_responses_to_jsonl

# Set your prompt file (you can switch this to 'kyc_process.jsonl' or 'loan_status.jsonl')
PROMPT_FILE = "prompts/balance_check.jsonl"
OUTPUT_FILE = "results/balance_check_with_responses.jsonl"

def main():
    # Step 1: Load prompts
    if not os.path.exists(PROMPT_FILE):
        print(f"Prompt file '{PROMPT_FILE}' not found.")
        return

    prompts = load_prompts_from_jsonl(PROMPT_FILE)
    print(f"Loaded {len(prompts)} prompts from {PROMPT_FILE}")

    # Step 2: Generate assistant responses
    for i, prompt in enumerate(prompts):
        print(f"\n[{i+1}] USER: {prompt['user_input']}")
        try:
            response = generate_response(prompt)
            prompt['assistant_response'] = response
            print(f"     BOT: {response}")
        except Exception as e:
            print(f"     ⚠️ Error: {e}")
            prompt['assistant_response'] = "ERROR"

    # Step 3: Save the updated data
    os.makedirs("results", exist_ok=True)
    save_responses_to_jsonl(prompts, OUTPUT_FILE)
    print(f"\n✅ Responses saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()

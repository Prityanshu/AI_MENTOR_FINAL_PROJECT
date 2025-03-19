import json
from rapidfuzz import process, fuzz

# Load FAQs from JSON file
def load_faqs(file_path="Afaqs.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("faqs", {})
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Error: Could not load FAQ file. Check if the file exists and has valid JSON.")
        return {}

# Get best-matching FAQ answer
def get_academic_answer(question, faqs):
    faq_keys = list(faqs.keys())  # Extract all FAQ question keys
    
    if not faq_keys:
        return "❌ No FAQs found. Please check if the FAQ file exists and has valid data."

    # Debugging: Print similarity scores for all FAQ keys
    matches = process.extract(question, faq_keys, scorer=fuzz.partial_ratio, limit=3)
    for match in matches:
        print(f"🔍 Possible match: {match[0]} (Score: {match[1]})")

    # Find the best match
    best_match, score, _ = matches[0]

    # If similarity score is 50 or higher, return the matched FAQ answer
    if score >= 50:
        return faqs[best_match]
    else:
        return "❌ Sorry, I couldn't find an exact match for your question. Please check the university website or contact the administration."

# Main interactive loop
if __name__ == "__main__":
    faqs = load_faqs()  # Load FAQs once
    while True:
        question = input("Enter your academic query (or type 'exit' to quit): ").strip().lower()
        if question == "exit":
            break
        response = get_academic_answer(question, faqs)
        print(response)
import json
from rapidfuzz import process, fuzz

# Load FAQs from JSON file
def load_faqs(file_path="Afaqs.json"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data.get("faqs", {})
    except (FileNotFoundError, json.JSONDecodeError):
        print("❌ Error: Could not load FAQ file. Check if the file exists and has valid JSON.")
        return {}

# Get best-matching FAQ answer
def get_academic_answer(question, faqs):
    faq_keys = list(faqs.keys())  # Extract all FAQ question keys
    
    if not faq_keys:
        return "❌ No FAQs found. Please check if the FAQ file exists and has valid data."

    # Debugging: Print similarity scores for all FAQ keys
    matches = process.extract(question, faq_keys, scorer=fuzz.partial_ratio, limit=3)
    
    if not matches:
        return "❌ No matching FAQs found."

    # Find the best match
    best_match, score, _ = matches[0]

    # If similarity score is 50 or higher, return the matched FAQ answer
    if score >= 50:
        return faqs[best_match]
    else:
        return "❌ Sorry, I couldn't find an exact match for your question. Please check the university website or contact the administration."

# New function to be used in chatbot.py
def handle_academic_query(question):
    faqs = load_faqs()  # Load FAQs once
    return get_academic_answer(question, faqs)

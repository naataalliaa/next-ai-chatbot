import requests
import json

OPENROUTER_API_KEY = "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"
LLAMA_API_ENDPOINT = "https://openrouter.ai/api/v1/chat/completions"

#authentication
headers = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json",
}

def llama_generate(query):
    payload = {
        "model": "meta-llama/llama-3.1-8b-instruct:free",  # Specify the model
        "messages": [
            {"role": "user", "content": query}
        ]
    }

    response = requests.post(LLAMA_API_ENDPOINT, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"]  # Assuming this structure from the API response
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None


# Travel Places Suggestion
def suggest_travel_places(query):
    return llama_generate(query)


# Explaining the History of a Place
def explain_history(query):
    return llama_generate(query)


# Booking Travel Cancellations
def book_cancellation(query):
    return f"Booking cancellation for query: {query} has been processed."


# Refunding
def process_refund(query):
    return f"Refund processed for query: {query}."


# Local Cuisine Guides
def local_cuisine_guides(query):
    return llama_generate(query)


# Router Function
def router(query):
    if "suggest" or "recommend" or "suggestion" or "recommendation" in query.lower():
        return suggest_travel_places(query)
    elif "history" in query.lower():
        return explain_history(query)
    elif "cancel" or "cancellation" in query.lower():
        return book_cancellation(query)
    elif "refund" in query.lower():
        return process_refund(query)
    elif "cuisine" or "food" or "restaurant" in query.lower():
        return local_cuisine_guides(query)
    else:
        return "I'm not sure how to help with that. Please try rephrasing your query."


def handle_query(query):
    response = router(query)
    print(f"Query: {query}")
    print(f"Response: {response}")


# Example
if __name__ == "__main__":
    user_query_1 = "Can you suggest some quiet places in Europe for a solo traveler?"
    user_query_2 = "Explain the history of the Colosseum."
    user_query_3 = "Please cancel my booking for tomorrow."
    user_query_4 = "I need a refund for my last purchase."
    user_query_5 = "What are the best local cuisines in Italy?"

    handle_query(user_query_1)
    handle_query(user_query_2)
    handle_query(user_query_3)
    handle_query(user_query_4)
    handle_query(user_query_5)
